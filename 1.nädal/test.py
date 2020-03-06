'''from math import *






#print("Hello \nworld!")
#print("testing", end=" ")
#print(5+5/2)
#pindala=20.34666
#print(pindala)
#print(pindala, " on pindala")
#kala=30
#print(pindala + kala)

#kokku=pindala*kala
#print(kokku)
#print("Pindala on %0.2f." % (pindala))

#kasutaja=input("Mis on su nimi? - ")
#print(kasutaja)

#arvEsimene= int(input("Esimene arv? - "))
#arvTeine= int(input("Teine arv? - "))

#print(arvEsimene + arvTeine)

#meieEsimene= ["politsei","tuletõrje","kiirabi"]
#print(meieEsimene[1])


#Kasutaja sisestab meile ruudu küljed, meie arvutame need kokku
#ja anname vastu pindala ja ümbermõõdu
#Omistamine ja inputi küsimine.

print(abs(-3))
print(round(2.6375, 2))
print(round(2.675))
print(5**3)
print(5//3)

tester = False
topelt = True

if 5+1==6:
    print(topelt)

#Küsime kasutajalt mingi värvi, kui see värv on sinine siis, näita 1
    #Kui see värv on punane, näita 2
        #Kui see värv on must, näita 3
            #Kui see värv on tundmatu, ei tee midagi.

#Kasutaja sisetab mingi nime.
nimi = "testeradgasdg"

print(len(nimi))
if len(nimi)>8:
    print("Liiga pikk")
if len(nimi)<20:
    print("Liiga pikk")
elif len(nimi)>3:
    print("Toene!")
else:
    print("Nojah")
    
if 2==3 and 2==2:
    print("test1")
elif 2==4:
    print("test2")
else:
    print("Nojah")
if 3>2: print("shorthand")

if 3==4 or 4==4 :
    print("on olemas")

if 4==4:
    if 5==4:
        print("on olemas nested if")

#Kasutaja sisestab arvu, meie vastame talle kas tegemist on paarisarvu või paaritu arvuga.
#IF MUUTUJA%2==0

#Liigaasta
#Kirjuta programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta.
#(Aasta on liigaasta, kui tema number jaguneb neljaga, välja arvatud need aasta, mille number jaguneb
# sajaga, kuid ei jagu neljasajaga)

#100,    400
#4



    
    
'''
displayList = []
tuhiList = []
mingiList = ["esimene", "teine"]
for x in mingiList[0]:
    tuhiList.append(x)
print(tuhiList)
for x in range(len(tuhiList)):
    displayList.append("_")
print(displayList)