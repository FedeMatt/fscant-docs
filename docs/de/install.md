# F-SCANT installieren

Die Installation unterscheidet sich etwas je nach Computer. Unter Windows erhalten Sie eine Installationsdatei. Auf einem Mac erhalten Sie die F-SCANT-App, die Sie in den Ordner Programme legen. F-SCANT wird weder im Microsoft Store noch im Mac App Store verkauft.

## Installation unter Windows

1. Doppelklicken Sie auf die erhaltene Installationsdatei (**F-SCANT-Setup-x64.exe**). Wenn Windows um Erlaubnis fragt, erlauben Sie die Installation (möglicherweise benötigen Sie ein Administratorpasswort).
2. Akzeptieren Sie die F-SCANT-Lizenz und die Silicon-Labs-Lizenz, wenn sie erscheinen. Silicon Labs stellt den kleinen USB-Helper bereit, mit dem der Computer mit dem F-SCAN kommunizieren kann. Der Installer richtet diesen Helper auf dem PC für Sie ein.
3. Öffnen Sie **F-SCANT** über das Windows-Startmenü.

Wenn Windows eine SmartScreen-Warnung anzeigt (ein blauer oder gelber Bildschirm mit dem Hinweis, dass Windows Ihren PC geschützt hat), bedeutet das, dass Windows den Herausgeber dieser Installationsdatei noch nicht kennt. Das kann vorkommen, weil Sie die Datei direkt erhalten und nicht aus dem Microsoft Store heruntergeladen haben. Wenn Sie den Installer von Ihrem Lieferanten erhalten haben, wählen Sie die Option, ihn trotzdem auszuführen.

Wenn Windows fragt, ob Apps erlaubt werden sollen, die nicht aus dem Store stammen, erlauben Sie das für diese Installation. Mit dieser Einstellung kann F-SCANT auf dem PC laufen.

## Installation auf einem Mac

1. Kopieren Sie **F-SCANT** in den Ordner Programme.
2. Installieren Sie den USB-Helper, der sich im selben Ordner wie F-SCANT befindet. Lesen Sie zuerst **SILICON-LABS-VCP-LICENSE.txt**. Öffnen Sie **Mac_OSX_VCP_Driver.zip**, öffnen Sie das Disk-Image darin und führen Sie **Install CP210x VCP Driver** aus. Dieser Helper ermöglicht dem Mac, den F-SCAN über USB zu erkennen.
3. Wenn macOS Sie auffordert, Software von Silicon Labs zuzulassen, schalten Sie diese Berechtigung ein. Nach dem Installer erlauben Sie den Treiber unter **Systemeinstellungen → Allgemein → Anmeldeobjekte & Erweiterungen**: unter **Erweiterungen** öffnen Sie **Treibererweiterungen**, schalten Sie **CP210xVCPDriver** (`com.silabs.cp210x`) ein und geben Sie bei Bedarf Ihr Mac-Passwort ein. Die vollständigen Schritte und Video 1 finden Sie unter [F-SCAN auf einem Mac verbinden](connect-mac.md).
4. Öffnen Sie **F-SCANT**.

Wenn macOS meldet, dass der Entwickler nicht verifiziert werden kann, blockiert der Mac eine App, die nicht aus dem App Store stammt. Das ist bei F-SCANT zu erwarten. Öffnen Sie sie mit den Apple-Schritten [Open Anyway](https://support.apple.com/en-us/102445) nur für diese eine App. Sie müssen die Sicherheit nicht für jede App auf dem Mac deaktivieren.
