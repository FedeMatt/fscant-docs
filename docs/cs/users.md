# Jak spravovat uživatele

**Uživatel** ve F-SCANT je osoba, pro kterou uchováváte výsledky DIRP. Nejde o přihlášení ani heslo.

**Spravovat uživatele** zobrazí všechny osoby uložené ve F-SCANT se sloupci **Jméno**, **DIRPs**, **Paměť**, **Datum** a **Čas**. Otevřením řádku zobrazíte DIRP a program dané osoby.

Obrázek 9. **Spravovat uživatele**, jeden řádek rozbalený.

![Tabulka Spravovat uživatele s jedním rozbaleným řádkem](../assets/images/fscant-user-guide/15-manage-users.png)

## Přidávání a hledání uživatelů

- **Přidat nového uživatele:** zadejte jméno a klikněte na **Přidat**.
- **Hledat:** zadejte jméno a potvrďte hledání ovládacím prvkem. Seznam se při psaní nefiltruje; hledání je potřeba potvrdit.

Osobu můžete přidat také přes **Nový uživatel** při spuštění DIRP.

Pokud vidíte **Pacient s tímto jménem již existuje.**, toto jméno už je v seznamu. F-SCANT nemůže uložit dva uživatele pod stejným jménem, proto zvolte jiné jméno, například přidáním prostředního iniciálu nebo čísla.

## Přejmenování nebo smazání uživatele

Vyberte uživatele a klikněte na **Spravovat uživatele**.

- **Upravit jméno:** zadejte nové jméno.
- **Smazat uživatele:** Při mazání uživatele F-SCANT požádá o potvrzení. Smazání znamená, že osoba i všechna její DIRP a programy budou z F-SCANT odstraněny a tuto akci nelze vzít zpět. Pokud jste si jisti, klikněte na **SMAZAT?**.

## Správa DIRP nebo programu uživatele

Na otevřeném řádku uživatele:

**Spravovat DIRP**

- **Načíst DIRP:** otevře graf DIRP (viz [Jak analyzovat DIRP](analysis.md)).
- **Analyzovat patogeny:** otevře přiřazení patogenů pro dané DIRP.
- **Odebrat DIRP u tohoto uživatele:** smaže toto DIRP z F-SCANT pro daného uživatele.
- **Změnit umístění v paměti:** nastaví číslo paměti od 1 do 100 pro tohoto uživatele.

**Spravovat program**

- **Otevřít program:** otevře seznam frekvencí.
- **Odebrat program u tohoto uživatele:** smaže program (nikoli však odpovídající DIRP).
- **Změnit umístění v paměti:** nastaví číslo paměti od 1 do 100.

Pro odeslání DIRP nebo programu do zařízení použijte **Přenést DIRP do zařízení** nebo **Uložit do** **Zařízení** (viz [vytvořit nebo importovat DIRP](dirp.md) a [analyzovat DIRP](analysis.md)).

## Porovnání dvou DIRP

1. Otevřete **Spravovat uživatele**.
2. Vyberte dvě DIRP.
3. Klikněte na **Porovnat DIRPs**.

Pokud se po kliknutí na **Porovnat DIRPs** nic nestane, zkontrolujte, že jsou vybrána právě *dvě* DIRP.

Porovnání se otevře jako graf. **Přepnout na program** a **Přepnout na DIRP** změní zobrazení. **Exportovat** uloží obě DIRP společně do jednoho souboru **CSV**.

Video 9. Porovnání dvou DIRP.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/dirp-comparison.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 9.</strong> Porovnání dvou DIRP. Sledujte online:
    <a href="https://fscant-docs.fscan.com/cs/users/">fscant-docs/cs/users/</a>
  </p>
</div>

## Změna umístění v paměti

Každý uživatel může mít ve F-SCANT čísla paměti 1 až 100. Tato čísla pomáhají DIRP znovu najít. Nejde o složky v počítači.

1. Klikněte na **Změnit umístění v paměti**.
2. Zvolte číslo od 1 do 100.
3. Pokud se F-SCANT zeptá **NAHRADIT?** a uvede, že v tomto umístění už něco je, toto číslo je u daného uživatele už použité. Klikněte na **Nahradit** pro přepsání stávající položky, nebo na **Zrušit** pro zachování staré položky a výběr jiného čísla.
