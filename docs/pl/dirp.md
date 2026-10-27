# Jak utworzyć lub zaimportować DIRP

**Needs F-SCAN**

DIRP oznacza Dual Integration Resonance Procedure i w praktyce jest skanem w zakresie częstotliwości. F-SCAN wysyła kolejno każdą częstotliwość, a F-SCANT rysuje wykres odpowiedzi.

Skan przebiega od dolnej częstotliwości (**Fmin**) do górnej (**Fmax**), w krokach **Delta F**.

Po kliknięciu **Utwórz lub importuj DIRP** na ekranie głównym albo **DIRP** na pasku menu u góry ekranu możesz wybrać sposób rozpoczęcia:

- **Uruchom nowy DIRP:** uruchamia nowy DIRP z F-SCANT
- **Importuj DIRP z urządzenia:** importuje DIRP, który już jest na urządzeniu F-SCAN

Rysunek 6. Start DIRP: **Uruchom nowy DIRP** lub **Importuj DIRP z urządzenia**.

![Start DIRP: Uruchom nowy DIRP lub Importuj DIRP z urządzenia](../assets/images/fscant-user-guide/06-dirp-start.png)

## Uruchamianie nowego DIRP

1. Wybierz użytkownika, potem kliknij **Kontynuuj**.
2. Wybierz zakres częstotliwości, potem kontynuuj.
3. Kliknij **Start** na wykresie DIRP.

### Wybór użytkownika

**Wybierz użytkownika** pokazuje osoby już zapisane w F-SCANT. Kliknij nazwę albo **Nowy użytkownik**, aby kogoś dodać, potem **Kontynuuj**.

Film 4. Tworzenie nowego użytkownika, potem start DIRP.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/new-user-dirp.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Film 4.</strong> Tworzenie nowego użytkownika, potem start DIRP. Obejrzyj online:
    <a href="https://fscant-docs.fscan.com/pl/dirp/">fscant-docs/pl/dirp/</a>
  </p>
</div>

### Wybór zakresu częstotliwości

Ekran zakresu oferuje:

- **Wybierz ostatnie wartości:** ostatnie **Fmin**, **Fmax** i **Delta F** użyte w F-SCANT (za pierwszym razem: od 300 kHz do 450 kHz, w krokach 150 Hz)
- **lub wybierz opcję:** gotowe zakresy **CLARK**, **RIFE**, **DIRP 290k**, **DIRP 390k**, **DIRP 490k**
- **Niestandardowy:** wpisz własne **Fmin**, **Fmax** i **Delta F**

**Fmin** to początek skanu. **Fmax** to koniec. **Delta F** to odstęp między kolejnymi częstotliwościami. Pole **Tryb DIRP** pokazuje **AUTO** lub **FAST** dla tego zakresu.

Uwaga: **Fmin** musi być niższe niż **Fmax**. Możesz ustawić **Fmin** od 50 Hz, **Fmax** do 2 MHz, a **Delta F** od 1 Hz do 10 000 Hz. Jeśli wartość jest poza tymi zakresami, F-SCANT pokaże błąd. Popraw liczbę, aby kontynuować.

Rysunek 7. Zakres częstotliwości: ostatnie wartości, ustawienia wstępne i **Niestandardowy**.

![Zakres częstotliwości: ostatnie wartości, ustawienia wstępne i Niestandardowy](../assets/images/fscant-user-guide/08-dirp-range.png)

Film 5. Wybór niestandardowego zakresu częstotliwości.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/custom-frequencies-selection.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Film 5.</strong> Wybór niestandardowego zakresu częstotliwości. Obejrzyj online:
    <a href="https://fscant-docs.fscan.com/pl/dirp/">fscant-docs/pl/dirp/</a>
  </p>
</div>

### Przed uruchomieniem DIRP

Przygotuj F-SCAN do DIRP zgodnie z instrukcją urządzenia (czujnik na wyjściu wskazanym na urządzeniu, osoba podłączona). F-SCANT uruchamia skan i zapisuje wykres. Nie zastępuje przygotowania czujnika na urządzeniu.

### Przebieg DIRP

Gdy urządzenie jest przygotowane, kliknij **Start**.

Wykres pokazuje skan od **Fmin** do **Fmax**:

- Zielone słupki to odpowiedzi przy każdej częstotliwości (**MV** to wysokość każdego słupka).
- Liliowa linia to poziom przycinania (**Clip**). Słupki powyżej tej linii liczą się jako **HITS**.
- **CV** to odczyt tła dla osoby.
- Funkcja powiększenia (− / +) sprawia, że słupki wyglądają na wyższe lub niższe, co ułatwia odczyt. Nie zmienia liczby **HITS**.

Poczekaj, aż wykres dojdzie do **Fmax** i status pokaże **Zakończono**. DIRP zostanie automatycznie zapisany zarówno w F-SCANT, jak i na urządzeniu.

Film 6. Przebieg DIRP na żywo.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/live-dirp.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Film 6.</strong> Przebieg DIRP na żywo. Obejrzyj online:
    <a href="https://fscant-docs.fscan.com/pl/dirp/">fscant-docs/pl/dirp/</a>
  </p>
</div>

Jeśli chcesz inny zestaw **HITS**, możesz przesunąć poziom przycinania, wpisując wartość od 0 do 100 w ustawieniach DIRP w szarym polu po prawej stronie wykresu. Podczas pracy z F-SCANT przesuwaj poziom przycinania wyłącznie w programie (nie na urządzeniu F-SCAN). **Zapisz DIRP** pojawia się, gdy poziom przycinania różni się od już zapisanego.

Jeśli zatrzymasz skan przed osiągnięciem Fmax, komunikat pyta, czy naprawdę chcesz zatrzymać. Wczesne zatrzymanie oznacza niekompletny skan, a F-SCANT nie może zapisać wyników częściowych. Zatrzymuj więc tylko wtedy, gdy chcesz odrzucić ten DIRP. Jeśli wolisz go zachować, wybierz **Zostań** — skan będzie kontynuowany.

Jeśli przełączysz się na inne menu z górnego paska, gdy DIRP nadal działa, dostaniesz ten sam wybór. **Zostań** zostawia Cię na wykresie. **Zatrzymaj** lub **Opuść** kończą skan.
