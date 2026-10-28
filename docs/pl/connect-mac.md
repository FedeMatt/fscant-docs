# Podłączanie F-SCAN na Macu

Masz już F-SCANT. Te kroki instalują dołączony sterownik USB i podłączają F-SCAN. Ten sam plik sterownika działa na Macu Intel i na Macu Apple Silicon. Nie wybierasz procesora i nie pobierasz sterownika z internetu.

Potrzebujesz:

- F-SCANT
- F-SCAN włączonego, wyświetlającego ekran główny
- Kabla USB (do Maca — bezpośrednio albo przez hub lub dok)
- L-Code z faktury F-SCANT

## 1. Zainstaluj sterownik dołączony do F-SCANT

W folderze dostarczonym z F-SCANT przeczytaj **SILICON-LABS-VCP-LICENSE.txt** przed kontynuacją. Następnie otwórz **Mac_OSX_VCP_Driver.zip**, otwórz **SiLabsUSBDriverDisk.dmg** i kliknij dwukrotnie **Install CP210x VCP Driver**.

Instalator może poprosić o hasło Maca. To Silicon Labs CP210x VCP 6.0.3. Według Silicon Labs sterownik działa z Mac OS X 10.11 i nowszymi. F-SCANT sprawdzono z tym sterownikiem na Macu Intel z macOS 15. Ta weryfikacja nie obejmuje każdej starszej ani nowszej wersji macOS.

Rysunek 4. Folder F-SCANT z instalatorem Silicon Labs obok aplikacji.

![Folder F-SCANT z instalatorem Silicon Labs obok aplikacji](../assets/images/connect-the-f-scan-on-mac/01-installer-with-app.png)

Rysunek 5. Instalator Silicon Labs.

![Instalator Silicon Labs](../assets/images/connect-the-f-scan-on-mac/02-silabs-installer.png)

## 2. Zezwól na rozszerzenie Silicon Labs

macOS i tak prosi o zezwolenie na sterownik po zakończeniu instalatora. Na Macu, na którym to ostatnio sprawdzano:

1. Otwórz **Ustawienia systemowe → Ogólne → Elementy logowania i rozszerzenia**.
2. W **Rozszerzenia** otwórz **Rozszerzenia sterowników** (jest tam `com.silabs.cp210x`).
3. Włącz **CP210xVCPDriver**. W razie potrzeby wpisz hasło Maca, potem kliknij **Gotowe**.

Nowszy macOS może używać nieco innej nazwy tego panelu. Skorzystaj z filmu poniżej.

Na tym Macu restart nie był potrzebny.

Film 1. Włączanie sterownika Silicon Labs na Macu.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/driver-extension-mac-intel.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Film 1.</strong> Włączanie sterownika Silicon Labs na Macu. Obejrzyj online:
    <a href="https://fscant-docs.fscan.com/pl/connect-mac/">fscant-docs/pl/connect-mac/</a>
  </p>
</div>

Jeśli macOS pokaże osobny przycisk zezwolenia na oprogramowanie systemowe od Silicon Labs, zezwól.

## 3. Podłącz F-SCAN

Włącz F-SCAN i pozostaw go na ekranie głównym. Podłącz kabel USB do Maca — bezpośrednio albo przez hub lub dok.

## 4. Połącz w F-SCANT

Otwórz **F-SCANT**. Jeśli macOS zgłosi, że deweloper nie może zostać zweryfikowany, skorzystaj z kroków Apple, aby mimo to otworzyć tę aplikację: [Open Anyway](https://support.apple.com/en-us/102445). Nie wyłączaj kontroli bezpieczeństwa dla wszystkich aplikacji.

Kliknij **Połącz**. Jeśli F-SCANT poprosi o L-Code, wpisz kod z faktury F-SCANT. Gdy panel pokazuje **Połączono** oraz numer seryjny i wersję, jesteś gotowy. Przebieg połączenia jest też pokazany w [Filmie 2 w Jak podłączyć F-SCAN](connect.md).

## Jeśli **Połącz** nie działa

Sprawdź to przed ponowną próbą:

- Rozszerzenie Silicon Labs jest włączone.
- Kabel jest podłączony do Maca albo do hubu lub doku.
- F-SCAN jest włączony i pokazuje ekran główny.
- L-Code zgadza się z fakturą.

Błędny L-Code pokazuje **BŁĄD: Wprowadzono nieprawidłowy L-Code. Spróbuj ponownie!**
