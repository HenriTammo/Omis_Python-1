from hoidja import my_function #from "FAILINIMI" import "FUNKTSIOONI NIMI"

my_function()

def korrutameKahega(sisendInfo):
    print(sisendInfo*2)

def kordameTagasi(sona,korduskord):
    for x in range(korduskord):
        print(sona)

def arvutid(*arvuteid):
    print(arvuteid)
    print("Kolmas arvuti on " + arvuteid[2])

arvutid("Samsung", "Apple", "Asus")



korrutis=int(input("Sisesta number - "))
korrutameKahega(korrutis)

kordameTagasi("kala", 10)

my_function()

#Koostage oma funktsioon, et lugeda kümneni.
#Koostage oma funktsioon, mis kordab ennast 5 korda ja lisab iga kord kasutaja vastuse listi.
#Koostage oma funktsioon, mis küsib ilma kohta kolm asja ja lisab need sõnastikku. Seejärel tagastab need.