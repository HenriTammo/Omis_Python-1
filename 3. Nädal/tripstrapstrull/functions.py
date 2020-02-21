def joonista(laud):
    print(laud[7] + "|" + laud[8] + "|" + laud[9])
    print(laud[4] + "|" + laud[5] + "|" + laud[6])
    print(laud[1] + "|" + laud[2] + "|" + laud[3])

def teeKaik(laud, kaik, kelle):
    if kaik < 10:
        laud[kaik] = kelle
