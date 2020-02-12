import random as x

suvaline = x.randint(1,20);
print(suvaline);
#test2

#Üks mängija mõtleb arvu etteantud piirides ja teine katsub seda ära arvata. 
#Meie ülesandes - arvuti mõtleb arvu ja inimene hakkab arvama. Arvuti vastab igale arvamisele 
#ja täpsustab, kas pakutud arv on liiga suur või liiga väike.

mangkaib = True

while mangkaib:
    mangkaib = False
#
#Funktsioon randint() paikneb moodulis random, 
#mis tuleb importida ning funktsiooni käivitamisel kirjutada nime ette random.