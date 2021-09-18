import requests
from bs4 import BeautifulSoup as BS
from requests import HTTPError

def downloadPage(stranka) -> BS:
    url_default = "https://volby.cz/pls/ps2017nss/"

    try:
        while True:

            odpoved = requests.get(url_default + stranka)
            odpoved.raise_for_status()

            break
        sp = BS(odpoved.text, "html.parser")
    except HTTPError as err:
        print("Stránka nenačtena, chybový kod: ", err)


    return sp

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
    nazvy_stran = list()

    for i in range(0,len(lst)):
        sp = downloadPage(lst[i][2])
        txt = sp.find("td", {'headers': 'sa2'}).text
        volici = txt.replace('\xa0', " ")
        txt = sp.find("td", {'headers': 'sa3'}).text
        obalky = txt.replace('\xa0', " ")
        txt = sp.find("td", {'headers': 'sa6'}).text
        hlasy = txt.replace('\xa0', " ")
        lst_strany = list()

        for td in sp.find_all("td",headers = ['t1sa2 t1sb3','t2sa2 t2sb3']):
            lst_strany.append(td.text)

        sub_data = [lst[i][0],lst[i][1],volici,obalky,hlasy,lst_strany]

        data_all.append(sub_data)

    sp1 = downloadPage(lst[0][2])
    for td in sp1.find_all("td",headers = ['t1sa1 t1sb2','t2sa1 t2sb2']):
        nazvy_stran.append(td.text)

    return data_all,nazvy_stran
















