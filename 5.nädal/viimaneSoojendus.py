#Kirjutage programm mis kontrollib kas sisestatud arv on suurem kasutaja
#sisestatud listis olevast arvudest.
#Kasutaja saab vastuseks Suurem või Väiksem













numberList = []
stopper = True
while stopper:
    kysimus = input("Soovid sisestada listi numbri? [J/E] ")
    if kysimus == "J":
        sisendArv = int(input("Sisesta listiarv: "))
        numberList.append(sisendArv)
    if kysimus == "E":
        print(numberList)
        stopper = False
sisendKontrolliks = int(input("Sisesta oma arv mida kontrollida: "))
for x in numberList:
    if x<sisendKontrolliks:
        print("Suurem")
    else:
        print("Väiksem")