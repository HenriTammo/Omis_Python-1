stopper = True
sygavus = 0
def recursive(x):
    while stopper:
        if x<1000:
            print(x)
            x=x+12
            recursive(x)

recursive(sygavus)

#Paneme kokku rekursiivse funktsiooni, mis edastab meile infot 12 kaupa.


def faktoriaal(x):
    if x == 1:
        return 1
    else:
        return (x * faktoriaal(x-1))

number = 10
print("Numbri ", number, "\nfaktoriaal on ", faktoriaal(number))



#Koosta programm mis küsib kasutajalt kas ta tahab kolmnurga, ruudu või ristküliku pindala teada.
#Koosta kolm funktsiooni, mis kutsutakse vastavalt kasutaja sisestusele ja täidavad selle ülesande.
#Jooksutame neid väljaspool visualcode