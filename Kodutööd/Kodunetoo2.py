from kolmpind import kolmnurga_pind
from kolmpind import kolmnurga_ymber
from ruutpind import ruudu_pind
from ruutpind import ruudu_ymber
from ristpind import rist_pind
from ristpind import rist_ymber
from ringpind import ring_pind
from ringpind import ring_ymber
from kuuppind import kuup_pind
from kuuppind import kuup_ruumala
from pyramiidpind import pyramiid_pind
from pyramiidpind import pyramiid_ruumala
from silinderpind import silinder_pind
from silinderpind import silinder_ruumala
from risttahukaspind import risttahukas_pind
from risttahukaspind import risttahukas_ruumala


tehe = input("Tee valik numbriga 1)Kolmnurga ümbermõõt 2)Kolmnurga pindala 3)Ruudu ümbermõõt 4)Ruudu pindala \n5)Ristküliku pindala 6)Ristküliku ümbermõõt 7)Ringi pindala 8)Ringi ümbemõõt 9)Kuubi pindala \n10)Kuubi ruumala 11)Püramiidi pindala 12)Püramiidi ruumala 13)Silindri pindala \n14)Silindri ruumala 15)Risttahuka pindala 16)Risttahuka ruumala ? -")
print(tehe)
if tehe=="1":
    print(kolmnurga_ymber())
if tehe=="2":
    print(kolmnurga_pind())
if tehe=="3":
    print(ruudu_ymber())
if tehe=="4":
    print(ruudu_pind())
if tehe=="5":
    print(rist_pind())
if tehe=="6":
    print(rist_ymber())
if tehe=="7":
    print(ring_pind())
if tehe=="8":
    print(ring_ymber())
if tehe=="9":
    print(kuup_pind())
if tehe=="10":
    print(kuup_ruumala())
if tehe=="11":
    print(pyramiid_pind())
if tehe=="12":
    print(pyramiid_ruumala())
if tehe=="13":
    print(silinder_pind())
if tehe=="14":
    print(silinder_ruumala())
if tehe=="15":
    print(risttahukas_pind())
if tehe=="16":
    print(risttahukas_ruumala())


input()