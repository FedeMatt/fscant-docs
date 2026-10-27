# Benutzer verwalten

Ein **Benutzer** in F-SCANT ist eine Person, für die Sie DIRP-Ergebnisse speichern. Es ist weder ein Login noch ein Passwort.

**Benutzer verwalten** listet alle in F-SCANT gespeicherten Personen mit **Name**, **DIRPs**, **Speicher**, **Datum** und **Zeit**. Öffnen Sie eine Zeile, um die DIRPs und das Programm dieser Person zu sehen.

Abbildung 9. **Benutzer verwalten**, eine Zeile aufgeklappt.

![Tabelle Benutzer verwalten mit einer aufgeklappten Zeile](../assets/images/fscant-user-guide/15-manage-users.png)

## Benutzer hinzufügen und finden

- **Neuen Benutzer hinzufügen:** Geben Sie einen Namen ein und klicken Sie auf **Hinzufügen**.
- **Suche:** Geben Sie einen Namen ein und bestätigen Sie die Suche. Die Liste filtert nicht während der Eingabe; Sie müssen die Suche bestätigen.

Sie können eine Person auch mit **Neuer Benutzer** hinzufügen, wenn Sie ein DIRP starten.

Wenn Sie **Ein Patient mit diesem Namen existiert bereits.** sehen, ist dieser Name bereits in Ihrer Liste. F-SCANT kann nicht zwei Benutzer unter demselben Namen speichern; wählen Sie daher einen anderen Namen, zum Beispiel mit einem mittleren Initial oder einer Zahl.

## Benutzer umbenennen oder löschen

Wählen Sie einen Benutzer und klicken Sie auf **Benutzer verwalten**.

- **Name bearbeiten:** Geben Sie den neuen Namen ein.
- **Benutzer löschen:** Wenn Sie einen Benutzer löschen, fragt F-SCANT nach einer Bestätigung. Löschen bedeutet, dass die Person und alle ihre DIRPs und Programme aus F-SCANT entfernt werden; das lässt sich nicht rückgängig machen. Wenn Sie sicher sind, klicken Sie auf **LÖSCHEN?**.

## DIRP oder Programm eines Benutzers verwalten

In einer geöffneten Benutzerzeile:

**DIRP verwalten**

- **DIRP laden:** öffnet das DIRP-Diagramm (siehe [DIRP analysieren](analysis.md)).
- **Pathogene analysieren:** öffnet den Pathogenabgleich für dieses DIRP.
- **DIRP von diesem Benutzer entfernen:** löscht dieses DIRP in F-SCANT für diesen Benutzer.
- **Speicherort ändern:** setzt eine Speichernummer von 1 bis 100 für diesen Benutzer.

**Programm verwalten**

- **Programm öffnen:** öffnet die Frequenzliste.
- **Programm von diesem Benutzer entfernen:** löscht das Programm (aber nicht das zugehörige DIRP).
- **Speicherort ändern:** setzt eine Speichernummer von 1 bis 100.

Um ein DIRP oder ein Programm an das Gerät zu senden, verwenden Sie **DIRP auf Gerät übertragen** oder **Speichern auf** **Gerät** (siehe [DIRP erstellen oder importieren](dirp.md) und [DIRP analysieren](analysis.md)).

## Zwei DIRPs vergleichen

1. Öffnen Sie **Benutzer verwalten**.
2. Wählen Sie zwei DIRPs aus.
3. Klicken Sie auf **DIRPs vergleichen**.

Wenn beim Klicken auf **DIRPs vergleichen** nichts passiert, prüfen Sie, ob genau *zwei* DIRPs ausgewählt sind.

Der Vergleich öffnet sich als Diagramm. **Zur Program wechseln** und **Zur DIRP wechseln** ändern die Anzeige. **Exportieren** speichert beide DIRPs zusammen in einer **CSV**-Tabelle.

Video 9. Zwei DIRPs vergleichen.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/dirp-comparison.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 9.</strong> Zwei DIRPs vergleichen. Online ansehen:
    <a href="https://fscant-docs.fscan.com/de/users/">fscant-docs/de/users/</a>
  </p>
</div>

## Einen Speicherort ändern

Jeder Benutzer kann in F-SCANT Speichernummern von 1 bis 100 haben. Diese Nummern helfen Ihnen, ein DIRP wiederzufinden. Sie entsprechen nicht Ordnern auf Ihrem Computer.

1. Klicken Sie auf **Speicherort ändern**.
2. Wählen Sie eine Nummer von 1 bis 100.
3. Wenn F-SCANT **ERSETZEN?** fragt und meldet, dass an diesem Speicherort bereits etwas gespeichert ist, ist diese Nummer für diesen Benutzer bereits belegt. Klicken Sie auf **Ersetzen**, um den vorhandenen Eintrag zu überschreiben, oder auf **Abbrechen**, um den alten Eintrag zu behalten und eine andere Nummer zu wählen.
