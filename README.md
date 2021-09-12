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

kód obce	název obce	voliči v seznamu	vydané obálky	platné hlasy	kandidující strany	
512974	Bělá	559	379	375	['22', '0', '0', '27', '1', '9', '15', '3', '8', '5', '1', '1', '18', '0', '1', '15', '150', '0', '1', '30', '0', '3', '0', '1', '63', '1']	
506192	Bohuslavice	1 380	908	905	['48', '3', '1', '48', '0', '20', '32', '3', '6', '9', '1', '2', '82', '0', '1', '47', '349', '0', '0', '141', '0', '3', '1', '0', '106', '2']	
506214	Bolatice	3 533	2 309	2 292	['99', '1', '3', '126', '1', '41', '101', '18', '11', '25', '1', '0', '165', '0', '0', '417', '844', '1', '4', '125', '0', '7', '4', '3', '290', '5']