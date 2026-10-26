#!/usr/bin/env python3
"""Re-encode master MP4s from videos-images/ into docs/assets/videos/ for the web.

Safari-safe H.264: yuv420p, High profile, even dimensions, faststart.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "videos-images"
OUT_DIR = ROOT / "docs" / "assets" / "videos"

# Same basename in → out (approved mapping).
VIDEOS = [
    "driver-extension-mac-intel.mp4",
    "connect-device.mp4",
    "bluebox-sizes.mp4",
    "new-user-dirp.mp4",
    "custom-frequencies-selection.mp4",
    "live-dirp.mp4",
    "analysis-navigation.mp4",
    "pathogens.mp4",
    "dirp-comparison.mp4",
]

MAX_HEIGHT = 720
VIDEO_BITRATE = "1200k"
AUDIO_BITRATE = "128k"


def _have_ffmpeg() -> bool:
    return shutil.which("ffmpeg") is not None


def _human(n: int) -> str:
    size = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} {unit}"
        size /= 1024
    return f"{size:.1f} GB"


def _has_audio(src: Path) -> bool:
    probe = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "a",
            "-show_entries",
            "stream=codec_type",
            "-of",
            "csv=p=0",
            str(src),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    return bool(probe.stdout.strip())


def compress_one(src: Path, dst: Path, *, force: bool = False) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if (
        not force
        and dst.exists()
        and dst.stat().st_mtime >= src.stat().st_mtime
    ):
        print(f"skip (up to date): {dst.name}")
        return

    print(f"encode: {src.name} ({_human(src.stat().st_size)}) → {dst.name}")
    tmp = dst.with_suffix(".tmp.mp4")
    if tmp.exists():
        tmp.unlink()

    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(src),
        "-vf",
        f"scale=-2:{MAX_HEIGHT}",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-profile:v",
        "high",
        "-level",
        "4.0",
        "-b:v",
        VIDEO_BITRATE,
        "-movflags",
        "+faststart",
    ]
    if _has_audio(src):
        cmd.extend(["-c:a", "aac", "-b:a", AUDIO_BITRATE])
    else:
        cmd.append("-an")
    cmd.append(str(tmp))

    subprocess.run(cmd, check=True)
    tmp.replace(dst)
    print(f"  done: {_human(dst.stat().st_size)}")


def main() -> int:
    force = "--force" in sys.argv
    if not _have_ffmpeg():
        print(
            "ffmpeg not found on PATH. Install with: brew install ffmpeg",
            file=sys.stderr,
        )
        return 1
    if not SRC_DIR.is_dir():
        print(f"missing source dir: {SRC_DIR}", file=sys.stderr)
        return 1

    subprocess.run(
        ["ffmpeg", "-version"],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    failures = 0
    for name in VIDEOS:
        src = SRC_DIR / name
        dst = OUT_DIR / name
        if not src.is_file():
            print(f"missing source: {src}", file=sys.stderr)
            failures += 1
            continue
        try:
            compress_one(src, dst, force=force)
        except Exception as exc:  # noqa: BLE001 — report and continue
            print(f"FAILED {name}: {exc}", file=sys.stderr)
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
