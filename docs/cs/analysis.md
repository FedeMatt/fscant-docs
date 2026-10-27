# Jak analyzovat DIRP

## Jak načíst uložené DIRP

1. Na úvodní obrazovce klikněte na **Načíst DIRP**, nebo v horní liště na **Analýza**.
2. Vyberte uživatele a poté DIRP, které chcete analyzovat.
3. Otevře se uložený graf.

Stejný graf můžete otevřít také přes **Spravovat uživatele**, **Spravovat DIRP** a poté **Načíst DIRP**.

Pokud vidíte **Vyberte uživatele** nebo **Vyberte DIRP**, ještě nic není vybráno. Vyberte uživatele a DIRP ze seznamů a pokračujte.

Video 7. Otevření Analýzy a načtení DIRP.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/analysis-navigation.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 7.</strong> Otevření Analýzy a načtení DIRP. Sledujte online:
    <a href="https://fscant-docs.fscan.com/cs/analysis/">fscant-docs/cs/analysis/</a>
  </p>
</div>

Na grafu **Přiřadit patogeny** a **Otevřít program** používají již uloženou **Úroveň ořezu**.

## Jak číst graf

Graf je stejný jako při živém snímání:

- **CV** (Conductivity Value): osobní základní hodnota pro analyzovanou osobu. Pro užitečné výsledky by měla být mezi 5 % a 25 %.
- **MV** (Measured Value): síla odezvy frekvence. Zobrazuje se jako zelený sloupec — čím vyšší sloupec, tím silnější hodnota.
- **HITS:** sloupce nad čárou CLIP. Jsou to nejsilnější výsledky snímání.
- **ZOOM:** pomocí + graf vizuálně zvýšíte a pomocí − snížíte. Zvyšte jej, když jsou sloupce příliš malé, a snižte, když jsou příliš velké.
- **CLIP** / **Úroveň ořezu:** čára, která určuje, které sloupce se počítají jako **HITS**. Po dokončení snímání ji **AUTO** nastaví za vás. Pokud chcete více nebo méně HITS, posuňte čáru dolů nebo nahoru.

Šipky vedle čísla DIRP otevřou předchozí nebo následující uložené DIRP pro daného uživatele.

## Jak přiřadit patogeny

Přiřazení patogenů porovná vaše HITS se seznamem patogenů uloženým ve F-SCANT. U každého patogenu v seznamu zkontroluje, zda je frekvence patogenu blízko některému z vašich HITS. Pokud ano, patogen se v tabulce zobrazí jako možná shoda.

Jak blízko je „dost blízko“, nastavuje **Práh ± Hz**. Obvyklé okno je 1000 Hz. Širší okno dá více možných shod, užší méně. Okno můžete změnit na obrazovce výsledků (ne v **Nastavení**).

Pro zobrazení shod:

1. Otevřete uložené **DIRP**, nebo dokončete nové.
2. Klikněte na **Přiřadit patogeny**.
3. Prohlédněte tabulku. Změňte **Práh ± Hz**, pokud chcete širší nebo užší okno.
4. Zvolte další postup:
    - **Exportovat** uloží tabulku CSV.
    - **Otevřít databázi patogenů** umožní prohlížet celý seznam. Můžete hledat podle patogenu a řadit od A do Z nebo podle frekvence. Vybrané řádky lze přidat do tabulky analýzy tlačítkem **Přidat do analýzy**.
    - **Uložit program** vytvoří a uloží program na základě vybraných řádků.

**Upozornění:** tabulka patogenů je pouze srovnání s uloženým seznamem. Nejde o lékařskou diagnózu.

Video 8. Přiřazení patogenů a prohlížení databáze patogenů.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/pathogens.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 8.</strong> Přiřazení patogenů a prohlížení databáze patogenů. Sledujte online:
    <a href="https://fscant-docs.fscan.com/cs/analysis/">fscant-docs/cs/analysis/</a>
  </p>
</div>

## Jak otevřít a uložit program

**Program** je seznam frekvencí převzatých z **HITS** DIRP (tvar vlny, čas, wobble, obálka a amplituda). Změna programu nemění původní graf DIRP.

1. Program otevřete jedním ze dvou způsobů: po dokončení DIRP klikněte na grafu DIRP na **Otevřít program**, nebo použijte **Spravovat program** ve **Spravovat uživatele**.
2. V případě potřeby upravte řádky. Můžete měnit **Tvar vlny**, **Čas**, **Wobble**, **Obálka** a **Amplituda**. Kliknutím na **+ Nová frekvence** přidáte řádek.
3. Klikněte na **Uložit do** a zvolte, kam uložit:
    - **CSV** uloží vybrané frekvence jako tabulkový soubor.
    - **Zařízení** odešle program do F-SCAN (**Needs F-SCAN**). F-SCANT výstup sám nespustí. Až jej chcete spustit, stiskněte na F-SCAN tlačítko START.

Obrázek 8. Seznam programu s **Uložit do** **Zařízení** a **CSV**.

![Seznam programu s Uložit do Zařízení a CSV](../assets/images/fscant-user-guide/14-program-list.png)
