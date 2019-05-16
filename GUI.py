# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:00:15 2019

@author: ekrembulbul
"""

# Gerekli kutuphaneler
from tkinter import *
from Skortahmin import skorTahmin
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

macKodu = -1

# 'Tahmin et' butonuna tiklandigi an girilen mac kodu alinir ve tahminler
# yapilir.
def getMacKodu():
    global count
    macKodu = int(macKoduEntry.get())
    rates = WebScraping(macKodu)
    print(len(rates))
    print(rates)
    
    np_rates = []
    np_rates.append(rates)
    
    # Tahmin yapilir.
    ms, ms_gol, kg, skor = skorTahmin(np_rates)
    ms = str((ms))
    ms_gol = str((ms_gol))
    kg = str((kg))
    skor = str(skor)
    
    global msL
    global ms_golL
    global kgL
    global skorL
    
    # Sonuclar ekrana yazdirilir.
    msL["text"] = ms
    ms_golL["text"] = ms_gol
    kgL["text"] = kg
    skorL["text"] = skor
    
# Site uzerinden macin oranlari alinir.
def WebScraping(mac_kodu):
    url = 'http://arsiv.mackolik.com/Genis-Iddaa-Programi'
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.execute_script('return document.documentElement.outerHTML')
    sel_soup = BeautifulSoup(html, 'html.parser')
    rates = []
    
    # Her oran html tag'inin class ismi ile alinir.
    TakeRate('MS1', mac_kodu, sel_soup, rates)
    TakeRate('MSX', mac_kodu, sel_soup, rates)
    TakeRate('MS2', mac_kodu, sel_soup, rates)
    TakeRate('IY1', mac_kodu, sel_soup, rates)
    TakeRate('IYX', mac_kodu, sel_soup, rates)
    TakeRate('IY2', mac_kodu, sel_soup, rates)
    TakeRate('H1', mac_kodu, sel_soup, rates)
    TakeRate('HX', mac_kodu, sel_soup, rates)
    TakeRate('H2', mac_kodu, sel_soup, rates)
    TakeRate('KG1', mac_kodu, sel_soup, rates)
    TakeRate('KG0', mac_kodu, sel_soup, rates)
    TakeRate('CS1-X', mac_kodu, sel_soup, rates)
    TakeRate('CS1-2', mac_kodu, sel_soup, rates)
    TakeRate('CSX-2', mac_kodu, sel_soup, rates)
    TakeRate('IYAU151', mac_kodu, sel_soup, rates)
    TakeRate('IYAU152', mac_kodu, sel_soup, rates)
    TakeRate('AU151', mac_kodu, sel_soup, rates)
    TakeRate('AU152', mac_kodu, sel_soup, rates)
    TakeRate('AU1', mac_kodu, sel_soup, rates)
    TakeRate('AU2', mac_kodu, sel_soup, rates)
    TakeRate('AU351', mac_kodu, sel_soup, rates)
    TakeRate('AU352', mac_kodu, sel_soup, rates)
    TakeRate('TG0-1', mac_kodu, sel_soup, rates)
    TakeRate('TG2-3', mac_kodu, sel_soup, rates)
    TakeRate('TG4-6', mac_kodu, sel_soup, rates)
    TakeRate('TG7_', mac_kodu, sel_soup, rates)
    
    driver.close()
    return rates

# Class ismi hazirlanir.
def TakeRate(code, mac_kodu, sel_soup, rates):
    _class = 'iddaa-rate ' + str(mac_kodu) + code
    tmp = sel_soup.find('a', {'class':_class})
    if (tmp != None):
        rates.append(float(tmp.text))
    else:
        rates.append(float(1))

# Arayuz baslatilir.
root = Tk()

# Arayuz olusturulur.
macKoduLabel = Label(root, text="Maç Kodu: ", font="Arial 14")
macKoduEntry = Entry(root, font="Arial 14")
button = Button(root, text="Tahmin Et", font="Arial 14", command=getMacKodu, padx=5, pady=5)
ms_label = Label(root, text="Maç Sonucu: ", font="Arial 14")
ms_gol_label = Label(root, text="Gol Sayısı (3 Gol): ", font="Arial 14")
kg_label = Label(root, text="Iki takımda gol atar: ", font="Arial 14")
skor_label = Label(root, text="Olası Skorlar: ", font="Arial 14")
msL = Label(root, font="Arial 14")
ms_golL = Label(root, font="Arial 14")
kgL = Label(root, font="Arial 14")
skorL = Label(root, font="Arial 14")

# Label'lar ve button arayuz uzerinde yerlestirilir.
macKoduLabel.grid(row=0, column=0, padx=10, pady=10)
macKoduEntry.grid(row=0, column=1, padx=10, pady=10)
button.grid(row=1, columnspan=2, padx=10, pady=10)
ms_label.grid(row=2, column=0, padx=10, pady=10)
ms_gol_label.grid(row=3, column=0, padx=10, pady=10)
kg_label.grid(row=4, column=0, padx=10, pady=10)
skor_label.grid(row=5, column=0, padx=10, pady=10)
msL.grid(row=2, column=1, padx=10, pady=10)
ms_golL.grid(row=3, column=1, padx=10, pady=10)
kgL.grid(row=4, column=1, padx=10, pady=10)
skorL.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()