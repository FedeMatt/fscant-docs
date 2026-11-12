# Come analizzare un DIRP

## Come caricare un DIRP salvato

1. Fai clic su **Carica DIRP** nella schermata iniziale, oppure su **Analisi** nella barra in alto.
2. Seleziona l’utente e poi il DIRP da analizzare.
3. Si apre il grafico salvato.

Puoi aprire lo stesso grafico da **Gestisci utenti**, **Gestisci DIRP**, poi **Carica DIRP**.

Se vedi **Seleziona un utente** o **Seleziona un DIRP**, non hai ancora selezionato nulla. Scegli un utente e un DIRP dagli elenchi, poi continua.

Video 7. Aprire Analisi e caricare un DIRP.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/analysis-navigation.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 7.</strong> Aprire Analisi e caricare un DIRP. Guarda online:
    <a href="https://fscant-docs.fscan.com/it/analysis/">fscant-docs/it/analysis/</a>
  </p>
</div>

Sul grafico, **Confronta con il catalogo** e **Apri programma** usano il livello di clipping già salvato.

## Come leggere il grafico

Il grafico è lo stesso di una scansione in tempo reale:

- **CV** (Conductivity Value): un valore di riferimento personale per l’utente analizzato. Per risultati utili dovrebbe essere tra 5% e 25%.
- **MV** (Measured Value): quanto è forte la risposta a una frequenza. Compare come barra verde: più è alta, più è forte la lettura.
- **HITS:** le barre sopra la linea CLIP. Sono i risultati più forti della scansione.
- **ZOOM:** usa + per rendere il grafico più alto e − per renderlo più basso. Alzalo quando le barre sono troppo piccole, abbassalo quando sono troppo grandi.
- **CLIP** / **Livello di clipping:** la linea che decide quali barre contano come **HITS**. A fine scansione, **AUTO** la posiziona per te. Se vuoi più o meno HITS, sposta la linea in basso o in alto.

Le frecce accanto al numero DIRP aprono il DIRP salvato precedente o successivo di quell’utente.

## Come confrontare gli HITS con il catalogo frequenze

**Confronta con il catalogo** confronta i tuoi HITS con il catalogo frequenze memorizzato in F-SCANT. Per ogni voce del catalogo, verifica se la sua frequenza rientra nell’intervallo di corrispondenza di uno dei tuoi HITS. Se è così, la voce compare nella tabella come corrispondenza nel catalogo.

Quanto deve essere “abbastanza vicino” lo definisce **Intervallo di corrispondenza ± Hz**. Di solito l’intervallo è di 1000 Hz. Un intervallo più ampio produce più corrispondenze; uno più stretto ne produce meno. Puoi cambiare l’intervallo nella schermata dei risultati (non in **Impostazioni**).

Per vedere le corrispondenze:

1. Apri un **DIRP** salvato, oppure terminane uno nuovo.
2. Fai clic su **Confronta con il catalogo**.
3. Leggi la tabella. Modifica **Intervallo di corrispondenza ± Hz** se vuoi un intervallo più ampio o più stretto.
4. Scegli cosa fare dopo:
    - **Esporta** salva un foglio CSV.
    - **Apri catalogo frequenze** permette di sfogliare l’intero catalogo. Puoi cercare per nome, ordinare dalla A alla Z o per frequenza. Le righe selezionate si possono aggiungere alla tabella di analisi con il pulsante **Aggiungi all’analisi**.
    - **Salva programma** crea e memorizza un programma basato sulle righe selezionate.

**Nota:** la tabella dei risultati elenca solo le voci del catalogo la cui frequenza è vicina ai tuoi HITS. Non è una diagnosi medica.

Video 8. Confrontare gli HITS con il catalogo e sfogliare il catalogo frequenze.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/pathogens.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 8.</strong> Confrontare gli HITS con il catalogo e sfogliare il catalogo frequenze. Guarda online:
    <a href="https://fscant-docs.fscan.com/it/analysis/">fscant-docs/it/analysis/</a>
  </p>
</div>

## Come aprire e salvare un programma

Un **programma** è l’elenco di frequenze ricavato dagli **HITS** di un DIRP (forma d’onda, tempo, wobble, inviluppo e ampiezza). Modificare un programma non modifica il grafico DIRP originale.

1. Apri il programma in uno di due modi: fai clic su **Apri programma** sul grafico DIRP dopo che il DIRP è completato, oppure usa **Gestisci programma** in **Gestisci utenti**.
2. Modifica le righe se serve. Puoi cambiare Forma d’onda, Tempo, Wobble, Inviluppo e Ampiezza. Fai clic su **+ Nuova frequenza** per aggiungere una riga.
3. Fai clic su **Salva su** e scegli dove salvarlo:
    - **CSV** salva le frequenze selezionate come foglio di calcolo.
    - **Dispositivo** invia il programma all’F-SCAN (**Needs F-SCAN**). F-SCANT non avvia l’uscita. Premi START sull’F-SCAN quando vuoi eseguirlo.

Figura 8. Elenco programmi con **Salva su** **Dispositivo** e **CSV**.

![Elenco programmi con Salva su Dispositivo e CSV](../assets/images/fscant-user-guide/14-program-list.png)
