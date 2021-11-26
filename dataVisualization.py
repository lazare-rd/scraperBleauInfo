import numpy as np 
import plotly.graph_objects as plt 

def fileToList(filePath):
    liste = []
    fichier = open(filePath, 'r')
    for line in fichier:
        liste.append(line[0:len(line)-1])
    fichier.close()
    return liste

listeCotations = fileToList("dataCotations.txt")
dictCotations = {}

for cote in listeCotations:
    if cote in dictCotations:
        dictCotations[cote]+=1
    else:
        dictCotations[cote]=1

dictCotations["9a"]=2

fig = plt.Figure(data=[plt.Pie(labels=list(dictCotations.keys()), values=list(dictCotations.values()), textinfo='label+percent')])
fig.show()