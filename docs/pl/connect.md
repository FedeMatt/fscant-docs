# Jak podłączyć F-SCAN

Po **Witamy w aplikacji F-SCANT!** F-SCANT pyta: **Czy chcesz podłączyć urządzenie?**

Rysunek 1. Pierwsze pytanie o połączenie z **Tak** i **Nie**.

![Czy chcesz podłączyć urządzenie? z Tak i Nie](../assets/images/fscant-user-guide/01-connect-question.png)

- **Tak** rozpoczyna kroki połączenia.
- **Nie** przenosi Cię na ekran główny. Możesz połączyć się później za pomocą panelu urządzenia w prawym dolnym rogu.

## Podłączanie urządzenia

**Needs F-SCAN**

Potrzebujesz:

- F-SCANT, zainstalowanego (zobacz [Jak zainstalować F-SCANT](install.md))
- F-SCAN włączonego, wyświetlającego ekran główny
- Kabla USB
- **F-Code** z faktury F-SCANT

Podłącz kabel USB do portu USB samego komputera. Nie podłączaj go do koncentratora USB (małego urządzenia dzielącego jeden port na kilka), stacji dokującej ani monitora z dodatkowymi portami USB. Takie akcesoria często uniemożliwiają komputerowi rozpoznanie F-SCAN.

1. Włącz F-SCAN i pozostaw go na ekranie głównym.
2. Podłącz kabel USB jak opisano powyżej.
3. Kliknij przycisk **Połącz** w oprogramowaniu F-SCANT.
4. Jeśli F-SCANT pokaże **Wprowadź F-Code**, wpisz kod z faktury i kliknij **Zatwierdź**.

F-Code znajduje się na fakturze aplikacji F-SCANT APP. Jeśli go nie znajdziesz, skontaktuj się z TB-Electronics.

Gdy panel pokazuje **Połączono** oraz numer seryjny i wersję, jesteś gotowy. Przy pierwszym udanym połączeniu pojawia się też **Połączenie powiodło się!** przed przejściem na ekran główny.

Film 2. Podłączanie urządzenia.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/connect-device.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Film 2.</strong> Podłączanie urządzenia. Obejrzyj online:
    <a href="https://fscant-docs.fscan.com/pl/connect/">fscant-docs/pl/connect/</a>
  </p>
</div>

Na Macu szczegółowe kroki sterownika USB są w [Podłączanie F-SCAN na Macu](connect-mac.md).

## Jeśli połączenie nie działa

Spróbuj ponownie **Połącz** po sprawdzeniu punktów poniżej.

Jeśli nic się nie dzieje albo panel pozostaje na **Łączenie…**:

- Na Macu upewnij się, że sterownik Silicon Labs jest zainstalowany i dozwolony (zobacz [instalację](install.md) i [Podłączanie na Macu](connect-mac.md)).
- Podłącz kabel do samego komputera, nie do hubu, doku ani monitora (jak wyżej).
- F-SCAN musi być włączony i pokazywać ekran główny.

Jeśli widzisz **BŁĄD: Wprowadzono nieprawidłowy F-Code. Spróbuj ponownie!**, wpisany kod nie pasuje do tego F-SCAN. F-SCANT weryfikuje kod na podstawie faktury tego urządzenia. Wpisz ponownie F-Code z faktury. Jeśli nadal się nie uda, skontaktuj się z TB-Electronics.

## Panel urządzenia

Panel urządzenia to niebieskie pole w prawym dolnym rogu ekranu. Zawsze pokazuje status urządzenia: połączone lub rozłączone. Gdy urządzenie jest połączone, widać dodatkowe informacje:

- **Urządzenie:** nazwa podłączonego urządzenia F-SCAN
- **Numer seryjny:** numer seryjny F-SCAN
- **Wersja:** wersja F-SCAN
- **Timer:** jeśli na urządzeniu ustawiono timer, po którym F-SCAN ma się automatycznie wyłączyć, jest on tu wyświetlany. Dla najlepszej współpracy z F-SCANT zalecamy wyłączenie timera w ustawieniach urządzenia.

Kliknij **Rozłącz**, gdy chcesz odłączyć. F-SCANT nie łączy się ponownie sam, jeśli odłączyłeś kabel lub wyłączyłeś F-SCAN. Gdy urządzenie jest znowu gotowe, kliknij **Połącz**.

Panel możesz rozwijać i zwijać białymi strzałkami „w górę” i „w dół”.

Film 3. Rozwijanie i zwijanie panelu urządzenia.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/bluebox-sizes.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Film 3.</strong> Rozwijanie i zwijanie panelu urządzenia. Obejrzyj online:
    <a href="https://fscant-docs.fscan.com/pl/connect/">fscant-docs/pl/connect/</a>
  </p>
</div>

## Ekran główny

Na ekranie głównym masz trzy opcje: **Utwórz lub importuj DIRP**, **Wczytaj DIRP** oraz **Zarządzaj użytkownikami**.

Rysunek 2. Ekran główny, F-SCAN bez połączenia.

![Ekran główny, F-SCAN bez połączenia](../assets/images/fscant-user-guide/04-home-disconnected.png)

Rysunek 3. Ekran główny, F-SCAN połączony.

![Ekran główny, F-SCAN połączony](../assets/images/fscant-user-guide/05-home-connected.png)
