# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
#
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
#
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
#
# Google search hint
# “how to check if item îs în list python”

'''
Am schimbat numele unor liste date in cerinta, si am pus Jucatorul x si y sa fie citit de la tastatura,
adica input.
Sper sa fie ok asa :)
'''


teren = ['Popa', 'Hagi', 'Mbappe', 'Benzema', 'Chivu']
print(f'Aici sunt jucatorii din teren: {(", ".join(teren))}')
rezerva = ['Dica', 'Maradona', 'Haaland']
jucator_din_teren = input("Numeste jucatorul din teren care sa fie schimbat: ")
print(f'Aici sunt jucatorii din rezerva: {(", ".join(rezerva))}')
jucator_din_rezerva = input("Numeste jucatorul din rezerva care sa fie adaugat: ")
schimbari_max = 3

if jucator_din_teren in teren and (schimbari_max > 0):
    schimbari_max -=1
    teren.remove(jucator_din_teren)
    if jucator_din_rezerva in rezerva:
        teren.append(jucator_din_rezerva)
        print(f'A iesit {jucator_din_teren}, a fost adaugat {jucator_din_rezerva}, mai avem {schimbari_max} '
              f'schimbari.')
    else:
        print(f'Jucatorul {jucator_din_rezerva} nu e in rezerva, mai avem {schimbari_max} schimbari')
else:
    print(
        f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_din_teren} nu e în teren, mai avem '
        f'{schimbari_max} schimbari')