from typing import overload
import requests
import bs4
import regex as re
from dataVisualization import fileToList
import scrapperBleauIInfo_cotations
import random as ra
import time

def getNbreRep(url):
    matching_items = []
    response = requests.get(url)
    responseText = response.text
    soup = bs4.BeautifulSoup(responseText, "html.parser")
    for item in soup.stripped_strings:
        if re.match("\([0-9]+ au total\)", item):
            matching_items.append(item)
    nbreRep = int(re.findall("[0-9]+" , matching_items[-1])[0])
    return nbreRep

def getUrlBloc(url):
    listUrl = []
    response = requests.get(url)
    responseTexte = response.text
    soup = bs4.BeautifulSoup(responseTexte, 'html.parser')
    soupUrl = soup.find_all(href=re.compile('\/.+\/[0-9]+\.html'))
    for item in soupUrl:
        listUrl.append(str(re.findall('\/[^\/]+\/[0-9]+\.html', str(item))))
    return list(set(listUrl))

def getAllUrlBlocs():
    listUrlSecteurs = scrapperBleauIInfo_cotations.fileToList("dataSecteurs.txt")
    for url in listUrlSecteurs:
        time.sleep(ra.randrange(1,5))
        urlBLocs = getUrlBloc(url)
        scrapperBleauIInfo_cotations.listToFile("dataUrlBlocs.txt", urlBLocs)

getAllUrlBlocs()


