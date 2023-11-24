#!/usr/bin/env python3

import requests, json, time, html, re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

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

def refresh_result_sdy():
    prd = open("sdy/data_sdy.json")
    periodes = json.load(prd)
    periode = periodes['periode']
    prd.close()
    url = "http://www.sidney4dpools.com/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    date = []
    rr = []
    for i,x in enumerate(data.find_all("table", {"class": "stripeMe"})):
        for a in x.find_all("td"):
            dd = []
            for d in a.find_all("strong"):
                if "-" in d.text:
                    date.append(d.text)
            for d in a.find_all("img"):
                dd.append(d['src'][-5])
            if dd != []:
                rr.append("".join(dd))
    result = {}
    for i,d in enumerate(date):
        result['data_'+str(i)] = [{"tanggal": d}, {"periode": str(periode)}, {"result": rr[i]}]
        periode-=1
    return result

def refresh_result_tw():
    url = "http://www.tw4dpools.com/home.php"
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get(url)
    drive = driver.find_elements(By.CSS_SELECTOR, "tr.results_row td div div")
    rr = []
    for d in drive:
        if d.text != "":
            if "\n" in d.text:
                x = d.text.replace("\n","")
                rr.append(x)
    datdr = driver.find_elements(By.CSS_SELECTOR, "tr.results_row td")
    date = []
    for x in datdr:
        if "," in x.text:
            date.append(x.text)
    result = {}
    for i,d in enumerate(rr):
        result['data_'+str(i)] = [{"tanggal": date[i]}, {"result": d}]
    return result
    
def refresh_result_cam():
    url = "https://magnumcambodia.com/apps/results?first=first"
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get(url)
    drive = driver.find_elements(By.CSS_SELECTOR, "b")
    date = []
    rr = []
    for x in drive:
        if "-" in x.text:
            date.append(x.text)
        asd = x.find_elements(By.CSS_SELECTOR, "img")
        dt = []
        for d in asd:
            ss = d.get_attribute("src")
            if "/bola/" in ss:
                dt.append(ss[-19])
        if dt != []:
            rr.append("".join(dt))
    result = {}
    for i,d in enumerate(date):
        result['data_'+str(i)] = [{"tanggal": d}, {"result": rr[i]}]
    return result
    
def refresh_result_chn():
    url = "https://www.china4dlottery.com/"
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get(url)
    drive = driver.find_elements(By.CSS_SELECTOR, "div.blog_wrap")
    date = []
    rr = []
    for x in drive:
        imgs = []
        date.append(x.find_element(By.CSS_SELECTOR, "div.post_title h2 a").text[17:])
        for img in x.find_elements(By.CSS_SELECTOR, "img.wp-smiley"):
            if img.get_attribute("alt") != ";logo4d;":
                imgs.append(img.get_attribute("src")[-5])
        if imgs != []:
            rr.append("".join(imgs))
    result = {}
    for i,d in enumerate(date):
        result['data_'+str(i)] = [{"tanggal": d}, {"result": rr[i]}]
    return result

def refresh_result_hariini():
    url = "https://angkatogelhariini.com/"
    r = requests.get(url)
    data = BeautifulSoup(r.content, "html5lib")
    val = []
    row = {}
    for x in data.find_all("p"):
        d = re.sub(r'\s+',' ',html.unescape(x.text))
        if d != "":
            val.append(d)
    asd = 0
    rr = []
    rep = 0
    for f in val:
        asd += 1
        if asd < 5:
            rr.append(f)
        if asd == 5:
            rep += 1
            if rep > 1:
                row["data_"+str(rep-1)] = rr
            asd = 0
            rr = []
        if rep == 51:
            break
    return row







