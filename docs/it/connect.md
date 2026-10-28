# Come collegare l’F-SCAN

Dopo **Benvenuto in F-SCANT!**, F-SCANT chiede: **Vuoi collegare il dispositivo?**

Figura 1. Prima domanda di connessione con **Sì** e **No**.

![Vuoi collegare il dispositivo? con Sì e No](../assets/images/fscant-user-guide/01-connect-question.png)

- **Sì** avvia i passaggi di connessione.
- **No** ti porta alla schermata iniziale. Puoi sempre collegarti in seguito, usando il pannello dispositivo in basso a destra.

## Collegare il dispositivo

**Needs F-SCAN**

Ti serve:

- F-SCANT, installato (vedi [Come installare F-SCANT](install.md))
- L’F-SCAN, acceso, sulla schermata iniziale
- Un cavo USB
- Il **L-CODE** dalla fattura F-SCANT

Collega il cavo USB a una porta USB del computer stesso. Non collegarlo a un hub USB (una piccola scatola che trasforma una porta in più porte) né a una docking station o a un monitor con porte USB aggiuntive. Quegli accessori spesso impediscono al computer di riconoscere l’F-SCAN.

1. Accendi l’F-SCAN e lascialo sulla schermata iniziale.
2. Collega il cavo USB come descritto sopra.
3. Fai clic sul pulsante **Connetti** nel software F-SCANT.
4. Se F-SCANT mostra **Inserisci L-CODE**, digita il codice dalla fattura e fai clic su **Invia**.

Il L-CODE si trova nella fattura dell’app F-SCANT. Se non lo trovi, contatta TB-Electronics.

Quando il pannello mostra **Connesso** insieme a un numero di serie e a una versione, hai finito. Alla prima connessione riuscita compare anche **Connessione riuscita!** prima di passare alla schermata iniziale.

Video 2. Collegare il dispositivo.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/connect-device.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 2.</strong> Collegare il dispositivo. Guarda online:
    <a href="https://fscant-docs.fscan.com/it/connect/">fscant-docs/it/connect/</a>
  </p>
</div>

Su Mac, i passaggi dettagliati del driver USB sono in [Collegare l’F-SCAN su Mac](connect-mac.md).

## Se la connessione non funziona

Prova di nuovo **Connetti** dopo aver controllato i punti sotto.

Se non succede nulla, o il pannello resta su **Connessione…**:

- Su Mac, assicurati che l’helper Silicon Labs sia installato e consentito (vedi [installazione](install.md) e [Collegare su Mac](connect-mac.md)).
- Collega il cavo al computer stesso, non a un hub, dock o monitor (vedi sopra).
- L’F-SCAN deve essere acceso, sulla schermata iniziale.

Se vedi **ERRORE: L-CODE errato. Riprova!**, il codice digitato non corrisponde a questo F-SCAN. F-SCANT verifica il codice rispetto alla fattura di quel dispositivo. Digita di nuovo il L-CODE dalla fattura. Se fallisce ancora, contatta TB-Electronics.

## Il pannello dispositivo

Il pannello dispositivo è il riquadro blu in basso a destra dello schermo. Serve a mostrarti sempre lo stato del dispositivo: connesso o disconnesso. Se è connesso, compaiono anche altre informazioni utili:

- **Dispositivo:** nome del dispositivo F-SCAN collegato
- **Numero di serie:** numero di serie dell’F-SCAN
- **Versione:** versione dell’F-SCAN
- **Timer:** se hai impostato sul dispositivo un timer dopo il quale l’F-SCAN si spegne automaticamente, viene mostrato qui. Per un uso ideale con F-SCANT, consigliamo di disattivare il timer dalle impostazioni del dispositivo.

Fai clic su **Disconnetti** quando vuoi scollegare. F-SCANT non si riconnette da solo se stacchi il cavo o spegni l’F-SCAN. Quando il dispositivo è di nuovo pronto, fai clic su **Connetti**.

Puoi espandere e ridurre il pannello con le frecce bianche “su” e “giù”.

Video 3. Espandere e ridurre il pannello dispositivo.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/bluebox-sizes.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 3.</strong> Espandere e ridurre il pannello dispositivo. Guarda online:
    <a href="https://fscant-docs.fscan.com/it/connect/">fscant-docs/it/connect/</a>
  </p>
</div>

## La schermata iniziale

La schermata iniziale offre tre opzioni: **Crea o importa DIRP**, **Carica DIRP** e **Gestisci utenti**.

Figura 2. Schermata iniziale, F-SCAN non connesso.

![Schermata iniziale, F-SCAN non connesso](../assets/images/fscant-user-guide/04-home-disconnected.png)

Figura 3. Schermata iniziale, F-SCAN connesso.

![Schermata iniziale, F-SCAN connesso](../assets/images/fscant-user-guide/05-home-connected.png)
