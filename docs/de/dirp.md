# DIRP erstellen oder importieren

**Needs F-SCAN**

DIRP steht für Dual Integration Resonance Procedure und ist im Wesentlichen ein Scan über einen Frequenzbereich. Der F-SCAN sendet nacheinander jede Frequenz, und F-SCANT zeichnet die Antworten in einem Diagramm auf.

Der Scan läuft von einer unteren Frequenz (**Fmin**) bis zu einer oberen Frequenz (**Fmax**), in Schritten von **Delta F**.

Nachdem Sie auf dem Startbildschirm auf **DIRP erstellen oder importieren** oder in der Menüleiste oben auf **DIRP** geklickt haben, können Sie wählen, wie Sie beginnen möchten:

- **Neues DIRP jetzt starten:** ein neues DIRP von F-SCANT aus durchführen
- **DIRP vom Gerät importieren:** ein DIRP importieren, das bereits auf Ihrem F-SCAN-Gerät gespeichert ist

Abbildung 6. DIRP-Start: **Neues DIRP jetzt starten** oder **DIRP vom Gerät importieren**.

![DIRP-Start: Neues DIRP jetzt starten oder DIRP vom Gerät importieren](../assets/images/fscant-user-guide/06-dirp-start.png)

## Ein neues DIRP starten

1. Wählen Sie einen Benutzer und klicken Sie dann auf **Weiter**.
2. Wählen Sie einen Frequenzbereich und fahren Sie fort.
3. Klicken Sie im DIRP-Diagramm auf **Start**.

### Benutzer auswählen

**Benutzer auswählen** listet die Personen, die bereits in F-SCANT gespeichert sind. Klicken Sie auf einen Namen, oder klicken Sie auf **Neuer Benutzer**, um jemanden hinzuzufügen, und dann auf **Weiter**.

Video 4. Neuen Benutzer anlegen und dann ein DIRP starten.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/new-user-dirp.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 4.</strong> Neuen Benutzer anlegen und dann ein DIRP starten. Online ansehen:
    <a href="https://fscant-docs.fscan.com/de/dirp/">fscant-docs/de/dirp/</a>
  </p>
</div>

### Frequenzbereich auswählen

Der Bereichsbildschirm bietet:

- **Zuletzt verwendete Werte:** die letzten **Fmin**-, **Fmax**- und **Delta F**-Werte, die Sie in F-SCANT verwendet haben (beim ersten Mal sind das 300 kHz bis 450 kHz, in Schritten von 150 Hz)
- **oder eine Option wählen:** vorgefertigte Bereiche **CLARK**, **RIFE**, **DIRP 290k**, **DIRP 390k**, **DIRP 490k**
- **Benutzerdefiniert:** eigene Werte für **Fmin**, **Fmax** und **Delta F** eingeben

**Fmin** ist der Start des Scans. **Fmax** ist das Ende. **Delta F** ist der Abstand zwischen einer Frequenz und der nächsten. Das Feld **DIRP-Modus** zeigt **AUTO** oder **FAST** für diesen Bereich.

Hinweis: **Fmin** muss kleiner als **Fmax** sein. Sie können **Fmin** ab 50 Hz, **Fmax** bis 2 MHz und **Delta F** von 1 Hz bis 10 000 Hz einstellen. Liegt ein Wert außerhalb dieser Bereiche, zeigt F-SCANT einen Fehler. Bitte korrigieren Sie die Zahl, um fortzufahren.

Abbildung 7. Frequenzbereich: zuletzt verwendete Werte, Voreinstellungen und **Benutzerdefiniert**.

![Frequenzbereich: zuletzt verwendete Werte, Voreinstellungen und Benutzerdefiniert](../assets/images/fscant-user-guide/08-dirp-range.png)

Video 5. Einen benutzerdefinierten Frequenzbereich wählen.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/custom-frequencies-selection.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 5.</strong> Einen benutzerdefinierten Frequenzbereich wählen. Online ansehen:
    <a href="https://fscant-docs.fscan.com/de/dirp/">fscant-docs/de/dirp/</a>
  </p>
</div>

### Vor dem Start des DIRP

Richten Sie den F-SCAN für ein DIRP wie in der Gerätebedienungsanleitung ein (Sensor am angezeigten Geräteausgang, Person angeschlossen). F-SCANT startet den Scan und speichert das Diagramm. Es ersetzt nicht die Sensor-Einrichtung am Gerät.

### Ein DIRP durchführen

Nachdem Sie Ihr Gerät eingerichtet haben, klicken Sie auf **Start.**

Das Diagramm zeigt den Scan von **Fmin** bis **Fmax**, wobei:

- Grüne Balken die Antworten bei jeder Frequenz sind (**MV** ist die Höhe jedes Balkens).
- Die lilafarbene Linie das Clipping-Level ist (**Clip**). Balken oberhalb dieser Linie zählen als **HITS**.
- **CV** ein Hintergrundwert für die Person ist.
- Die Zoomfunktion (− / +) die Balken höher oder niedriger darstellt, damit sie leichter lesbar sind. Sie ändert nicht, wie viele **HITS** es gibt.

Warten Sie, bis das Diagramm **Fmax** erreicht und der Status **Abgeschlossen** anzeigt. Das DIRP wird automatisch sowohl in F-SCANT als auch auf Ihrem Gerät gespeichert.

Video 6. Live-DIRP durchführen.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/live-dirp.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 6.</strong> Live-DIRP durchführen. Online ansehen:
    <a href="https://fscant-docs.fscan.com/de/dirp/">fscant-docs/de/dirp/</a>
  </p>
</div>

Wenn Sie eine andere Anzahl von **HITS** möchten, können Sie das Clipping-Level verschieben, indem Sie in den DIRP-Einstellungen im grauen Kasten rechts neben dem Diagramm einen Wert zwischen 0 und 100 eingeben. Bei der Nutzung von F-SCANT verschieben Sie das Clipping-Level bitte nur in der Software (nicht am F-SCAN-Gerät). **DIRP speichern** erscheint, wenn das Clipping-Level vom bereits gespeicherten Wert abweicht.

Wenn Sie den Scan stoppen, bevor Fmax erreicht ist, erscheint eine Meldung mit der Frage, ob Sie wirklich stoppen möchten. Ein vorzeitiger Stopp bedeutet, dass der Scan unvollständig ist, und F-SCANT kann Teilergebnisse nicht speichern. Stoppen Sie daher nur, wenn Sie dieses DIRP verwerfen möchten. Wenn Sie es behalten möchten, wählen Sie **Bleiben**, und der Scan läuft weiter.

Wenn Sie über die obere Menüleiste zu einem anderen Menü wechseln, während ein DIRP noch läuft, erhalten Sie dieselbe Wahl. **Bleiben** lässt Sie beim Diagramm. **Stopp** oder **Verlassen** beendet den Scan.
