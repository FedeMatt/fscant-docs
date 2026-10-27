# Jak vytvořit nebo importovat DIRP

**Needs F-SCAN**

DIRP znamená Dual Integration Resonance Procedure a jde v podstatě o snímání v rozsahu frekvencí. F-SCAN postupně vysílá jednotlivé frekvence a F-SCANT vykreslí graf odpovědí.

Snímání probíhá od nižší frekvence (**Fmin**) po vyšší frekvenci (**Fmax**) v krocích **Delta F**.

Po kliknutí na **Vytvořit nebo importovat DIRP** na úvodní obrazovce, nebo na **DIRP** v horní liště nabídky, můžete zvolit, jak začít:

- **Spustit nové DIRP:** spustí nové DIRP ve F-SCANT
- **Importovat DIRP ze zařízení:** importuje DIRP, které už je na zařízení F-SCAN

Obrázek 6. Spuštění DIRP: **Spustit nové DIRP** nebo **Importovat DIRP ze zařízení**.

![Spuštění DIRP: Spustit nové DIRP nebo Importovat DIRP ze zařízení](../assets/images/fscant-user-guide/06-dirp-start.png)

## Spuštění nového DIRP

1. Vyberte uživatele a klikněte na **Pokračovat**.
2. Vyberte frekvenční rozsah a pokračujte.
3. Na grafu DIRP klikněte na **Spustit**.

### Výběr uživatele

**Vybrat uživatele** zobrazí osoby již uložené ve F-SCANT. Klikněte na jméno, nebo klikněte na **Nový uživatel** pro přidání někoho nového, a poté na **Pokračovat**.

Video 4. Vytvoření nového uživatele a spuštění DIRP.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/new-user-dirp.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 4.</strong> Vytvoření nového uživatele a spuštění DIRP. Sledujte online:
    <a href="https://fscant-docs.fscan.com/cs/dirp/">fscant-docs/cs/dirp/</a>
  </p>
</div>

### Výběr frekvenčního rozsahu

Obrazovka rozsahu nabízí:

- **Vybrat naposledy použité:** poslední **Fmin**, **Fmax** a **Delta F**, které jste použili ve F-SCANT (poprvé je to 300 kHz až 450 kHz v krocích 150 Hz)
- **nebo vyberte možnost:** připravené rozsahy **CLARK**, **RIFE**, **DIRP 290k**, **DIRP 390k**, **DIRP 490k**
- **Vlastní:** zadejte vlastní **Fmin**, **Fmax** a **Delta F**

**Fmin** je začátek snímání. **Fmax** je jeho konec. **Delta F** je rozestup mezi jednou frekvencí a další. Pole **Režim DIRP** u daného rozsahu zobrazuje **AUTO** nebo **FAST**.

Poznámka: **Fmin** musí být nižší než **Fmax**. **Fmin** lze nastavit od 50 Hz, **Fmax** až do 2 MHz a **Delta F** od 1 Hz do 10 000 Hz. Pokud je hodnota mimo tyto rozsahy, F-SCANT zobrazí chybu. Pro pokračování číslo opravte.

Obrázek 7. Frekvenční rozsah: naposledy použité hodnoty, předvolby a **Vlastní**.

![Frekvenční rozsah: naposledy použité hodnoty, předvolby a Vlastní](../assets/images/fscant-user-guide/08-dirp-range.png)

Video 5. Volba vlastního frekvenčního rozsahu.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/custom-frequencies-selection.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 5.</strong> Volba vlastního frekvenčního rozsahu. Sledujte online:
    <a href="https://fscant-docs.fscan.com/cs/dirp/">fscant-docs/cs/dirp/</a>
  </p>
</div>

### Před spuštěním DIRP

Připravte F-SCAN na DIRP podle návodu k zařízení (senzor na výstupu uvedeném na zařízení, osoba připojená). F-SCANT spustí snímání a uloží graf. Nenahrazuje nastavení senzoru na zařízení.

### Průběh DIRP

Jakmile máte zařízení připravené, klikněte na **Spustit.**

Graf zobrazí snímání od **Fmin** do **Fmax**, přičemž:

- Zelené sloupce jsou odpovědi na jednotlivých frekvencích (**MV** je výška každého sloupce).
- Fialová čára je úroveň ořezu (**Clip**). Sloupce nad touto čárou se počítají jako **HITS**.
- **CV** je základní hodnota pro danou osobu.
- Funkce **ZOOM** (− / +) sloupce vizuálně zvýší nebo sníží pro snazší čtení. Nemění počet **HITS**.

Počkejte, až graf dosáhne **Fmax** a stav zobrazí **Dokončeno**. DIRP se automaticky uloží ve F-SCANT i na zařízení.

Video 6. Průběh živého DIRP.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/live-dirp.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 6.</strong> Průběh živého DIRP. Sledujte online:
    <a href="https://fscant-docs.fscan.com/cs/dirp/">fscant-docs/cs/dirp/</a>
  </p>
</div>

Pokud chcete jinou sadu **HITS**, můžete přesunout úroveň ořezu zadáním hodnoty mezi 0 a 100 v nastavení DIRP v šedém rámečku vpravo od grafu. Při práci ve F-SCANT používejte k ručnímu posunu úrovně ořezu pouze software (ne zařízení F-SCAN). **Uložit DIRP** se zobrazí, když se úroveň ořezu liší od již uložené.

Pokud snímání zastavíte dříve, než dosáhne Fmax, zobrazí se dotaz, zda opravdu chcete zastavit. Předčasné zastavení znamená neúplné snímání a F-SCANT nemůže uložit částečné výsledky. Zastavujte tedy jen tehdy, když jste ochotni toto DIRP zahodit. Pokud jej chcete zachovat, zvolte **Zůstat** a snímání pokračuje.

Pokud během probíhajícího DIRP přes horní lištu nabídky přejdete jinam, dostanete stejnou volbu. **Zůstat** vás nechá na grafu. **Zastavit** nebo **Opustit** snímání ukončí.
