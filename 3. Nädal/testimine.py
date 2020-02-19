try:
    print("fasdfasd")
except NameError:
    print("Muutujat ei ole olemas!")
    mingiArv = 10
    print(mingiArv)
except:
    print("On tekkinud mingi muu viga.")
finally:
    print("Nüüd saan teha seda.")

try:
    f = open("testimine.py")
    f.write(
        "Ei saa kirjutada"
    )
except:
    print("Faili avamisel või kirjutamisel tekkis probleem")
finally:
    f.close()

'''
number = 20
if number > 10:
    raise Exception("Sorry see number ei sobi.")
'''
tekst = "tervist"

if not type(tekst) is int:
    raise TypeError("Ainult numbrid lubatud")

#Kivi paber käärid
#123123
#[2312312,m232,123]