# How to install F-SCANT

The installation will vary a bit depending on your computer. On Windows you receive an installer file. On a Mac you receive the F-SCANT app, which you put in the Applications folder. F-SCANT is not sold in the Microsoft Store or the Mac App Store.

## How to install on Windows

1. Double-click the installer you received (**F-SCANT-Setup-x64.exe**). If Windows asks for permission, allow it (you may need an administrator password).
2. Accept the F-SCANT licence and the Silicon Labs licence when they appear. Silicon Labs makes the small USB helper that lets the computer talk to the F-SCAN. The installer puts that helper on the PC for you.
3. Open **F-SCANT** from the Windows Start menu.

If Windows shows a SmartScreen warning (a blue or yellow screen that says Windows protected your PC), it means Windows does not yet know the publisher of this installer. That can happen because you received the file directly, not from the Microsoft Store. If you got the installer from your supplier, click the option to run it anyway.

If Windows asks you to allow apps that did not come from the store, allow it for this install. That setting is what lets F-SCANT run on the PC.

## How to install on a Mac

1. Copy **F-SCANT** into the Applications folder.
2. Install the USB helper that came in the same folder as F-SCANT. Read **SILICON-LABS-VCP-LICENSE.txt** first. Open **Mac_OSX_VCP_Driver.zip**, open the disk image inside, and run **Install CP210x VCP Driver**. This helper lets the Mac see the F-SCAN on USB.
3. When macOS asks you to allow software from Silicon Labs, turn that permission on.
4. Open **F-SCANT**.

Pictures of the USB helper steps are in [Connect the F-SCAN on a Mac](connect-mac.md).

### Enable Silabs driver on macOS Intel

Video 1. Enable the Silicon Labs driver on a Mac.

<video controls preload="none" width="100%" src="assets/videos/driver-extension-mac-intel.mp4">
  Your browser does not support the video tag.
</video>

If macOS says the developer cannot be verified, it means the Mac is blocking an app that did not come from the App Store. That is expected for F-SCANT. Open it with Apple’s [Open Anyway](https://support.apple.com/en-us/102445) steps for this one app. You do not need to turn off security for every app on the Mac.
