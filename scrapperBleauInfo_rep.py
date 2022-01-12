from fake_useragent.fake import UserAgent
import requests
import bs4
import regex as re
from scrapperBleauIInfo_cotations import listToFile
from scrapperBleauIInfo_cotations import fileToList
import random as ra
import time

fakeUserAgent = [{"User-Agent" : "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)"}, 
                {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)"},
                {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1"},
                {"User-Agent" : "Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11"},
                {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"},
                {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13"},
                {"User-Agent" : "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"},
                {"User-Agent" : "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1"},
                {"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1"},
                {"User-Agent" : "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"}]

def getNbreRep(responseText):
    repete = False
    matching_items = []
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

def getCoteBlocPage(responseText):
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
    listUrlBlocs = fileToList(filePath)
    listRepBlocs = {}
    for url in listUrlBlocs :
        time.sleep(ra.randrange(1,5)/100)
        response = requests.get(url, headers=fakeUserAgent[ra.randrange(0, len(fakeUserAgent)-1)])
        responseText = response.text
        cot = getCoteBlocPage(responseText)
        nbrRep = getNbreRep(responseText)
        if cot in listRepBlocs : 
            listRepBlocs[cot] += nbrRep
        else : 
            listRepBlocs[cot] = nbrRep
    return listRepBlocs

def dicoToFile(dico, filePath): 
    file = open(filePath, 'a')
    for key, value in dico.items() :
        file.write(key + "," + str(value) + "\n")
    file.close()


def main():
    dicoCotRep = getAllRepOnAllBlocs("dataUrlBlocs.txt")
    dicoToFile(dicoCotRep, "finalData.txt")

if __name__ == '__main__':
    main()
    
