thisdict = {
  "mark": "Audi",
  "mudel": "Quattro",
  "aasta": 1996
}
print(thisdict)

x = thisdict["mudel"]
print(x)
y = thisdict.get("mudel")#SAMA mis eelmine
print(y)

thisdict["varv"] = "punane"
print(thisdict)

thisdict["aasta"] = 2018

for x in thisdict:
  print(x)
thisdict.pop("mudel")
print(thisdict)


'''
tuhi = {}

for x in range(3):
      kategooria = input("Kategooria - ")
      vaartus = input("Väärtus - ")
      tuhi[kategooria] = vaartus
print(tuhi)

'''

testDict = {
  "liik":"Ahven",
  "vanus":12,
  "värv":"hall"
}
print(testDict)
for x in testDict:
    inputVariable = input(" - ")
    if inputVariable == "ALL":
          break
    else:  
      testDict[x] = inputVariable
print(testDict)


#Koostage programm, mis annab ette sõnastiku tühjade väärtustega ja laske kasutajal for loopiga see ära täita.
#Koostage programm mis laseb enne koostatud sõnastikule lisada muud kategooriad 
# kuni sisestatakse "ALL".
#Lisage sellele programmile juurde võimekus eemaldada nii mitu mudelit kuni kasutaja kirjutab "ALL".