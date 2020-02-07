#while
#for 

index=100
teineIndex=10
#print(index)

while index<=10:
    print(teineIndex)
    index+=1
    teineIndex+=100
    if index==5:
        print(index)
        continue
else:
    print("Condition is False")

fruits=["apple","banana","cherry"]    

for x in fruits:
    pass

for x in range(2,60,3):
    print(x)
else:
    print("Finished!")

for x in range(11):
    for x in range(11):
        print(x)
        

print(x)
#Anname ette mingi listi objekte
#kasutaja sisestab mingi elemendi seal listi
#for x in range(LISTIPIKKUS):
#   LIST[INDEX]
#print(LIST[ELEMENT])
#mitmes see listis on
#Vaja läheb 2 loopi, üks listi näitamiseks, teine selle otsimiseks.
#listinimi.index(ELEMENT)

testList=["Audi","BMW", "Mustang"]
for x in testList:#Prindime listi välja
    print(x)
valik=input("Millist marki soovite?")#Küsime millist marki soovitakse
for x in testList:#Käime listi läbi
    if x==valik:#Kui elemendi väärtus on vastav valikule
        vastus=testList.index(valik)#Võtame ta järjekorranumbri
        print(vastus)