#!/usr/bin/env python3
"""Re-encode master MP4s from videos-images/ into docs/assets/videos/ for the web."""

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
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} {unit}"
        n /= 1024
    return f"{n:.1f} GB"


def compress_one(src: Path, dst: Path) -> None:
    from moviepy import VideoFileClip

    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
        print(f"skip (up to date): {dst.name}")
        return

    print(f"encode: {src.name} ({_human(src.stat().st_size)}) → {dst.name}")
    clip = VideoFileClip(str(src))
    try:
        h = clip.h or 0
        if h > MAX_HEIGHT:
            clip = clip.resized(height=MAX_HEIGHT)
        # moviepy 2.x write_videofile; ffmpeg_params for faststart
        clip.write_videofile(
            str(dst),
            codec="libx264",
            audio_codec="aac",
            bitrate=VIDEO_BITRATE,
            audio_bitrate=AUDIO_BITRATE,
            fps=clip.fps or 30,
            logger=None,
            ffmpeg_params=["-movflags", "+faststart"],
        )
    finally:
        clip.close()

    print(f"  done: {_human(dst.stat().st_size)}")


def main() -> int:
    if not _have_ffmpeg():
        print(
            "ffmpeg not found on PATH. Install with: brew install ffmpeg",
            file=sys.stderr,
        )
        return 1
    if not SRC_DIR.is_dir():
        print(f"missing source dir: {SRC_DIR}", file=sys.stderr)
        return 1

    # Sanity: ffmpeg responds
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
            compress_one(src, dst)
        except Exception as exc:  # noqa: BLE001 — report and continue
            print(f"FAILED {name}: {exc}", file=sys.stderr)
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
