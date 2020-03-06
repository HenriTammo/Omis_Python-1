# Omis Python
Pythoni ja programmeerimise algkursus.
<br></br>
<a href="https://www.omis.ee/course/python-2503-3004-40-kr_eesti/">Koduleht</a>
<br></br>
Õppejõud: Kristjan Veensalu
<br></br>
Email: kristjan.veensalu@gmail.com
<br></br>

<hr></hr>
Kasulikke linke:
<ul>
	Python ajalugu ja sissejuhatus
	<li>http://www.cs.tlu.ee/~inga/progbaas/Materjalid/Python_sissejuhatus_2019.pdf</li>
	Python õpetused/süntaks
	<li>https://www.w3schools.com/python/default.asp</li>
	Sisendi ja väljundi kohta
	<li>http://www.cs.tlu.ee/~inga/progbaas/Materjalid/Python_sisend_valjund_2019.pdf</li>
	Andmetüüpide kohta
	<li>http://www.cs.tlu.ee/~inga/progbaas/Materjalid/Python_muutujad_2019.pdf</li>
	If lausete kohta
	<li>https://progeopik.cs.ut.ee/03_liitlaused.html</li>
	For ja While kordused
	<li>https://www.w3schools.com/python/python_while_loops.asp</li>
	<li>https://www.w3schools.com/python/python_for_loops.asp</li>
	Funktsioonid
	<li>https://www.w3schools.com/python/python_functions.asp</li>
	DateTime
	<li>https://www.w3schools.com/python/python_datetime.asp</li>
	Üldine dokumentatsioon
	<li>https://www.python.org/doc/</li>
</ul>
<hr></hr>
Kodutööd:
<br></br>
<ul>
	<li>Eesmärk - Mis te teha tahtsite?</li>
	<li>Tehnoloogia - Millega te tegite?</li>
	<li>Kirjeldus protsessist - Kuidas te tegite?</li>
	<li>Tulemus - Mis ta teeb?</li>
<hr></hr>

![Pilt pythoni koodist](/assets/pilt.png)

Vigade otsimine: 
Esimene eesmärk seoses vigade otsimisega võiks olla programmi käivitumine esimesel katsel, st programmi koodist on likvideeritud 
esmased pisivead ja näpukad (süntaksivead). Selleks loe programm läbi ning veendu, et:

- ühelgi muutujal ei ole nimeks võtmesõna
- juhtlause lõpus (if, while, for, def) on koolon :
- treppimine on järjekindel. Soovitav on kasutada ainult tühikuid või ainult tab-e. Taanded olgu ühe suurusega.
- kõigil stringidel on alguse ja lõpusümbol (just viimane kipub ära jääma)
- kõigil sulgudel on paarilised
- võrdlemine toimub ==-ga ja mitte =-ga ja omistamine =-ga ja mitte ==-ga

Kui loetletud vigade leidmine enne programmi käivitamist juba õnnestub, võiks kontrolli laiendada. 
Järgnevalt valik küsimusi, mida soovitatakse testijal küsida programmikoodi lugemise käigus 
(muide, seda tegevust kutsutakse ametlikult staatiliseks testimiseks):

1. Vaata üle muutujad ja nende nimed:
- Kas proovitakse kasutada muutuja väärtust enne muutuja tekkimist, st kas esineb mõni algväärtustamata 
muutuja omistuslause paremal poolel, avaldises, väljatrükis?
- Kas oled eksinud mõne muutujanime kirjutamisel? Või oled ehk programmis ühes kohas kirjutanud muutuja 
suure algustähega, aga teises kohas sama muutuja väikese algustähega?

2. Vaata üle keelesõnad:
- Nad peavad IDLE redaktoris olema teist värvi - siis on õigesti kirjutatud. Kui ei ole, otsi sõnast viga.
- Vaata ka üle, milliseid funktsioone kasutad - äkki on tegemist mõne funktsiooniga, mille kasutamiseks 
eraldi mooduli poole pöörduda tulab (import math) jms?

3. Avaldised ja andmetüübid - vaata üle nii aritmeetikaavaldised kui ka loogikaavaldised:
- Kas ühte lausesse või avaldisse on kokku sattunud sobivad andmetüübid? Arvude ja stringide koos kasutamine 
ei lõppe enamasti hästi. Arvuti ei saa arvutada "porgand" + 3.
- Kas kõik arvutamisel kasutatavad muutujad on peale sisestamist ka arvuks teisendatud?
- Kas sealjuures on kasutatud andme iseloomule sobivalt täisarvu (int()) või ujukomaarvu (float())?
- Kas tehete järjekord on õigesti määratud ja kas kasutatakse selleks piisavalt sulge?
- Kas võib tekkida jagamist nulliga?

4. Võrdlemised - vaata üle loogikaavaldistes olevad võrdlustehted:
- Kas võrreldakse erinevaid asju: näiteks teksti ja numbrit? Arvuti ei oska otsustada, kas "porgand" > 3
- Kas algoritm on võrdlustehetesse õigesti tõlgitud? Näiteks märkide < ja <= kasutamise tulemus võib olla erinev.
- Kas võrdlustehete prioriteedid on määratud õigesti?
- Kas võrreldakse komakohaga muutujat konkreetse arvuga ja sealjuurel võrdusmärgiga (==)? 
Ujukomaarvud ei pruugi olla täpsed ja seetõttu on nad ebasobivad võrdusmärgiga võrdlemiseks.

5. Vead programmi struktuuris - vaata üle kõik keelekonstruktsioonid (tsüklid, valikud)
- Kas taanded määravad õigesti planeeritud tsükli- ja valikulausete piirid?
- Kas tsüklid on sisuliselt õigesti planeeritud - kas while-tsükli sisu ja loogikaavaldis
on kooskõlas ning avaldise väärtus saab muutuda vääraks (False)? Kas loogikaavaldises kasutatavate muutujate 
väärtused tsükli sees muutuvad?
- Kas loogikaavaldis tsükli alguses esimesel kordusel saab olla tõene (True)? Kas tsükkel üldse käivitub?

Jõudu oma koodi lugemiseks ja iseseisvaks vigade leidmiseks!

<hr></hr>
Osalejate github:
<ol>
	<li><a href="https://github.com/priitsepp/python">Priit Sepp</a></li>
	<li><a href="https://github.com/maarjaryytel/python">Maarja Rüütel</a></li>
	<li><a href="#">Oona Elise Marie Luik</a></li>
</ol>
