import requests
import os
import sys
import csv
from bs4 import BeautifulSoup as BS
from requests import HTTPError


vloz_url= "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
cut_url = vloz_url[30:]

def downloadPage(stranka) -> BS:
    url_default = "https://volby.cz/pls/ps2017nss/"
    while True:
        odpoved = requests.get(url_default + stranka)
        odpoved.raise_for_status()

        break
    sp = BS(odpoved.text, "html.parser")

    return sp

#sp = downloadPage(cut_url)

def getCity(soup) ->list:
    data = list()

    for td in soup.find_all("td", {'headers': 't1sa1 t1sb1'}):
        kod = td.text
        link = td.find_next('a')['href']
        nazev = td.find_next("td", {'headers': 't1sa1 t1sb2'})
        pridej = [kod,nazev.text,link]
        data.append(pridej)

    return data

def getVoteData(lst:list)-> list:
    data_all = list()

    for i in range(0,len(lst)):
        sp = downloadPage(lst[i][2])
        txt = sp.find("td", {'headers': 'sa2'}).text
        volici = txt.replace('\xa0', " ")
        txt = sp.find("td", {'headers': 'sa3'}).text
        obalky = txt.replace('\xa0', " ")
        txt = sp.find("td", {'headers': 'sa6'}).text
        hlasy = txt.replace('\xa0', " ")
        lst_strany = list()
        for td in sp.find_all('td', {'headers': 't1sa1 t1sb2'}):
            lst_strany.append(td.text)
        for td in sp.find_all('td', {'headers': 't2sa1 t2sb2'}):
            lst_strany.append(td.text)
        #lst_strany.remove('-')
        sub_data = [lst[i][0],lst[i][1],volici,obalky,hlasy,lst_strany]
        #print(sub_data)
        data_all.append(sub_data)

    return data_all












