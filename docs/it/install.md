# Come installare F-SCANT

L’installazione varia un po’ a seconda del computer. Su Windows ricevi un file di installazione. Su Mac ricevi l’app F-SCANT, da copiare nella cartella Applicazioni. F-SCANT non è venduto nel Microsoft Store né nel Mac App Store.

## Come installare su Windows

1. Fai doppio clic sull’installer ricevuto (**F-SCANT-Setup-x64.exe**). Se Windows chiede l’autorizzazione, concedila (potrebbe servire una password di amministratore).
2. Accetta la licenza F-SCANT e la licenza Silicon Labs quando compaiono. Silicon Labs produce il piccolo helper USB che permette al computer di comunicare con l’F-SCAN. L’installer lo installa sul PC per te.
3. Apri **F-SCANT** dal menu Start di Windows.

Se Windows mostra un avviso SmartScreen (una schermata blu o gialla che dice che Windows ha protetto il PC), significa che Windows non riconosce ancora l’editore di questo installer. Può succedere perché hai ricevuto il file direttamente, non dal Microsoft Store. Se hai ricevuto l’installer dal tuo fornitore, scegli l’opzione per eseguirlo comunque.

Se Windows chiede di consentire app non provenienti dallo Store, consentilo per questa installazione. Quella impostazione permette a F-SCANT di funzionare sul PC.

## Come installare su Mac

1. Copia **F-SCANT** nella cartella Applicazioni.
2. Installa l’helper USB incluso nella stessa cartella di F-SCANT. Leggi prima **SILICON-LABS-VCP-LICENSE.txt**. Apri **Mac_OSX_VCP_Driver.zip**, apri l’immagine disco al suo interno ed esegui **Install CP210x VCP Driver**. Questo helper permette al Mac di vedere l’F-SCAN via USB.
3. Quando macOS chiede di consentire il software di Silicon Labs, attiva quell’autorizzazione. Dopo l’installer, consenti il driver in **Impostazioni di Sistema → Generali → Elementi di login ed estensioni**: sotto **Estensioni**, apri **Estensioni driver**, attiva **CP210xVCPDriver** (`com.silabs.cp210x`) e digita la password del Mac se richiesta. I passaggi completi e il Video 1 sono in [Collegare l’F-SCAN su Mac](connect-mac.md).
4. Apri **F-SCANT**.

Se macOS dice che lo sviluppatore non può essere verificato, significa che il Mac sta bloccando un’app che non proviene dall’App Store. Per F-SCANT è normale. Aprila con i passaggi Apple [Open Anyway](https://support.apple.com/en-us/102445) solo per questa app. Non serve disattivare la sicurezza per tutte le app sul Mac.
