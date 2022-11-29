# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
print('-------FOR----------')
for masina in range(len(masini)):
    print(f'Mașina mea preferată este {masini[masina]}')

print('------FOR EACH----------')
for masina in masini:
    print(f'Masina mea preferata este {masina}')

print('------WHILE------------')
masina = 0
while masina<len(masini):
    print(f'Masina mea preferata este {masini[masina]}')
    masina+=1


print('------EXERCITIUL 2------')
# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.
'''
for masina in range(len(masini)):
    if masina == 0:
        continue
    if masina == len(masini)-1:
        continue
    masini[masina] = masini[masina].upper()
else:print(masini)
'''
# am oprit codul aici deoarece schimba toata lista dupa


print('-----EXERCITIUL 3 ---------')
# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
for masina_noua in masini:
    if masina_noua == 'Mercedes':
        print('Am găsit mașina dorită de dvs')
        break
    else: print(f'Am găsit mașina {masina_noua}. Mai căutam')


print('------EXERCITIUL 4 ---------')
# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

for masina_bogata in masini:
    if masina_bogata == 'Trabant' or masina_bogata == 'Lăstun':
        continue
    print(f'S-ar putea să vă placă mașina {masina_bogata}')


print('-----EXERCITIUL 5-----')
# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.

masini_vechi = []
for car in masini:
    if car == 'Lăstun':
        masini_vechi.append('Lăstun')
    if car == 'Trabant':
        masini_vechi.append('Trabant')
masini[masini.index('Trabant')] = 'Tesla'
masini[masini.index('Lăstun')] = 'Tesla'
print(f'Modele vechi {masini_vechi}')
print(f'Modele noi {masini}')

#SAU ASA
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
old_cars = []
for j in range(len(cars)):
    if cars[j] == 'Trabant':
        cars[j] = 'Tesla'
        old_cars.append('Trabant')
    if cars[j] == 'Lăstun':
        cars[j] = 'Tesla'
        old_cars.append('Lăstun')
print(f'Modele vechi {old_cars}')
print(f'Modele noi {cars}')


print('-----EXERCITIUL 6------')
# 6. Având dict:
# pret_masini = {'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină x
# ● Iterează prin listă.
pret_masini = {'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
for a in pret_masini.keys():
    if pret_masini[a] <= 15000:
        print(f'Pentru un buget de sub 15000 euro puteți alege mașină {a}')


print('-----EXERCITIUL 7------')
# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
aparente = 0
for k in numere:
    if k == 3:
        aparente +=1

print(f'Numarul 3 apare de {aparente} ori.')


print('------EXERCITIUL 8------')
# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
suma = 0
for l in numere:
    suma +=l
print(f'Suma este {suma}')


print('------EXERCITIUL 9------')
# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
max_num = 0
for b in numere:
    if b > max_num:
        max_num = b
print(f'Cel mai mare numar din lista este {max_num}.')


print('------EXERCITIUL 10------')
# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.
for c in range(len(numere)):
    numere[c] = -numere[c]
print(numere)










