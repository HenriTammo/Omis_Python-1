import os
if os.path.exists("teginfaili.txt"):
    print("Olemas fail")
    os.remove("teginfaili.txt")
    print("Fail kustutatud")
else:
    print("Faili ei ole\n")


os.rmdir("teginkausta")
#os.chdir("./teginkausta/")










#f = open("demo.txt", "r")
#print(f.read(20))
#print(f.readline())
#print(f.readline())
#print(f.readline())

#tekstiSisu = f.read(100)
#print(tekstiSisu)
'''testiList = []

for x in f:
    testiList.append(x)
print(testiList)

f.close()
'''
#x = open("teginfaili.txt", "x")
'''f = open("teginfaili.txt", "a")
f.write("LISASIN SELLE JUURDE FAILI!!!!")
f.close'''
'''f = open("teginfaili.txt", "w")
f.write("KIRJUTASIN ÜLE!")
f.close'''

