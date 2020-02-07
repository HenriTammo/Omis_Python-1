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
#Koostage programm, mis annab ette sõnastiku tühjade väärtustega ja laske kasutajal for loopiga see ära täita.
#Koostage programm mis laseb enne koostatud sõnastikule lisada muud kategooriad kuni sisestatakse "ALL".
#Lisage sellele programmile juurde võimekus eemaldada nii mitu mudelit kuni kasutaja kirjutab "ALL".