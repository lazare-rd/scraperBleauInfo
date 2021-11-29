import requests
import bs4
import regex as re
from scrapperBleauIInfo_cotations import listToFile
from scrapperBleauIInfo_cotations import fileToList
import random as ra
import time

def getNbreRep(url):
    repete = False
    matching_items = []
    response = requests.get(url)
    responseText = response.text
    soup = bs4.BeautifulSoup(responseText, "html.parser")
    for item in soup.stripped_strings :
        if re.match("Répétitions publiques", item):
            repete = True
    if repete :
        for item in soup.stripped_strings:
            if re.match("\([0-9]+ au total\)", item):
                matching_items.append(item)
        nbreRep = int(re.findall("[0-9]+" , matching_items[-1])[0])
        return nbreRep
    return 0

def getUrlBloc(url):
    listUrl = []
    response = requests.get(url)
    responseTexte = response.text
    soup = bs4.BeautifulSoup(responseTexte, 'html.parser')
    soupUrl = soup.find_all(href=re.compile('\/.+\/[0-9]+\.html'))
    for item in soupUrl:
        listUrl.append(str(re.findall('\/[^\/]+\/[0-9]+\.html', str(item))))
    return list(set(listUrl))

# ATTENTION : Scrapping method !!!
def getAllUrlBlocs():
    listUrlSecteurs = fileToList("dataSecteurs.txt")
    for url in listUrlSecteurs:
        time.sleep(ra.randrange(1,5))
        urlBLocs = getUrlBloc(url)
        listToFile("dataUrlBlocs.txt", urlBLocs)

def remplaceData(filePath):
    urlListe = []
    file = open(filePath, 'r')
    for url in file :
        if url != "\n":
            urlListe.append(url[:-1])
    file.close()
    return urlListe





