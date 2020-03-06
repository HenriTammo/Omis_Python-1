
#Moodusta ekraanile tärnidest ruut. 
#Tärnide arvu ruudu külgede jaoks sisestab kasutaja. 
#Näiteks kui ruudu külg on 5, siis ekraanile ilmub:

#*****
#*****
#*****
#*****
#*****
#sisestus = int(input("Mitu korda? - "))
#muutuja = 1
#Nested loop

for y in range(1,11):
    for x in range(1,11):
        print(x*y, end=" ")
    #muutuja = muutuja + sisestus
    print()
