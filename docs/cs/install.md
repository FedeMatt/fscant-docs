# Jak nainstalovat F-SCANT

Instalace se mírně liší podle počítače. Na Windows dostanete instalační soubor. Na Macu dostanete aplikaci F-SCANT, kterou umístíte do složky Aplikace. F-SCANT se neprodává v Microsoft Store ani v Mac App Store.

## Jak nainstalovat na Windows

1. Poklepejte na instalátor, který jste obdrželi (**F-SCANT-Setup-x64.exe**). Pokud Windows požádá o oprávnění, povolte je (může být vyžadováno heslo správce).
2. Přijměte licenci F-SCANT a licenci Silicon Labs, jakmile se zobrazí. Silicon Labs vyrábí malý USB ovladač, díky kterému počítač komunikuje s F-SCAN. Instalátor tento ovladač na PC nainstaluje za vás.
3. Otevřete **F-SCANT** z nabídky Start ve Windows.

Pokud Windows zobrazí varování SmartScreen (modrá nebo žlutá obrazovka s textem, že Windows chránil váš počítač), znamená to, že Windows zatím nezná vydavatele tohoto instalátoru. To se může stát, protože jste soubor dostali přímo, nikoli z Microsoft Store. Pokud jste instalátor získali od dodavatele, klikněte na možnost, která jej přesto spustí.

Pokud Windows požádá o povolení aplikací, které nepocházejí z obchodu, povolte to pro tuto instalaci. Díky tomuto nastavení může F-SCANT na PC běžet.

## Jak nainstalovat na Macu

1. Zkopírujte **F-SCANT** do složky Aplikace.
2. Nainstalujte USB ovladač, který je ve stejné složce jako F-SCANT. Nejprve si přečtěte **SILICON-LABS-VCP-LICENSE.txt**. Otevřete **Mac_OSX_VCP_Driver.zip**, otevřete diskový obraz uvnitř a spusťte **Install CP210x VCP Driver**. Tento ovladač umožní Macu rozpoznat F-SCAN přes USB.
3. Když macOS požádá o povolení softwaru od Silicon Labs, toto oprávnění zapněte. Po dokončení instalátoru povolte ovladač v **Nastavení systému → Obecné → Přihlašovací položky a rozšíření**: pod **Rozšíření** otevřete **Rozšíření ovladačů**, zapněte **CP210xVCPDriver** (`com.silabs.cp210x`) a v případě potřeby zadejte heslo Macu. Podrobné kroky a Video 1 jsou v [Připojení F-SCAN na Macu](connect-mac.md).
4. Otevřete **F-SCANT**.

Pokud macOS uvede, že vývojáře nelze ověřit, znamená to, že Mac blokuje aplikaci, která nepochází z App Store. U F-SCANT je to očekávané. Otevřete ji podle pokynů Apple [Open Anyway](https://support.apple.com/en-us/102445) pro tuto jednu aplikaci. Nemusíte vypínat zabezpečení pro všechny aplikace na Macu.
