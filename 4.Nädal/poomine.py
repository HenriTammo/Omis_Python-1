import random
#loome poomise mängu
#tekitame ise suvaliste sõnade listi
#Liigutame sõna eraldi listi tähe haaval.
#Tekitame listi mis on meie display: [_,_,_,_,_]
#Kasutaja saab kuus korda arvata.
#Kui kasutaja arvab õigesti: [_,_,_,a,_]
#Soovitan kasutada lisafunktsiooni IN 

#Sõnade listi:
suvalisedSonad = ["kala", "teine", "pall", "koer", "arvuti", "auto", "sein", "monitor", "mees", "aken"]
listiPikkus = len(suvalisedSonad) - 1
valija = random.randint(0,listiPikkus)
valitudSona = suvalisedSonad[valija]
displayList = []
mangKaib = True

def parseWord(word):
    newList = []
    for x in range(len(word)):
        newList.append(word[x])
    return newList

uksiksonaList = parseWord(valitudSona)
#print(uksiksonaList)
for x in range(len(uksiksonaList)):
    displayList.append("_")

guessIndex = []
elud = 6

while mangKaib:
    print (displayList)
    userGuess = input("Paku täht - ")
    if userGuess == valitudSona:
        print("Sinu võit!")
        print("Elusid alles : ", elud)
        uuestiMang=input("Kas soovid uuesti mängida? [j/e] - ")
        if uuestiMang == "j":
            valija = random.randint(0,listiPikkus)
            valitudSona = suvalisedSonad[valija]
            displayList = []
            uksiksonaList = parseWord(valitudSona)
            elud = 6
            for x in range(len(uksiksonaList)):
                displayList.append("_")
        else:
            mangKaib = False
    else:
        if userGuess in uksiksonaList:
            for x in range(len(uksiksonaList)):
                if uksiksonaList[x] == userGuess:
                    guessIndex.append(x)
            for x in range(len(guessIndex)):
                displayList[guessIndex[x]] = userGuess
            guessIndex = []
        else: 
            elud = elud-1
            print ("Sul on alles " , elud , " elu")
            if elud == 0:
                print("Elud otsas!")
                print(uksiksonaList)
                uuestiMang=input("Kas soovid uuesti mängida? [j/e] - ")
                if uuestiMang == "j":
                    valija = random.randint(0,listiPikkus)
                    valitudSona = suvalisedSonad[valija]
                    displayList = []
                    uksiksonaList = parseWord(valitudSona)
                    elud = 6
                    for x in range(len(uksiksonaList)):
                        displayList.append("_")
                else:
                    mangKaib = False
        if displayList == uksiksonaList:
            print("Sinu võit!")
            print("Elusid alles : ", elud)
            uuestiMang=input("Kas soovid uuesti mängida? [j/e] - ")
            if uuestiMang == "j":
                valija = random.randint(0,listiPikkus)
                valitudSona = suvalisedSonad[valija]
                displayList = []
                uksiksonaList = parseWord(valitudSona)
                elud = 6
                for x in range(len(uksiksonaList)):
                    displayList.append("_")
            else:
                mangKaib = False








