# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import scrolledtext
from bs4 import BeautifulSoup
import volby as vlb
import csv
import sys

lst = list()
lst_url = list()
lst_dataAll = list()
lst_head = ["kód obce","název obce","voliči v seznamu","vydané obálky","platné hlasy","kandidující strany"]

def inData(zdr1,zdr2):
    lst.clear()
    obsah = zdr1.get()
    lst.append(obsah)
    obsah1 = zdr2.get()
    lst.append(obsah1)


def correctURL() -> BeautifulSoup:
    url = lst[0][30:]
    sp = vlb.downloadPage(url)
    return sp



def getCityData() -> list():
    sp1 = correctURL()
    lst_url = vlb.getCity(sp1)
    return lst_url




def showDataAll(zdr,lt):
    lst_dataAll = vlb.getVoteData(lt)
    zdr.insert(END,lst_dataAll)

def saveData(lt):
    lst_dataAll,ltnazvy = vlb.getVoteData(lt)
    lst_head.extend(ltnazvy)
    with open(lst[1]+".csv", "wt") as f :
        f_writer = csv.writer(f, delimiter=";")
        f_writer.writerow(lst_head)
        f_writer.writerows(lst_dataAll)

def deleteEntry(z1,z2):
    z1.delete(0,END)
    z2.delete(0, END)

def disBut(zdroj):
    zdroj["state"] = DISABLED



def main():
    okno=Tk()
    okno.title("Projekt3: Elections Scraper")
    okno.option_add('*Font', 'Verdana 10')
    okno.geometry("1100x400+100+100")
    Label(okno, text=u"Zadej url: ").grid(row=0, sticky=W)
    Label(okno, text=u"Zadej název výst.souboru:   ").grid(row=1, sticky=W)
    url_str = Entry(okno,width=70)
    name_str= Entry(okno)
    url_str.grid(row=0, column=1,columnspan=10,pady = 5 )
    name_str.grid(row=1, column=1,pady = 5)
    text_area = scrolledtext.ScrolledText(okno,width=150,height=10,font=("calibre",10))
    text_area.grid(row=3,column=0,columnspan=30, rowspan=4,pady = 10, padx = 10)
    b = Button(okno,text="Zadej data",command=lambda: [(inData(url_str,name_str),correctURL())])
    b.grid(row=8, column=0,pady = 5, padx = 10)
    c = Button(okno, text="Načti data", command=lambda: [showDataAll(text_area,getCityData()),disBut(b)])
    c.grid(row=9, column=0,pady = 5, padx = 5)
    d = Button(okno, text="Ulož data", command=lambda: [saveData(getCityData()),disBut(c) ])
    d.grid(row=10, column=0, pady=5, padx=5)
    e = Button(okno, text="Vymaž vstup", command=lambda: deleteEntry(url_str,name_str))
    e.grid(row=8, column=1, pady=5, padx=5)
    f = Button(okno, text="Ukončit", command=lambda: sys.exit(0))
    f.grid(row=9, column=1, pady=5, padx=5)

    mainloop()


if __name__ == '__main__':
    main()







