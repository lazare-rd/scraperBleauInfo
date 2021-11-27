import requests
import bs4 
import regex as re
import random as ra
import time 

##############################################################
# ATTENTION : Scrapping file !!!
##############################################################

def fileToList(filePath):
    liste = []
    fichier = open(filePath, 'r')
    for line in fichier:
        liste.append("https://bleau.info"+line[0:len(line)-1])
    fichier.close()
    return liste

def getCotes(url):
    cotes_secteur=[]
    response = requests.get(url)
    responseText = response.text
    soup = bs4.BeautifulSoup(responseText, 'html.parser')
    for link in soup.stripped_strings:
        if re.match("^[0-9][abc]$|^[0-9][abc][+-]$", link):
            cotes_secteur.append(link)
    return cotes_secteur

def listToFile(filePath, liste):
    fichier = open(filePath, 'a')
    for item in liste:
        fichier.write(item+"\n")
    fichier.close()

def main():
    addrSecteurs = fileToList()
    for url in addrSecteurs:
        time.sleep(ra.randrange(1,5))
        cotes = getCotes(url)
        listToFile("dataCotations.txt", cotes)
        
        
if __name__ == '__main__':
    main()

