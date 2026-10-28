# DIRP analysieren

## Einen gespeicherten DIRP laden

1. Klicken Sie auf dem Startbildschirm auf **DIRP laden** oder in der oberen Leiste auf **Analyse**.
2. Wählen Sie den Benutzer und dann den DIRP, den Sie analysieren möchten.
3. Das gespeicherte Diagramm öffnet sich.

Sie können dasselbe Diagramm auch über **Benutzer verwalten**, **DIRP verwalten** und dann **DIRP laden** öffnen.

Wenn Sie **Bitte einen Benutzer wählen** oder **Bitte ein DIRP wählen** sehen, ist noch nichts ausgewählt. Wählen Sie einen Benutzer und einen DIRP aus den Listen und fahren Sie fort.

Video 7. Analyse öffnen und einen DIRP laden.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/analysis-navigation.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 7.</strong> Analyse öffnen und einen DIRP laden. Online ansehen:
    <a href="https://fscant-docs.fscan.com/de/analysis/">fscant-docs/de/analysis/</a>
  </p>
</div>

Im Diagramm nutzen **Pathogene abgleichen** und **Programm öffnen** das bereits gespeicherte Clipping-Level.

## Das Diagramm lesen

Das Diagramm ist dasselbe wie bei einem Live-Scan:

- **CV** (Conductivity Value): ein persönlicher Basiswert für die analysierte Person. Für aussagekräftige Ergebnisse sollte er zwischen 5 % und 25 % liegen.
- **MV** (Measured Value): wie stark eine Frequenz registriert wurde. Sie erscheint als grüner Balken; je höher der Balken, desto stärker die Messung.
- **HITS:** die Balken oberhalb der CLIP-Linie. Das sind die stärksten Ergebnisse des Scans.
- **ZOOM:** mit + vergrößern Sie das Diagramm und mit − verkleinern Sie es. Vergrößern Sie es, wenn die Balken zu klein sind, und verkleinern Sie es, wenn sie zu groß sind.
- **CLIP** / **Clipping-Level:** die Linie, die entscheidet, welche Balken als **HITS** zählen. Nach dem Scan setzt **AUTO** sie für Sie. Wenn Sie mehr oder weniger HITS möchten, verschieben Sie die Linie nach unten oder oben.

Die Pfeile neben der DIRP-Nummer öffnen den vorherigen oder nächsten gespeicherten DIRP für diesen Benutzer.

## Pathogene abgleichen

Pathogene abgleichen vergleicht Ihre HITS mit der in F-SCANT gespeicherten Pathogenliste. Für jedes Pathogen auf der Liste wird geprüft, ob dessen Frequenz nahe an einem Ihrer HITS liegt. Wenn ja, erscheint das Pathogen in der Tabelle als mögliche Übereinstimmung.

Was als „nah genug“ gilt, legen Sie mit **Schwelle ± Hz** fest. Das übliche Fenster beträgt 1000 Hz. Ein breiteres Fenster ergibt mehr mögliche Übereinstimmungen, ein engeres weniger. Sie können das Fenster auf dem Ergebnisbildschirm ändern (nicht unter **Einstellungen**).

So sehen Sie die Übereinstimmungen:

1. Öffnen Sie einen gespeicherten **DIRP**, oder schließen Sie einen neuen ab.
2. Klicken Sie auf **Pathogene abgleichen**.
3. Lesen Sie die Tabelle. Ändern Sie **Schwelle ± Hz**, wenn Sie ein breiteres oder engeres Fenster möchten.
4. Wählen Sie, was als Nächstes geschehen soll:
    - **Exportieren** speichert eine CSV-Tabelle.
    - **Erregerdatenbank öffnen** ermöglicht Ihnen, die vollständige Liste durchzusuchen. Sie können nach Pathogen suchen und von A bis Z oder nach Frequenz sortieren. Ausgewählte Zeilen können Sie mit der Schaltfläche **Zur Analyse hinzufügen** zur Analysetabelle hinzufügen.
    - **Programm speichern** erstellt und speichert ein Programm auf Basis der ausgewählten Zeilen.

**Bitte beachten Sie:** Die Pathogentabelle ist nur ein Vergleich mit der gespeicherten Liste. Sie ist keine medizinische Diagnose.

Video 8. Pathogene abgleichen und die Erregerdatenbank durchsuchen.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/pathogens.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 8.</strong> Pathogene abgleichen und die Erregerdatenbank durchsuchen. Online ansehen:
    <a href="https://fscant-docs.fscan.com/de/analysis/">fscant-docs/de/analysis/</a>
  </p>
</div>

## Ein Programm öffnen und speichern

Ein **Programm** ist die Frequenzliste aus den **HITS** eines DIRP (Wellenform, Zeit, Wobble, Hüllkurve und Amplitude). Das Ändern eines Programms ändert nicht das ursprüngliche DIRP-Diagramm.

1. Öffnen Sie das Programm auf eine von zwei Arten: Klicken Sie nach Abschluss des DIRP im DIRP-Diagramm auf **Programm öffnen**, oder verwenden Sie **Programm verwalten** unter **Benutzer verwalten**.
2. Bearbeiten Sie die Zeilen bei Bedarf. Sie können Wellenform, Zeit, Wobble, Hüllkurve und Amplitude ändern. Klicken Sie auf **+ Neue Frequenz**, um eine Zeile hinzuzufügen.
3. Klicken Sie auf **Speichern auf** und wählen Sie den Speicherort:
    - **CSV** speichert die ausgewählten Frequenzen als Tabellendatei.
    - **Gerät** sendet das Programm an den F-SCAN (**Needs F-SCAN**). F-SCANT startet die Ausgabe nicht. Drücken Sie START am F-SCAN, wenn Sie es ausführen möchten.

Abbildung 8. Programmliste mit **Speichern auf** **Gerät** und **CSV**.

![Programmliste mit Speichern auf Gerät und CSV](../assets/images/fscant-user-guide/14-program-list.png)
