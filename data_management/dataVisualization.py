import numpy as np 
import plotly.graph_objects as plt 

def getDatafromFile(filePath):
    liste = []
    fichier = open(filePath, 'r')
    for line in fichier:
        liste.append(line[0:len(line)-1])
    fichier.close()
    return liste

def fileToDico(filePath):
    dico = {}
    dico["Autre"]=0
    fichier = open(filePath, 'r')
    for line in fichier :
        splittedLine = line.split(",") 
        if splittedLine[0] != "Missed" :
            if int(splittedLine[0][0]) >= 6 :
                dico[splittedLine[0]] = int(splittedLine[1])
            else :
                dico["Autre"] += int(splittedLine[1])
    fichier.close()
    return dico

# listeCotations = getDatafromFile("data/dataCotations.txt")
# dictCotations = {}

# for cote in listeCotations:
#     if cote in dictCotations:
#         dictCotations[cote]+=1
#     else:
#         dictCotations[cote]=1

# dictCotations["9a"]=2

dictRep_pre = fileToDico("data/dataRepCot.txt")
dictRep = {}

def getSumReps(dico):
    somme = 0
    for v in dico.values() : 
        somme += v
    return somme

def sortDico(dico):
    sortedDico = {}
    for k in sorted(dico.keys()):
        sortedDico[k] = dico[k]
    return sortedDico

dictRep = sortDico(dictRep_pre)

fig = plt.Figure(data=[plt.Pie(labels=list(dictRep.keys()), values=list(dictRep.values()), textinfo='label+percent')])
fig.show()