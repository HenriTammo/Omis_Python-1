import sys
from time import sleep
mangija = "A"
arvuti = "B"
ManguLaud = ["NULL"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
ManguLaudGuide = ["NULL","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","11","12","13","14","15","16","17","18","19","20"]
mangOnMangimata = True
plaadiSygavus = 0
eelmineKaik = 0
kaiguList=[1]
sygavus2 = 0

#1,3,4,9,8,14,12,13,17

def joonista(laud): #Funktsioon mis joonistab laua
	print(laud[17] + ' | ' + laud[18] + ' | ' + laud[19] + ' | ' + laud[20])	
	print(laud[13] + ' | ' + laud[14] + ' | ' + laud[15] + ' | ' + laud[16])	
	print(laud[9] + ' | ' + laud[10] + ' | ' + laud[11] + ' | ' + laud[12])
	print(laud[5] + ' | ' + laud[6] + ' | ' + laud[7] + ' | ' + laud[8])
	print(laud[1] + ' | ' + laud[2] + ' | ' + laud[3] + ' | ' + laud[4])

def voidukontroll(laud, mangija): #Kõik meetodid kuidas võita mäng
	return ((laud[1] == mangija and laud[2] == mangija and laud[3] == mangija and laud[4] == mangija) or #Horisontaal
	(laud[5] == mangija and laud[6] == mangija and laud[7] == mangija and laud[8] == mangija) or 
	(laud[9] == mangija and laud[10] == mangija and laud[11] == mangija and laud[12] == mangija) or 
	(laud[13] == mangija and laud[14] == mangija and laud[15] == mangija and laud[16] == mangija) or
	(laud[17] == mangija and laud[18] == mangija and laud[19] == mangija and laud[20] == mangija) or 
	(laud[1] == mangija and laud[5] == mangija and laud[9] == mangija and laud[13] == mangija) or  #Püsti
	(laud[2] == mangija and laud[6] == mangija and laud[10] == mangija and laud[14] == mangija) or
	(laud[3] == mangija and laud[7] == mangija and laud[11] == mangija and laud[15] == mangija) or 
	(laud[4] == mangija and laud[8] == mangija and laud[12] == mangija and laud[16] == mangija) or
	(laud[5] == mangija and laud[9] == mangija and laud[13] == mangija and laud[17] == mangija) or  #Püsti V2
	(laud[6] == mangija and laud[10] == mangija and laud[14] == mangija and laud[18] == mangija) or
	(laud[7] == mangija and laud[11] == mangija and laud[15] == mangija and laud[19] == mangija) or 
	(laud[8] == mangija and laud[12] == mangija and laud[16] == mangija and laud[20] == mangija) or
	(laud[1] == mangija and laud[6] == mangija and laud[11] == mangija and laud[16] == mangija) or #Diagonaal
	(laud[4] == mangija and laud[7] == mangija and laud[10] == mangija and laud[13] == mangija)) 


def kohaKontroll(laud, kaik):	
	return laud[kaik] == " "
def ArvutiTehtudKaik(laud, kaik):
	return laud[kaik] == "B"

def kasAllon(laud, kaik, plaadiSygavus): 
	if kaik < 5 and kohaKontroll(laud, kaik):
		return True
	else:
		kaik = kaik - 4
		if kaik >=1 and kohaKontroll(laud, kaik) == False:
			return True
		else:
			return False

def teekaik(laud, mangija, kaik): 
	laud[kaik] = mangija

def AnnaKoopia(laud):	
	Lauakoopia = []
	for i in laud:
		Lauakoopia.append(i)
	return Lauakoopia

def kaiEsimesse(laud):	
	for i in range(1, 20):
		if kohaKontroll(laud, i):
			if i>=4:
				if kasAllon (laud, i, plaadiSygavus):
					return i
			else:
				return i


def mangijaKaik(laud):	
	kaik = ' '
	print('Tee oma käik')
	kaik = input()
	return int(kaik)

def arvutiKaik(laud):	
	koopia = AnnaKoopia(laud)
	for i in range(1, 20):	#Hakkab lauda kontrollima
		koopia = AnnaKoopia(laud)
		if kohaKontroll(koopia, i):
			teekaik(koopia, arvuti, i)
		if voidukontroll(koopia, arvuti):	#Otsib kas on võimalust võita
			if kasAllon (koopia, i, plaadiSygavus):
				return i
	for i in range(1, 20):
		koopia = AnnaKoopia(laud)
		if kohaKontroll(koopia, i):
			teekaik(koopia, mangija, i)
			if voidukontroll(koopia, mangija):	#Otsib kas on vaja peatada mängija võitmast
				if kasAllon (koopia, i, plaadiSygavus):
					return i
	return recKontroll(laud, kaiguList, sygavus2)	#Kui ei ole kumbagi siis käib lähedale, et saada puntrasse, lihtsam võita



def recKontroll(laud, kaiguList, sygavus2):
	koopia = AnnaKoopia(laud)
	uusSygavus = sygavus2 + 1
	if uusSygavus > 5:
		return 0
	if uusSygavus == 1: 
		if kohaKontroll(koopia, kaiguList[-1]-uusSygavus):
			return int(kaiguList[-1]-uusSygavus)
		if kohaKontroll(koopia, kaiguList[-1]+uusSygavus):
			return int(kaiguList[-1]+uusSygavus)
	if uusSygavus == 2:
		if kohaKontroll(koopia, kaiguList[-1]+uusSygavus+1):
			return int(kaiguList[-1]+uusSygavus+1)
		if kohaKontroll(koopia, kaiguList[-1]+uusSygavus+2):
			return int(kaiguList[-1]+uusSygavus+2)
		if kohaKontroll(koopia, kaiguList[-1]+uusSygavus+3):
			return int(kaiguList[-1]+uusSygavus+3)
	else:
		return recKontroll(laud, kaiguList, uusSygavus)


# MÄNGUPROTSESS
while mangOnMangimata: 
	kellekaik = "mangija"
	start = True	
	sygavus = 0
	while start:
		if kellekaik == "mangija": 
			joonista(ManguLaud)
			joonista(ManguLaudGuide)
			kaik = mangijaKaik(ManguLaud)
			while kaik > 20 or kaik < 1:
				print("Numbrid 1-20 ainult, proovi uuesti") 
				kaik = mangijaKaik(ManguLaud)
			while kohaKontroll(ManguLaud,kaik) == False:
				print("Koht on võetud, proovi uuesti") 
				kaik = mangijaKaik(ManguLaud)
			while kasAllon(ManguLaud, kaik, plaadiSygavus) == False:
				print("All pole nuppu, mis seda toetaks")
				kaik = mangijaKaik(ManguLaud)
			if kohaKontroll(ManguLaud,kaik):
				teekaik(ManguLaud, mangija, kaik)
				joonista(ManguLaud)
			if voidukontroll(ManguLaud, mangija):
				print("------------")
				joonista(ManguLaud)
				print("Mängija võit")
				start = False
			else:
				sygavus = sygavus +1
				kellekaik = "arvuti"
				if sygavus == 20: #Laud on täis
					start = False

		else:
			kaik = arvutiKaik(ManguLaud) #Arvuti hakkab käima 
			kaiguList.append(kaik)
			sleep(1)
			print(recKontroll)
			teekaik(ManguLaud, arvuti,kaik)

			if voidukontroll(ManguLaud, arvuti):
				print("-----------")
				joonista(ManguLaud)
				print("Arvuti võit")
				start = False
			else:
				print("Arvuti käib...")
				sygavus = sygavus +1
				kellekaik = "mangija"
	if start == False:
		print("Mäng läbi!")
		break



"""
joonista(ManguLaud)
if voidukontroll(ManguLaud, mangija):
	print(True)
else:
	print(False)
print("testime käiku")
kaik = int(input())
kasAllon(ManguLaud, kaik, plaadiSygavus)
if kohaKontroll(ManguLaud, kaik) and kasAllon(ManguLaud, kaik, plaadiSygavus):
	print("TRUE")
else:
	print("FALSE") """

