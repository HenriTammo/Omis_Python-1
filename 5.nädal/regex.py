muutuja = "Arizona Coyotes3Montreal Canadians220,7892:32"
sygavus = 0
skoorid = []
skooriKombinatsioon = " "
for x in muutuja:
    if x.isdigit():
        sygavus=sygavus+1
        if sygavus==1:
            skooriKombinatsioon = x
        if sygavus==2:
            skooriKombinatsioon = skooriKombinatsioon+"-"+x
            skoorid.append(skooriKombinatsioon)
            print(x)           

print(skoorid)

for x in list:
    if "OT" in x:
        otList.append("OT")
    elif "SO" in x:
        otList.append("SO")
    else: 
        otList.append("No overtime")


listAwat=[]
listHome = []

for y in tuhilist:
    for x in tiimid:
        if x in y[0:21]:
            listHome.append(y)
        if x in y[-21:]:
            listAwat.append(y)

away team
home team
skoorid
overtime

loplikList = []


loplikList.append(htList[0])
loplikList.append(awayteam[0])
loplikList.append(overtime[0])
loplikList.append(skoorid[0])
print(loplikList)

'''for x in range(len(overtime)):
    loplikList.append(hometeam[x])
    loplikList.append(listAwat[x])
    loplikList.append(overtime[x])
    loplikList.append(skoorid[x])
for x in range(len(loplikList))
    print(loplikList[x])'''
