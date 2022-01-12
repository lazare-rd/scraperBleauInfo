import requests
import bs4
import regex as re
from scrapperBleauIInfo_cotations import listToFile
from scrapperBleauIInfo_cotations import fileToList
from fake_useragent import UserAgent
import random as ra
import time

def getNbreRep(url, uA):
    repete = False
    matching_items = []
    response = requests.get(url, headers = uA)
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

def getCoteBlocPage(url, uA):
    response = requests.get(url, headers = uA)
    responseText = response.text
    soup = bs4.BeautifulSoup(responseText, "html.parser")
    if (len(re.findall('[0-9][abc]?[+-]?' ,str(soup.find('h3'))))>1):
        return re.findall('[0-9][abc]?[+-]?' ,str(soup.find('h3')))[1]
    return re.findall('[0-9][abc]?[+-]?' ,str(soup.find('h3')))[0]

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

def getAllRepOnAllBlocs(filePath):
    ua = UserAgent()
    listUrlBlocs = fileToList("dataUrlBlocs.txt")
    listRepBlocs = {}
    for url in listUrlBlocs :
        time.sleep(ra.randrange(1,5)/100)
        cot = getCoteBlocPage(url)
        nbrRep = getNbreRep(url)


def main():
    ua = UserAgent()
    print(ua['Internet Explorer'])

if __name__ == '__main__':
    main()
    
# response = requests.get("https://bleau.info/canon/4460.html")
# responseText = response.text
# soup = bs4.BeautifulSoup(responseText, "html.parser")
# print(soup.find('h3'))

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

