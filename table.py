#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def refresh_result_sgp():
    url = "https://tabelpakde.com/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    numball = []
    tgl = []
    periode = []
    for x in data.find_all("td", {"class":"text-center"}):
        numb = []
        for r in x.find_all("span", {"class":"numball"}):
            numb.append(r.text)
        if numb != []:
            numball.append("".join(numb))
        if "," in x.text:
            tgl.append(x.text)
        if "-" in x.text:
            periode.append(x.text)
    result = {}
    for i,x in enumerate(periode):
        result['data_'+str(i)] = [tgl[i], periode[i], numball[i]]
    return result

def refresh_result_hk():
    url = "https://tabelpakde.com/data-hk/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    numball = []
    tgl = []
    periode = []
    for x in data.find_all("td", {"class":"text-center"}):
        if "," in x.text:
            tgl.append(x.text)
        if "-" in x.text:
            periode.append(x.text)
        if "," not in x.text and "-" not in x.text:
            numball.append(x.text)
    result = {}
    for i,x in enumerate(periode):
        result['data_'+str(i)] = [tgl[i], periode[i], numball[i]]
    return result

def refresh_livedraw_sgp():
    url = "https://tabelpakde.com/live-draw-sgp/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    value1 = []
    value2 = []
    for x in data.find_all("td", {"class":"box-value"}):
        try:
            if int(x.text):
                value2.append(x.text)
        except:
            pass
    for x in data.find_all("td", {"class":"box-color sgp"}):
        if "," in x.text:
            value1.append(x.text)
        try:
            if int(x.text):
                value2.append(x.text)
        except:
            pass
    result = {
        'tanggal1': value1[0],
        'tanggal2': value1[1],
        'prize1': value2[0],
        'prize2': value2[1],
        'prize3': value2[2],
        'starter_prize': value2[3:13],
        'consolation_prize': value2[13:23],
        '4d_result': value2[23],
        'winning_number': value2[24:-1],
        'additional_number': value2[-1]
    }
    return result

def refresh_livedraw_hk():
    url = "https://tabelpakde.com/live-draw-hk/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    value = []
    tgl = []
    for i,x in enumerate(data.find_all("td", {"class":"box-value"})):
        va = []
        if i == 0:
            for a in x.text:
                try:
                    if a == "0":
                        va.append(a)
                    if int(a):
                        va.append(a)
                except:
                    pass
        else:
            for a in x.find_all("span", {"class": "hkball"}):
                try:
                    if a.text.isdigit():
                        va.append(a.text)
                except:
                    pass
        if va != []:
            value.append("".join(va))
    for x in data.find_all("td", {"class":"box-color hk"}):
        if "," in x.text:
            tgl.append(x.text)
        try:
            if int(x.text):
                value.append(x.text)
        except:
            pass
    result = {
        'tanggal': tgl[0],
        'prize1': value[0],
        'prize2': value[1],
        'prize3': value[2],
        'starter_prize': value[3:7],
        'consolation_prize': value[7:]
    }
    return result

def refresh_prediksi_sgp():
    url = "https://tabelpakde.com/prediksi-sgp/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    value1 = []
    value2 = []
    for i,x in enumerate(data.find_all("td", {"class":"column-1"})):
        if i != 0:
            value1.append(x.text)
    for x in data.find_all("td", {"class":"column-2"}):
        value2.append(x.text)
    while("" in value1):
        value1.remove("")
    while("" in value2):
        value2.remove("")
    result = {}
    for i,d in enumerate(value1):
        result[d] = value2[i]
    return result

def refresh_prediksi_hk():
    url = "https://tabelpakde.com/prediksi-hk/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    value1 = []
    value2 = []
    for i,x in enumerate(data.find_all("td", {"class":"column-1"})):
        if i != 0:
            value1.append(x.text)
    for x in data.find_all("td", {"class":"column-2"}):
        value2.append(x.text)
    while("" in value1):
        value1.remove("")
    while("" in value2):
        value2.remove("")
    result = {}
    for i,d in enumerate(value1):
        result[d] = value2[i]
    return result

def refresh_prediksi_sdy():
    url = "https://tabelpakde.com/prediksi-sdy/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    value1 = []
    value2 = []
    for i,x in enumerate(data.find_all("td", {"class":"column-1"})):
        value1.append(x.text)
    for x in data.find_all("td", {"class":"column-2"}):
        value2.append(x.text)
    while("" in value1):
        value1.remove("")
    while("" in value2):
        value2.remove("")
    result = {}
    for i,d in enumerate(value1):
        result[d] = value2[i]
    return result

def refresh_result_macau():
    url = "https://rgb.team/data-macau/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    jam = []
    rr = []
    for i,x in enumerate(data.find_all("td")):
        if ":" in x.text:
            jam.append(x.text)
        if i > 7:
            rr.append(x.text)
    result = {'jam':[],'table':{}}
    result['jam'] = jam
    for i,d in enumerate(rr):
        result['table']['tr_'+str(i)] = rr[:7]
        del rr[:7]

    return result
