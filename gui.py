# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import scrolledtext

from bs4 import BeautifulSoup

import volby as vlb

lst = list()
lst_url = list()
lst_dataAll = list()

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




def main():
    okno=Tk()
    okno.title("Project 3 - scrapování")
    okno.option_add('*Font', 'Verdana 10')
    okno.geometry("800x400+100+100")
    Label(okno, text=u"Zadej url: ").grid(row=0, sticky=W)
    Label(okno, text=u"Zadej název výst.souboru:   ").grid(row=1, sticky=W)
    url_str = Entry(okno,width=50)
    name_str= Entry(okno)
    url_str.grid(row=0, column=0,pady = 5, padx = 50)
    name_str.grid(row=1, column=0,pady = 5, padx = 50)
    text_area = scrolledtext.ScrolledText(okno,width=100,height=10,font=("calibre",10))
    text_area.grid(row=3,column=0,pady = 10, padx = 10)
    b = Button(okno,text="Zadej data",command=lambda: [(inData(url_str,name_str),correctURL())])
    b.grid(row=4, column=0,pady = 5, padx = 10)
    c = Button(okno, text="Načti data", command=lambda: showDataAll(text_area,getCityData()))
    c.grid(row=5, column=0,pady = 5, padx = 5)
    d = Button(okno, text="Ulož data", command=lambda: inData(url_str, name_str))
    d.grid(row=6, column=0, pady=5, padx=5)

    mainloop()


if __name__ == '__main__':
    main()







