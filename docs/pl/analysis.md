# Jak analizować DIRP

## Jak wczytać zapisany DIRP

1. Kliknij **Wczytaj DIRP** na ekranie głównym albo **Analiza** na górnym pasku.
2. Wybierz użytkownika, a następnie DIRP do analizy.
3. Otwiera się zapisany wykres.

Ten sam wykres możesz otworzyć z **Zarządzaj użytkownikami**, **Zarządzaj DIRP**, potem **Wczytaj DIRP**.

Jeśli widzisz **Wybierz użytkownika** lub **Wybierz DIRP**, nic jeszcze nie wybrano. Wybierz użytkownika i DIRP z list, potem kontynuuj.

Film 7. Otwarcie Analizy i wczytanie DIRP.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/analysis-navigation.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Film 7.</strong> Otwarcie Analizy i wczytanie DIRP. Obejrzyj online:
    <a href="https://fscant-docs.fscan.com/pl/analysis/">fscant-docs/pl/analysis/</a>
  </p>
</div>

Na wykresie **Dopasuj patogeny** i **Otwórz program** korzystają z już zapisanego poziomu przycinania.

## Jak czytać wykres

Wykres jest taki sam jak podczas skanu na żywo:

- **CV** (Conductivity Value): osobista wartość bazowa osoby analizowanej. Dla użytecznych wyników powinna wynosić od 5% do 25%.
- **MV** (Measured Value): jak silnie zarejestrowała się częstotliwość. Widać ją jako zielony słupek — im wyższy, tym silniejszy odczyt.
- **HITS:** słupki powyżej linii CLIP. To najsilniejsze wyniki skanu.
- **ZOOM:** użyj +, aby wykres był wyższy, i −, aby był niższy. Podnieś go, gdy słupki są za małe, obniż, gdy są za duże.
- **CLIP** / **Poziom przycinania:** linia decydująca, które słupki liczą się jako **HITS**. Po zakończeniu skanu **AUTO** ustawia ją za Ciebie. Jeśli chcesz więcej lub mniej HITS, przesuń linię w dół lub w górę.

Strzałki obok numeru DIRP otwierają poprzedni lub następny zapisany DIRP tego użytkownika.

## Jak dopasować patogeny

**Dopasuj patogeny** porównuje Twoje HITS z listą patogenów zapisaną w F-SCANT. Dla każdego patogenu na liście sprawdza, czy jego częstotliwość jest bliska któremuś z Twoich HITS. Jeśli tak, patogen pojawia się w tabeli jako możliwe dopasowanie.

**Próg ± Hz** określa, jak blisko muszą być częstotliwości, żeby uznać je za dopasowanie. Typowe okno to 1000 Hz. Szersze okno daje więcej możliwych dopasowań, węższe — mniej. Okno możesz zmienić na ekranie wyników (nie w **Ustawienia**).

Aby zobaczyć dopasowania:

1. Otwórz zapisany **DIRP** albo dokończ nowy.
2. Kliknij **Dopasuj patogeny**.
3. Przeczytaj tabelę. Zmień **Próg ± Hz**, jeśli chcesz szersze lub węższe okno.
4. Wybierz, co dalej:
    - **Eksportuj** zapisuje arkusz CSV.
    - **Otwórz bazę patogenów** pozwala przeglądać pełną listę. Możesz szukać po patogenie, sortować od A do Z lub według częstotliwości. Zaznaczone wiersze można dodać do tabeli analizy przyciskiem **Dodaj do analizy**.
    - **Zapisz program** tworzy i zapisuje program na podstawie zaznaczonych wierszy.

**Uwaga:** tabela patogenów to tylko porównanie z zapisaną listą. Nie jest diagnozą medyczną.

Film 8. Dopasowanie patogenów i przeglądanie bazy patogenów.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/pathogens.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Film 8.</strong> Dopasowanie patogenów i przeglądanie bazy patogenów. Obejrzyj online:
    <a href="https://fscant-docs.fscan.com/pl/analysis/">fscant-docs/pl/analysis/</a>
  </p>
</div>

## Jak otworzyć i zapisać program

**Program** to lista częstotliwości wzięta z **HITS** DIRP (przebieg, czas, Wobble, obwiednia i amplituda). Zmiana programu nie zmienia oryginalnego wykresu DIRP.

1. Otwórz program na jeden z dwóch sposobów: kliknij **Otwórz program** na wykresie DIRP po zakończeniu DIRP albo użyj **Zarządzaj programem** w **Zarządzaj użytkownikami**.
2. W razie potrzeby edytuj wiersze. Możesz zmienić Przebieg, Czas, Wobble, Obwiednię i Amplitudę. Kliknij **+ Nowa częstotliwość**, aby dodać wiersz.
3. Kliknij **Zapisz do** i wybierz miejsce zapisu:
    - **CSV** zapisuje wybrane częstotliwości jako plik arkusza.
    - **Urządzenie** wysyła program na F-SCAN (**Needs F-SCAN**). F-SCANT nie uruchamia programu na urządzeniu. Naciśnij START na F-SCAN, gdy chcesz go uruchomić.

Rysunek 8. Lista programu z **Zapisz do** **Urządzenie** i **CSV**.

![Lista programu z Zapisz do Urządzenie i CSV](../assets/images/fscant-user-guide/14-program-list.png)
