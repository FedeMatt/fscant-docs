# F-SCAN verbinden

Nach **Willkommen bei F-SCANT!** fragt F-SCANT: **Möchten Sie Ihr Gerät verbinden?**

Abbildung 1. Erste Verbindungsfrage mit **Ja** und **Nein**.

![Möchten Sie Ihr Gerät verbinden? mit Ja und Nein](../assets/images/fscant-user-guide/01-connect-question.png)

- **Ja** startet die Verbindungsschritte.
- **Nein** führt Sie zum Startbildschirm. Später können Sie jederzeit über das Gerätefenster unten rechts verbinden.

## Gerät verbinden

**Needs F-SCAN**

Sie benötigen:

- F-SCANT, installiert (siehe [F-SCANT installieren](install.md))
- Den F-SCAN, eingeschaltet und mit angezeigtem Startbildschirm
- Ein USB-Kabel
- Den **L-CODE** von Ihrer F-SCANT-Rechnung

Stecken Sie das USB-Kabel in einen USB-Anschluss am Computer selbst. Stecken Sie es nicht in einen USB-Hub (eine kleine Box, die einen Anschluss in mehrere umwandelt) und auch nicht in eine Dockingstation oder einen Monitor mit zusätzlichen USB-Anschlüssen. Solche Zusätze verhindern oft, dass der Computer den F-SCAN erkennt.

1. Schalten Sie den F-SCAN ein und lassen Sie ihn auf dem Startbildschirm.
2. Stecken Sie das USB-Kabel wie oben beschrieben ein.
3. Klicken Sie in der F-SCANT-Software auf die Schaltfläche **Verbinden**.
4. Wenn F-SCANT **L-CODE eingeben** anzeigt, geben Sie den Code von der Rechnung ein und klicken Sie auf **Absenden**.

Der L-CODE steht auf der F-SCANT-Rechnung. Wenn Sie ihn nicht finden, kontaktieren Sie bitte TB-Electronics.

Wenn das Fenster **Verbunden** sowie eine Seriennummer und eine Version anzeigt, sind Sie fertig. Bei der ersten erfolgreichen Verbindung erscheint außerdem **Verbindung erfolgreich!**, bevor Sie zum Startbildschirm gelangen.

Video 2. Gerät verbinden.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/connect-device.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 2.</strong> Gerät verbinden. Online ansehen:
    <a href="https://fscant-docs.fscan.com/de/connect/">fscant-docs/de/connect/</a>
  </p>
</div>

Auf einem Mac finden Sie detaillierte USB-Treiberschritte unter [F-SCAN auf einem Mac verbinden](connect-mac.md).

## Wenn die Verbindung nicht funktioniert

Versuchen Sie **Verbinden** erneut, nachdem Sie die Punkte unten geprüft haben.

Wenn nichts passiert oder das Fenster bei **Verbindung wird hergestellt…** bleibt:

- Auf einem Mac stellen Sie sicher, dass der Silicon-Labs-Helper installiert und zugelassen ist (siehe [Installation](install.md) und [Auf einem Mac verbinden](connect-mac.md)).
- Stecken Sie das Kabel in den Computer selbst, nicht in einen Hub, ein Dock oder einen Monitor (siehe oben).
- Der F-SCAN muss eingeschaltet sein und den Startbildschirm anzeigen.

Wenn Sie **FEHLER: Falscher L-CODE. Bitte erneut versuchen!** sehen, stimmt der eingegebene Code nicht mit diesem F-SCAN überein. F-SCANT prüft den Code anhand der Rechnung für dieses Gerät. Geben Sie den L-CODE erneut von der Rechnung ein. Wenn es weiterhin fehlschlägt, kontaktieren Sie bitte TB-Electronics.

## Das Gerätefenster

Das Gerätefenster ist der blaue Kasten unten rechts auf dem Bildschirm. Es zeigt Ihnen jederzeit den Status Ihres Geräts an — verbunden oder getrennt. Ist das Gerät verbunden, erscheinen weitere relevante Informationen:

- **Gerät:** Name des verbundenen F-SCAN-Geräts
- **Seriennummer:** Seriennummer des F-SCAN
- **Version:** Version des F-SCAN
- **Timer:** Wenn Sie am Gerät einen Timer eingestellt haben, nach dem sich Ihr F-SCAN automatisch ausschalten soll, wird er hier angezeigt. Für die ideale Nutzung mit F-SCANT empfehlen wir, den Timer in den Geräteeinstellungen auszuschalten.

Klicken Sie auf **Trennen**, wenn Sie das Gerät abstecken möchten. F-SCANT verbindet sich nicht von selbst erneut, wenn Sie das Kabel abgezogen oder den F-SCAN ausgeschaltet haben. Wenn das Gerät wieder bereit ist, klicken Sie auf **Verbinden**.

Sie können das Fenster mit den weißen Pfeilen „hoch“ und „runter“ erweitern und einklappen.

Video 3. Gerätefenster erweitern und einklappen.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/bluebox-sizes.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 3.</strong> Gerätefenster erweitern und einklappen. Online ansehen:
    <a href="https://fscant-docs.fscan.com/de/connect/">fscant-docs/de/connect/</a>
  </p>
</div>

## Der Startbildschirm

Der Startbildschirm bietet drei Optionen: **DIRP erstellen oder importieren**, **DIRP laden** und **Benutzer verwalten**.

Abbildung 2. Startbildschirm, F-SCAN nicht verbunden.

![Startbildschirm, F-SCAN nicht verbunden](../assets/images/fscant-user-guide/04-home-disconnected.png)

Abbildung 3. Startbildschirm, F-SCAN verbunden.

![Startbildschirm, F-SCAN verbunden](../assets/images/fscant-user-guide/05-home-connected.png)
