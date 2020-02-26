import enum

globaalneMuutuja = 1

def kordamisFunktsioon():
    print("Hello")

def uheMuutujaga(tuhiMuutuja):
    tuhiMuutuja = tuhiMuutuja * 2
    return(tuhiMuutuja)

listTest = [1,2,3]
#print(uheMuutujaga(listTest))

def kaheMuutujaga(esimene, teine):
    return esimene + teine

print(kaheMuutujaga(239, 2))

def neljaMuutujaga(esimene,teine,kolmas,neljas):
    pass

neljaMuutujaga(1,3,56,21)

def parseList(listMillegaTeeme, mituKordaTeeme):
    for x in range(mituKordaTeeme):
        if x<len(listMillegaTeeme):
            print(listMillegaTeeme[x])
        else:
            x = 0


