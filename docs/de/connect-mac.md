# F-SCAN auf einem Mac verbinden

Sie haben bereits F-SCANT. Mit diesen Schritten installieren Sie den mitgelieferten USB-Treiber und verbinden den F-SCAN. Dieselbe Treiberdatei wird auf einem Intel-Mac und einem Apple-Silicon-Mac verwendet. Sie wählen keinen Prozessor und laden keinen Treiber aus dem Web herunter.

Sie benötigen:

- F-SCANT
- Den F-SCAN, eingeschaltet und mit angezeigtem Startbildschirm
- Ein USB-Kabel (am Mac oder über einen Hub bzw. ein Dock)
- Den L-CODE von Ihrer F-SCANT-Rechnung

## 1. Den mit F-SCANT gelieferten Treiber installieren

Lesen Sie im Ordner, der mit F-SCANT geliefert wurde, zuerst **SILICON-LABS-VCP-LICENSE.txt**. Öffnen Sie dann **Mac_OSX_VCP_Driver.zip**, öffnen Sie **SiLabsUSBDriverDisk.dmg** und doppelklicken Sie auf **Install CP210x VCP Driver**.

Der Installer kann nach Ihrem Mac-Passwort fragen. Es handelt sich um Silicon Labs CP210x VCP 6.0.3. Silicon Labs gibt an, dass er für Mac OS X 10.11 und neuer ist. F-SCANT wurde mit diesem Treiber auf einem Intel-Mac mit macOS 15 geprüft. Diese Prüfung deckt nicht jedes ältere oder neuere macOS ab.

Abbildung 4. Der F-SCANT-Ordner mit dem Silicon-Labs-Installer neben der App.

![Der F-SCANT-Ordner mit dem Silicon-Labs-Installer neben der App](../assets/images/connect-the-f-scan-on-mac/01-installer-with-app.png)

Abbildung 5. Der Silicon-Labs-Installer.

![Der Silicon-Labs-Installer](../assets/images/connect-the-f-scan-on-mac/02-silabs-installer.png)

## 2. Die Silicon-Labs-Erweiterung zulassen

macOS fordert Sie nach dem Installer weiterhin auf, den Treiber zuzulassen. Auf dem Mac, mit dem dies zuletzt geprüft wurde:

1. Öffnen Sie **Systemeinstellungen → Allgemein → Anmeldeobjekte & Erweiterungen**.
2. Unter **Erweiterungen** öffnen Sie **Treibererweiterungen** (dort steht `com.silabs.cp210x`).
3. Schalten Sie **CP210xVCPDriver** ein. Geben Sie bei Bedarf Ihr Mac-Passwort ein und klicken Sie dann auf **Fertig**.

Ein neueres macOS kann für dieses Fenster einen etwas anderen Namen verwenden. Nutzen Sie das Video unten.

Auf diesem Mac war kein Neustart erforderlich.

Video 1. Silicon-Labs-Treiber auf einem Mac aktivieren.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/driver-extension-mac-intel.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 1.</strong> Silicon-Labs-Treiber auf einem Mac aktivieren. Online ansehen:
    <a href="https://fscant-docs.fscan.com/de/connect-mac/">fscant-docs/de/connect-mac/</a>
  </p>
</div>

Wenn macOS zusätzlich eine separate Schaltfläche anzeigt, um Systemsoftware von Silicon Labs zuzulassen, lassen Sie sie zu.

## 3. F-SCAN anschließen

Schalten Sie den F-SCAN ein und lassen Sie ihn auf dem Startbildschirm. Stecken Sie das USB-Kabel in den Mac oder über einen Hub bzw. ein Dock.

## 4. In F-SCANT verbinden

Öffnen Sie **F-SCANT**. Wenn macOS meldet, dass der Entwickler nicht verifiziert werden kann, folgen Sie den Apple-Schritten, um diese App trotzdem zu öffnen: [Open Anyway](https://support.apple.com/en-us/102445). Deaktivieren Sie die Sicherheitsprüfung nicht für jede App.

Klicken Sie auf **Verbinden**. Wenn F-SCANT nach einem L-CODE fragt, geben Sie den Code von Ihrer F-SCANT-Rechnung ein. Wenn das Fenster **Verbunden** anzeigt und eine Seriennummer sowie eine Version zeigt, sind Sie fertig. Der Verbindungsablauf ist auch in [Video 2 unter F-SCAN verbinden](connect.md) zu sehen.

## Wenn Verbinden nicht gelingt

Prüfen Sie Folgendes, bevor Sie es erneut versuchen:

- Die Silicon-Labs-Erweiterung ist eingeschaltet.
- Das Kabel steckt im Mac oder in einem Hub bzw. Dock.
- Der F-SCAN ist eingeschaltet und zeigt den Startbildschirm.
- Der L-CODE stimmt mit der Rechnung überein.

Ein falscher L-CODE zeigt **FEHLER: Falscher L-CODE. Bitte erneut versuchen!**
