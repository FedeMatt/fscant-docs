# Připojení F-SCAN na Macu

F-SCANT již máte. Tyto kroky nainstalují USB ovladač, který je k němu přiložen, a připojí F-SCAN. Stejný soubor ovladače se používá na Intel Macu i na Apple Silicon Macu. Procesor nevybíráte a ovladač si nestahujete z webu.

Budete potřebovat:

- F-SCANT
- F-SCAN zapnutý a zobrazující úvodní obrazovku
- USB kabel (do Macu, nebo přes hub či dok)
- L-CODE z faktury F-SCANT

## 1. Nainstalujte ovladač dodaný s F-SCANT

Ve složce, která přišla s F-SCANT, si před pokračováním přečtěte **SILICON-LABS-VCP-LICENSE.txt**. Poté otevřete **Mac_OSX_VCP_Driver.zip**, otevřete **SiLabsUSBDriverDisk.dmg** a poklepejte na **Install CP210x VCP Driver**.

Instalátor může požádat o heslo Macu. Jedná se o Silicon Labs CP210x VCP 6.0.3. Silicon Labs uvádí, že je určen pro Mac OS X 10.11 a novější. F-SCANT byl s tímto ovladačem ověřen na Intel Macu s macOS 15. Tato kontrola nepokrývá každý starší ani novější macOS.

Obrázek 4. Složka F-SCANT s instalátorem Silicon Labs vedle aplikace.

![Složka F-SCANT s instalátorem Silicon Labs vedle aplikace](../assets/images/connect-the-f-scan-on-mac/01-installer-with-app.png)

Obrázek 5. Instalátor Silicon Labs.

![Instalátor Silicon Labs](../assets/images/connect-the-f-scan-on-mac/02-silabs-installer.png)

## 2. Povolte rozšíření Silicon Labs

macOS vás i po dokončení instalátoru požádá o povolení ovladače. Na Macu, kde to bylo naposledy ověřeno:

1. Otevřete **Nastavení systému → Obecné → Přihlašovací položky a rozšíření**.
2. Pod **Rozšíření** otevřete **Rozšíření ovladačů** (uvádí `com.silabs.cp210x`).
3. Zapněte **CP210xVCPDriver**. V případě potřeby zadejte heslo Macu a klikněte na **Hotovo**.

Novější macOS může pro tento panel používat mírně odlišný název. Použijte video níže.

Na daném Macu nebyl nutný restart.

Video 1. Povolení ovladače Silicon Labs na Macu.

<div class="guide-video">
  <video controls preload="none" width="100%" src="/assets/videos/driver-extension-mac-intel.mp4">
  </video>
  <p class="guide-video-fallback" hidden>
    <strong>Video 1.</strong> Povolení ovladače Silicon Labs na Macu. Sledujte online:
    <a href="https://fscant-docs.fscan.com/cs/connect-mac/">fscant-docs/cs/connect-mac/</a>
  </p>
</div>

Pokud macOS zobrazí také samostatné tlačítko pro povolení systémového softwaru od Silicon Labs, povolte jej.

## 3. Zapojte F-SCAN

Zapněte F-SCAN a nechte jej na úvodní obrazovce. USB kabel zapojte do Macu, nebo přes hub či dok.

## 4. Připojení ve F-SCANT

Otevřete **F-SCANT**. Pokud macOS uvede, že vývojáře nelze ověřit, otevřete tuto aplikaci podle pokynů Apple: [Open Anyway](https://support.apple.com/en-us/102445). Nevypínejte bezpečnostní kontrolu pro všechny aplikace.

Klikněte na **Připojit**. Pokud F-SCANT požádá o L-CODE, zadejte kód z faktury F-SCANT. Když panel zobrazí **Připojeno** spolu se sériovým číslem a verzí, jste hotovi. Průběh připojení je také ve [Videu 2 v Jak připojit F-SCAN](connect.md).

## Pokud **Připojit** nefunguje

Před dalším pokusem zkontrolujte:

- Rozšíření Silicon Labs je zapnuté.
- Kabel je zapojený do Macu, nebo do hubu či doku.
- F-SCAN je zapnutý a zobrazuje úvodní obrazovku.
- L-CODE odpovídá faktuře.

Nesprávný L-CODE zobrazí **CHYBA: Byl zadán nesprávný L-CODE. Zkuste to znovu!**
