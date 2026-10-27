# Jak zainstalować F-SCANT

Instalacja nieco się różni w zależności od komputera. Na Windowsie otrzymujesz plik instalatora. Na Macu otrzymujesz aplikację F-SCANT, którą umieszczasz w folderze Aplikacje. F-SCANT nie jest sprzedawany w Microsoft Store ani w Mac App Store.

## Jak zainstalować w systemie Windows

1. Kliknij dwukrotnie otrzymany instalator (**F-SCANT-Setup-x64.exe**). Jeśli Windows poprosi o uprawnienia, zezwól (może być potrzebne hasło administratora).
2. Zaakceptuj licencję F-SCANT oraz licencję Silicon Labs, gdy się pojawią. Silicon Labs dostarcza mały sterownik USB, dzięki któremu komputer komunikuje się z F-SCAN. Instalator umieszcza go na PC za Ciebie.
3. Otwórz **F-SCANT** z menu Start Windows.

Jeśli Windows pokaże ostrzeżenie SmartScreen (niebieski lub żółty ekran z komunikatem, że Windows ochronił komputer), oznacza to, że Windows nie zna jeszcze wydawcy tego instalatora. Może się tak stać, bo plik otrzymałeś bezpośrednio, a nie z Microsoft Store. Jeśli instalator pochodzi od dostawcy, uruchom go mimo to.

Jeśli Windows poprosi o zezwolenie na aplikacje spoza sklepu, zezwól na tę instalację. Dzięki temu ustawieniu F-SCANT może działać na PC.

## Jak zainstalować na Macu

1. Skopiuj **F-SCANT** do folderu Aplikacje.
2. Zainstaluj sterownik USB dołączony w tym samym folderze co F-SCANT. Najpierw przeczytaj **SILICON-LABS-VCP-LICENSE.txt**. Otwórz **Mac_OSX_VCP_Driver.zip**, otwórz obraz dysku wewnątrz i uruchom **Install CP210x VCP Driver**. Ten sterownik pozwala Macowi zobaczyć F-SCAN przez USB.
3. Gdy macOS poprosi o zezwolenie na oprogramowanie Silicon Labs, włącz to uprawnienie. Po zakończeniu instalatora zezwól na sterownik w **Ustawienia systemowe → Ogólne → Elementy logowania i rozszerzenia**: w **Rozszerzenia** otwórz **Rozszerzenia sterowników**, włącz **CP210xVCPDriver** (`com.silabs.cp210x`) i w razie potrzeby wpisz hasło Maca. Pełne kroki oraz Film 1 znajdziesz w [Podłączanie F-SCAN na Macu](connect-mac.md).
4. Otwórz **F-SCANT**.

Jeśli macOS zgłosi, że deweloper nie może zostać zweryfikowany, oznacza to, że Mac blokuje aplikację spoza App Store. Dla F-SCANT to normalne. Otwórz ją według kroków Apple [Open Anyway](https://support.apple.com/en-us/102445) tylko dla tej jednej aplikacji. Nie musisz wyłączać zabezpieczeń dla wszystkich aplikacji na Macu.
