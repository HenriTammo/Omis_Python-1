from functions import *

#Muutujad
mangija = "X"
arvuti = "O"
mangKaib = True
kaiguVaartus = 0
manguLaud = [".",".",".",".",".",".",".",".",".","."]
sygavus = 0

#Mänguprotsess
while mangKaib:
    if sygavus < 9:
        joonista(manguLaud)
        kaiguVaartus = int(input("Siseta käik - "))
        if manguLaud[kaiguVaartus] == ".":
            if sygavus%2: 
                teeKaik(manguLaud, kaiguVaartus, arvuti)
            else:
                teeKaik(manguLaud, kaiguVaartus, mangija)
        else:
            continue
        sygavus=sygavus+1
    else: 
        joonista(manguLaud)
        print("VIIK!")
        mangKaib = False










#Mängijad
#Mängulaud
#Mängijatemärgid
#Reeglistik
#Võitjat



