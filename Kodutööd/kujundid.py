from kujundite_funktsioonid import *

valik=int(input("Tee oma valik, sisesta valitud kujundi number: \n1- ruut\n2- ristkülik\n3- kolmnurk\n4- trapets\n5- kuup\n6- risttahukas\n7- silinder\n8- püramiid\n"))

if valik == 1:
    korduvValik=int(input("\nMille arvutamist soovid? Sisesta soovitud number: \n1- pindala\n2- ümbermõõt\n"))
    if korduvValik == 1:
        print("\nRuudu pindala on:", round(ruudu_funktsioon_pindala(), 2),"cm2.")        
    else:
        print("\nRuudu ümbermõõt on:",ruudu_funktsioon_ymbermoot(),"cm.")

if valik == 2:
    korduvValik=int(input("\nMille arvutamist soovid? Sisesta soovitud number: \n1- pindala\n2- ümbermõõt\n"))
    if korduvValik == 1:
        print("\nRistküliku pindala on:", round(ristkyliku_funktsioon_pindala(), 2),"cm2.")
    else:
        print("\nRistküliku ümbermõõt on:", round(ristkyliku_funktsioon_ymbermoot(), 2),"cm.")
    
if valik == 3:
    korduvValik=int(input("\nMille arvutamist soovid? Sisesta soovitud number: \n1- pindala\n2- ümbermõõt\n"))
    if korduvValik == 1:
        print("\nKolmnurga pindala on:", round(kolmnurga_funktsioon_pindala(), 2), "cm2.")
    else:
        print("\nKolmnurga ümbermõõt on:", round(kolmnurga_funktsioon_ymbermoot(), 2), "cm.")

if valik == 4:
    korduvValik=int(input("\nMille arvutamist soovid? Sisesta soovitud number: \n1- pindala\n2- ümbermõõt\n"))
    if korduvValik == 1:
        print("\nTrapetsi pindala on:", round(trapetsi_funktsioon_pindala(), 2),"cm2.")
    else:
        print("\nTrapetsi ümbermõõt on:", round(trapetsi_funktsioon_ymbermoot(), 2),"cm.")

if valik == 5:
    korduvValik=int(input("\nMille arvutamist soovid? Sisesta soovitud number: \n1- pindala\n2- ümbermõõt\n3- ruumala\n"))
    if korduvValik == 1:
        print ("\nKuubi pindala on:", round(kuubi_funktsioon_pindala(), 2), "cm2.")
    if korduvValik == 2:
        print("\nKuubi ümbermõõt on:", round(kuubi_funktsioon_ymbermoot(), 2), "cm.")
    if korduvValik == 3:
        print("\nKuubi ruumala on:", round(kuubi_funktsioon_ruumala(), 2), "cm3.")

if valik == 6:
    korduvValik=int(input("\nMille arvutamist soovid? Sisesta soovitud number: \n1- pindala\n2- ruumala\n"))
    if korduvValik == 1:
        print("\nRisttahuka pindala on:", round(risttahuka_funktsioon_pindala(), 2), "cm2.")
    else:
        print("\nRisttahuka ruumala on:", round(risttahuka_funktsioon_ruumala(), 2), "cm3.")
    
if valik == 7:
    korduvValik=int(input("\nMille arvutamist soovid? Sisesta soovitud number: \n1- pindala\n2- ruumala\n"))
    if korduvValik == 1:
        print("\nSilindri pindala on:", round(silindri_funktsioon_pindala(), 2), "m2.")
    else:
        print("\nSilindri ruumala on:", round(silindri_funktsioon_ruumala(), 2), "m3.")

if valik == 8:
    korduvValik=int(input("\nMille arvutamist soovid? Sisesta soovitud number: \n1- pindala\n2- ruumala\n"))
    if korduvValik == 1:
        print("\nPüramiidi pindala on:", round(pyramiidi_funktsioon_pindala(), 2),"cm2.")
    else:
        print("\nPüramiidi ruumala on:", round(pyramiidi_funktsioon_ruumala(), 2), "cm3.")

input()