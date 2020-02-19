def ruudu_funktsioon_pindala():
    ruuduKylg=float(input("\nSisesta ruudu külje pikkus (cm): "))
    ruuduPindala= ruuduKylg*ruuduKylg
    return round(ruuduPindala)

def ruudu_funktsioon_ymbermoot():
    ruuduKylg=float(input("\nSisesta ruudu külje pikkus (cm): "))
    ruuduYmbermoot= 4*ruuduKylg
    return round(ruuduYmbermoot)

def ristkyliku_funktsioon_pindala():
    ristkyliku_pikkus=float(input("\nSisesta ristküliku pikkus (cm): "))
    ristkyliku_laius=float(input("\nSisesta ristküliku laius (cm): "))
    ristkyliku_pindala=ristkyliku_pikkus*ristkyliku_laius
    return ristkyliku_pindala

def ristkyliku_funktsioon_ymbermoot():
    ristkyliku_pikkus=float(input("\nSisesta ristküliku pikkus (cm): "))
    ristkyliku_laius=float(input("\nSisesta ristküliku laius (cm): "))
    ristkyliku_ymbermoot= 2*(ristkyliku_pikkus + ristkyliku_laius)
    return round(ristkyliku_ymbermoot)

def kolmnurga_funktsioon_pindala():
    kolmnurga_alus=float(input("\nSisesta kolmnurga alus (cm): "))
    kolmnurga_korgus=float(input("\nSisesta kolmnurga kõrgus (cm): "))
    kolmnurga_pindala= kolmnurga_alus*kolmnurga_korgus/2
    return kolmnurga_pindala

def kolmnurga_funktsioon_ymbermoot():
    kolmnurga_kyljepikkus=float(input("\nSisesta kolmnurga 1. külg (cm): "))
    kolmnurga_kyljepikkus2=float(input("\nSisesta kolmnurga 2. külg (cm): "))
    kolmnurga_kyljepikkus3=float(input("\nSisesta kolmnurga 3. külg (cm): "))
    kolmnurga_ymbermoot= kolmnurga_kyljepikkus + kolmnurga_kyljepikkus2 + kolmnurga_kyljepikkus3
    return kolmnurga_ymbermoot

def trapetsi_funktsioon_pindala():
    trapetsi_alus=float(input("\nSisesta trapetsi 1. alus (cm): "))
    trapetsi_alus2=float(input("\nSisesta trapetsi 2. alus (cm): "))
    trapetsi_korgus=float(input("\nSisesta trapetsi kõrgus (cm): "))
    trapetsi_pindala= (trapetsi_alus + trapetsi_alus2) / 2 * trapetsi_korgus     
    return trapetsi_pindala

def trapetsi_funktsioon_ymbermoot():
    trapetsi_alus=float(input("\nSisesta trapetsi 1. alus (cm): "))
    trapetsi_alus2=float(input("\nSisesta trapetsi 2. alus (cm): "))
    trapetsi_haar=float(input("\nSisesta trapetsi 1. haar (cm): "))
    trapetsi_haar2=float(input("\nSisesta trapetsi 2. haar (cm): "))
    trapetsi_ymbermoot= trapetsi_alus+trapetsi_alus2+trapetsi_haar+trapetsi_haar2
    return trapetsi_ymbermoot

def kuubi_funktsioon_pindala():
    kuubi_serva_pikkus=float(input("\nSisesta kuubi serva pikkus (cm): "))
    kuubi_pindala= 6*(kuubi_serva_pikkus*kuubi_serva_pikkus)
    return kuubi_pindala
  
def kuubi_funktsioon_ymbermoot():
    kuubi_serva_pikkus=float(input("\nSisesta kuubi serva pikkus (cm): "))
    kuubi_ymbermoot= 12*kuubi_serva_pikkus
    return kuubi_ymbermoot

def kuubi_funktsioon_ruumala():
    kuubi_serva_pikkus=float(input("\nSisesta kuubi serva pikkus (cm): "))
    kuubi_ruumala= kuubi_serva_pikkus*kuubi_serva_pikkus*kuubi_serva_pikkus
    return kuubi_ruumala

def risttahuka_funktsioon_pindala():
    risttahuka_pikkus=float(input("\nSisesta risttahuka pikkus (cm): "))
    risttahuka_laius=float(input("\nSisesta risttahuka laius (cm): "))
    risttahuka_korgus=float(input("\nSisesta risttahuka kõrgus (cm): "))
    risttahuka_pindala= 2*((risttahuka_pikkus * risttahuka_laius) + (risttahuka_laius * risttahuka_korgus) + (risttahuka_pikkus * risttahuka_korgus))
    return risttahuka_pindala

def risttahuka_funktsioon_ruumala():
    risttahuka_pikkus=float(input("\nSisesta risttahuka pikkus (cm): "))
    risttahuks_laius=float(input("\nSisesta risttahuka laius (cm): "))
    risttahuka_korgus=float(input("\nSisesta risttahuka kõrgus (cm): "))
    risttahuka_ruumala= risttahuka_pikkus*risttahuks_laius*risttahuka_korgus
    return risttahuka_ruumala

def silindri_funktsioon_pindala():
    silindri_raadius=float(input("\nSisesta silindri raadius (cm): "))
    silindri_korgus=float(input("\nSisesta silindri kõrgus (cm): "))
    π=3.14159
    silindri_pindala=2 * π * silindri_raadius * (silindri_korgus + silindri_raadius)
    return silindri_pindala

def silindri_funktsioon_ruumala():
    silindri_raadius=float(input("\nSisesta silindri raadius (cm): "))
    silindri_korgus=float(input("\nSisesta silindri kõrgus (cm): "))
    π=3.14159
    silindri_ruumala= π * silindri_raadius * silindri_raadius * silindri_korgus
    return silindri_ruumala

def pyramiidi_funktsioon_pindala():
    pyramiidi_pohiserva_pikkus=float(input("\nSisesta püramiidi põhiserva pikkus (cm): "))
    pyramiidi_kyljetahu_korgus=float(input("\nSisesta püramiidi küljetahu kõrgus (cm): "))
    pyramiidi_pindala= 2* pyramiidi_pohiserva_pikkus * pyramiidi_kyljetahu_korgus + pyramiidi_pohiserva_pikkus * pyramiidi_pohiserva_pikkus
    return pyramiidi_pindala

def pyramiidi_funktsioon_ruumala():
    pyramiidi_pohiserva_pikkus=float(input("\nSisesta püramiidi põhiserva pikkus (cm): "))
    pyramiidi_korgus=float(input("\nSisesta püramiidi kõrgus (cm): "))
    pyramiidi_ruumala= (pyramiidi_pohiserva_pikkus * pyramiidi_pohiserva_pikkus * pyramiidi_korgus) / 3
    return pyramiidi_ruumala