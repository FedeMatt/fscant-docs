# Collegare l’F-SCAN su Mac

Hai già F-SCANT. Questi passaggi installano il driver USB incluso e collegano l’F-SCAN. Lo stesso file driver si usa su Mac Intel e su Mac Apple Silicon. Non devi scegliere un processore né scaricare un driver dal web.

Ti serve:

- F-SCANT
- L’F-SCAN, acceso e sulla schermata iniziale
- Un cavo USB (collegato al Mac, oppure a un hub o a una dock)
- Il L-CODE dalla fattura F-SCANT o inviato via email dal tuo rivenditore.

## 1. Installa il driver incluso con F-SCANT

Nella cartella fornita con F-SCANT, leggi **SILICON-LABS-VCP-LICENSE.txt** prima di continuare. Poi apri **Mac_OSX_VCP_Driver.zip**, apri **SiLabsUSBDriverDisk.dmg** e fai doppio clic su **Install CP210x VCP Driver**.

L’installer può chiedere la password del Mac. Si tratta di Silicon Labs CP210x VCP 6.0.3. Silicon Labs lo indica come adatto a Mac OS X 10.11 e successivi. F-SCANT è stato verificato con questo driver su un Mac Intel con macOS 15. Quella verifica non copre ogni macOS più vecchio o più nuovo.

Figura 4. La cartella F-SCANT con l’installer Silicon Labs accanto all’app.

![La cartella F-SCANT con l’installer Silicon Labs accanto all’app](../assets/images/connect-the-f-scan-on-mac/01-installer-with-app.png)

Figura 5. L’installer Silicon Labs.

![L’installer Silicon Labs](../assets/images/connect-the-f-scan-on-mac/02-silabs-installer.png)

## 2. Consenti l’estensione Silicon Labs

macOS chiede comunque di consentire il driver dopo che l’installer termina. Sul Mac dove questo è stato verificato di recente:

1. Apri **Impostazioni di Sistema → Generali → Elementi di login ed estensioni**.
2. Sotto **Estensioni**, apri **Estensioni driver** (elenca `com.silabs.cp210x`).
3. Attiva **CP210xVCPDriver**. Digita la password del Mac se richiesta, poi fai clic su **Fine**.

Un macOS più recente può usare un nome leggermente diverso per quel pannello. Usa il video qui sotto.

Su quel Mac non è servito un riavvio.

Video 1. Abilitare il driver Silicon Labs su Mac.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/driver-extension-mac-intel.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 1.</strong> Abilitare il driver Silicon Labs su Mac. Guarda online:
    <a href="https://fscant-docs.fscan.com/it/connect-mac/">fscant-docs/it/connect-mac/</a>
  </p>
</div>

Se macOS mostra anche un pulsante separato per consentire software di sistema da Silicon Labs, consentilo.

## 3. Collega l’F-SCAN

Accendi l’F-SCAN e lascialo sulla schermata iniziale. Assicurati nel menu SETUP del dispositivo che AUTO POWER OFF sia disattivato. Collega il cavo USB al Mac o tramite un hub o una dock.

## 4. Connetti in F-SCANT

Apri **F-SCANT**. Se macOS dice che lo sviluppatore non può essere verificato, usa i passaggi Apple per aprire comunque quell’app: [Open Anyway](https://support.apple.com/en-us/102445). Non disattivare il controllo di sicurezza per tutte le app.

Fai clic su **Connetti**. Se F-SCANT chiede un L-CODE, inserisci il codice dalla fattura F-SCANT o dall’email inviata dal tuo rivenditore. Quando il pannello dice **Connesso** e mostra un numero di serie e una versione, hai finito. Il flusso di connessione è anche nel [Video 2 di Come collegare l’F-SCAN](connect.md).

## Se Connetti non riesce

Controlla questi punti prima di riprovare:

- L’estensione Silicon Labs è attiva.
- Il cavo è collegato al Mac, o a un hub o una dock.
- L’F-SCAN è acceso e sulla schermata iniziale.
- Il L-CODE corrisponde alla fattura.

Un L-CODE errato mostra **ERRORE: L-CODE errato. Riprova!**
