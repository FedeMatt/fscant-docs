# Jak zarządzać użytkownikami

**Użytkownik** w F-SCANT to osoba, dla której przechowujesz wyniki DIRP. To nie jest login ani hasło.

**Zarządzaj użytkownikami** pokazuje wszystkich zapisanych w F-SCANT, z kolumnami **Nazwa**, **DIRPs**, **Pamięć**, **Data** i **Czas**. Otwórz wiersz, aby zobaczyć DIRP i program tej osoby.

Rysunek 9. **Zarządzaj użytkownikami**, jeden wiersz rozwinięty.

![Tabela Zarządzaj użytkownikami z jednym rozwiniętym wierszem](../assets/images/fscant-user-guide/15-manage-users.png)

## Dodawanie i wyszukiwanie użytkowników

- **Dodaj nowego użytkownika:** wpisz nazwę i kliknij **Dodaj**.
- **Szukaj:** wpisz nazwę i potwierdź kontrolką wyszukiwania. Lista nie filtruje się w trakcie pisania — trzeba potwierdzić wyszukiwanie.

Możesz też dodać osobę przez **Nowy użytkownik**, gdy uruchamiasz DIRP.

Jeśli widzisz **Pacjent o tej nazwie już istnieje.**, ta nazwa jest już na liście. F-SCANT nie może zapisać dwóch użytkowników pod tą samą nazwą, więc wybierz inną — na przykład dodając inicjał lub numer.

## Zmiana nazwy lub usuwanie użytkownika

Wybierz użytkownika i kliknij **Zarządzaj użytkownikiem**.

- **Edytuj nazwę:** wpisz nową nazwę.
- **Usuń użytkownika:** Gdy usuwasz użytkownika, F-SCANT prosi o potwierdzenie. Usunięcie oznacza, że osoba oraz wszystkie jej DIRP i programy zostaną usunięte z F-SCANT i nie da się tego cofnąć. Jeśli jesteś pewien, kliknij **USUNĄĆ?**.

## Zarządzanie DIRP lub programem użytkownika

Na otwartym wierszu użytkownika:

**Zarządzaj DIRP**

- **Wczytaj DIRP:** otwiera wykres DIRP (zobacz [Jak analizować DIRP](analysis.md)).
- **Analizuj patogeny:** otwiera dopasowanie patogenów dla tego DIRP.
- **Usuń DIRP u tego użytkownika:** usuwa ten DIRP z F-SCANT dla tego użytkownika.
- **Zmień lokalizację pamięci:** ustawia numer pamięci od 1 do 100 dla tego użytkownika.

**Zarządzaj programem**

- **Otwórz program:** otwiera listę częstotliwości.
- **Usuń program u tego użytkownika:** usuwa program (ale nie odpowiadający mu DIRP).
- **Zmień lokalizację pamięci:** ustawia numer pamięci od 1 do 100.

Aby wysłać DIRP lub program na urządzenie, użyj **Prześlij DIRP na urządzenie** albo **Zapisz do** **Urządzenie** (zobacz [Jak utworzyć lub zaimportować DIRP](dirp.md) oraz [Jak analizować DIRP](analysis.md)).

## Porównywanie dwóch DIRP

1. Otwórz **Zarządzaj użytkownikami**.
2. Zaznacz dwa DIRP.
3. Kliknij **Porównaj DIRPs**.

Jeśli po kliknięciu **Porównaj DIRPs** nic się nie dzieje, sprawdź, czy zaznaczone są dokładnie *dwa* DIRP.

Porównanie otwiera się jako wykres. **Przełącz na program** i **Przełącz na DIRP** zmieniają widok. **Eksportuj** zapisuje oba DIRP razem w jednym arkuszu **CSV**.

Film 9. Porównanie dwóch DIRP.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/dirp-comparison.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Film 9.</strong> Porównanie dwóch DIRP. Obejrzyj online:
    <a href="https://fscant-docs.fscan.com/pl/users/">fscant-docs/pl/users/</a>
  </p>
</div>

## Zmiana lokalizacji pamięci

Każdy użytkownik może mieć numery pamięci od 1 do 100 w F-SCANT. Te numery pomagają ponownie znaleźć DIRP. Nie są tym samym co foldery na komputerze.

1. Kliknij **Zmień lokalizację pamięci**.
2. Wybierz numer od 1 do 100.
3. Jeśli F-SCANT pyta **ZASTĄPIĆ?** i informuje, że w tej lokalizacji pamięci coś już jest, ten numer jest już używany dla tego użytkownika. Kliknij **Zastąp**, aby nadpisać zawartość, albo **Anuluj**, aby zachować poprzedni element i wybrać inny numer.
