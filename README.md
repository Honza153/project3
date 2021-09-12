--------------- Projekt3 - Elections Scraper -----------------------------

# Popis projektu:

projekt řeší extrahování volebních dat ze zadaného územního celku

# Instalace knihoven:
použité nihovny jsou vidět v souboru requirements.txt. Pro instalaci knihoven byl použit program pip.
Pro projekt bylo vytvořeno nové<env> prostředí a taktéž je vhodné upgradovat program pip na poslední verzi

python -m pip install --upgrade pip

Pro práci s webovými stránkami slouží knihovna request
$ pip install requests or python -m pip install requests
Pro práci extrahování dat je využita knihovna BeautifulSoup
$ pip install beautifulsoup4  or python -m pip install beautifulsoup4 
Pro grafické rozhraní je využita knihovna tkinter, jež je součástí distribuce pythonu
$ from tkinter import *
Pro zobrazení načtených dat je využita knihovna scrolledtext, tuto je nutno naimportovat zvláště
$ from tkinter import scrolledtext

# Spuštění projektu:

Po spuštění programu z cmd je nutno do okna aplikace zadat dva povinné argumenty:
- URL územního celku jež chceme vyscrapovat
- Název výsledného souboru ve formátu *.csv, přípona se neuvádí

Výsledky se uloží do pracovního adresáře/složky s příponou *.csv

# Ukázka projektu:

1. Územní celek Opava: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8105
2. Výsledný soubor: vysledky_opava.csv

Po otevření okna aplikace je nutno zadat 2 povinné argumenty
button «Zadej data» - slouží k přenosu vstupních dat do aplikace a inicializaci extrahování dat
button «Načti data» - slouží k zobrazení dat v text_area, jestliže se data nezobrazí,došlo ke špatnému vložení url nebo k chybě spojení se serverem
button «Ulož data» - slouží k uložení dat do pracovního prostředí uživatele
button «Vymaž vstup» - slouží k vymazání zadaných dat = argumentů
button «Ukončit» - slouží k ukončení aplikace

512974	Bělá	559	379	375	['Občanská demokratická strana', 'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI', 'Česká str.sociálně demokrat.', 'Radostné Česko', 'STAROSTOVÉ A NEZÁVISLÍ', 'Komunistická str.Čech a Moravy', 'Strana zelených', 'ROZUMNÍ-stop migraci,diktát.EU', 'Strana svobodných občanů', 'Blok proti islam.-Obran.domova', 'Občanská demokratická aliance', 'Česká pirátská strana', 'Česká národní fronta', 'Referendum o Evropské unii', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016', 'SPR-Republ.str.Čsl. M.Sládka', 'Křesť.demokr.unie-Čs.str.lid.', 'Česká strana národně sociální', 'REALISTÉ', 'SPORTOVCI', 'Dělnic.str.sociální spravedl.', 'Svob.a př.dem.-T.Okamura (SPD)', 'Strana Práv Občanů']