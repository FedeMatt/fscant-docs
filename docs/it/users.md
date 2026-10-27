# Come gestire gli utenti

Un **utente** in F-SCANT è una persona per cui conservi risultati DIRP. Non è un login né una password.

**Gestisci utenti** elenca tutti gli utenti memorizzati in F-SCANT, con **Nome**, **DIRPs**, **Memoria**, **Data** e **Ora**. Apri una riga per vedere i DIRP e il programma di quella persona.

Figura 9. **Gestisci utenti**, una riga espansa.

![Tabella Gestisci utenti con una riga espansa](../assets/images/fscant-user-guide/15-manage-users.png)

## Aggiungere e trovare utenti

- **Aggiungi nuovo utente:** digita un nome e fai clic su **Aggiungi**.
- **Cerca:** digita un nome e conferma con il controllo di ricerca. L’elenco non si filtra mentre digiti; devi confermare la ricerca.

Puoi anche aggiungere una persona con **Nuovo utente** quando avvii un DIRP.

Se vedi **Esiste già un paziente con questo nome.**, quel nome è già nell’elenco. F-SCANT non può salvare due utenti con lo stesso nome: scegli un nome diverso, ad esempio aggiungendo un’iniziale o un numero.

## Rinominare o eliminare un utente

Seleziona un utente e fai clic su **Gestisci utente**.

- **Modifica nome:** digita il nuovo nome.
- **Elimina utente:** Quando elimini un utente, F-SCANT chiede conferma. Eliminare significa che la persona e tutti i suoi DIRP e programmi verranno rimossi da F-SCANT, e l’operazione non si può annullare. Se sei sicuro, fai clic su **ELIMINARE**.

## Gestire DIRP o programma di un utente

Su una riga utente aperta:

**Gestisci DIRP**

- **Carica DIRP:** apre il grafico DIRP (vedi [Come analizzare un DIRP](analysis.md)).
- **Analizza patogeni:** apre l’abbinamento patogeni per quel DIRP.
- **Rimuovi DIRP da questo utente:** elimina quel DIRP da F-SCANT per questo utente.
- **Cambia posizione di memoria:** imposta un numero di memoria da 1 a 100 per questo utente.

**Gestisci programma**

- **Apri programma:** apre l’elenco frequenze.
- **Rimuovi programma da questo utente:** elimina il programma (ma non il DIRP corrispondente).
- **Cambia posizione di memoria:** imposta un numero di memoria da 1 a 100.

Per inviare un DIRP o un programma al dispositivo, usa **Trasferisci DIRP al dispositivo** oppure **Salva su** **Dispositivo** (vedi [creare o importare un DIRP](dirp.md) e [analizzare un DIRP](analysis.md)).

## Confrontare due DIRP

1. Apri **Gestisci utenti**.
2. Seleziona due DIRP.
3. Fai clic su **Confronta DIRPs**.

Se non succede nulla quando fai clic su **Confronta DIRPs**, verifica che siano selezionati esattamente *due* DIRP.

Il confronto si apre come grafico. **Passa a programma** e **Passa a DIRP** cambiano la visualizzazione. **Esporta** salva entrambi i DIRP insieme in un foglio **CSV**.

Video 9. Confrontare due DIRP.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/fscant-docs/assets/videos/dirp-comparison.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 9.</strong> Confrontare due DIRP. Guarda online:
    <a href="https://FedeMatt.github.io/fscant-docs/it/users/">fscant-docs/it/users/</a>
  </p>
</div>

## Cambiare una posizione di memoria

Ogni utente può avere numeri di memoria da 1 a 100 in F-SCANT. Questi numeri aiutano a ritrovare un DIRP. Non sono le stesse cose delle cartelle sul computer.

1. Fai clic su **Cambia posizione di memoria**.
2. Scegli un numero da 1 a 100.
3. Se F-SCANT chiede **SOSTITUIRE?** e indica che in questa posizione di memoria c’è già qualcosa, quel numero è già usato per questo utente. Fai clic su **Sostituisci** per sovrascrivere ciò che c’è, oppure **Annulla** per tenere l’elemento precedente e scegliere un altro numero.
