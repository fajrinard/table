#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def refresh():
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