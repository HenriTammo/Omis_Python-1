#Koostame väikese kivi-paber-käärid mängu.
#Kasutame funktsiooni ja listi.
import random
vordleja = True
baas = ["Kivi", "Paber", "Käärid"]

def mang():
    otsija = random.randint(0,2)
    kasutajaValik = input("Kivi,Paber või Käärid? X TO STOP - ")
    arvutiValik = baas[otsija]
    if arvutiValik == "Käärid" and kasutajaValik == "Kivi":
        print("Teie võit!")
        print(arvutiValik)
        print(kasutajaValik)
    if arvutiValik == "Paber" and kasutajaValik == "Käärid":
        print("Teie võit!")
        print(arvutiValik)
        print(kasutajaValik)
    if arvutiValik == "Kivi" and kasutajaValik == "Paber":
        print("Teie võit!")
        print(arvutiValik)
        print(kasutajaValik)
    if arvutiValik == "Käärid" and kasutajaValik == "Paber":
        print("Arvuti võit!")
        print(arvutiValik)
        print(kasutajaValik)
    if arvutiValik == "Kivi" and kasutajaValik == "Käärid":
        print("Arvuti võit!")
        print(arvutiValik)
        print(kasutajaValik)
    if arvutiValik == "Paber" and kasutajaValik == "Kivis":
        print("Arvuti võit!")
        print(arvutiValik)
        print(kasutajaValik)
    if arvutiValik == kasutajaValik:
        print("VIIK!")
        print(arvutiValik)
        print(kasutajaValik)
    return(kasutajaValik)

while vordleja:
    if mang() == "X":
        vordleja = False

