# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = str(int(input("Introduceti un numar pentru x: ")))
if 4<=len(x):
    print(f'{x} are minim 4 cifre')
else:
    print(f'{x} nu are minim 4 cifre')

# 2.Verifică dacă x are exact 6 cifre.
if len(x) == 6: # prima data l-am facut cu assert dar trebuia mereu pus x cu 6 cifre, altfel dadea eroare
    print(f'{x} are 6 cifre')
else:
    print(f'{x} nu are 6 cifre')

# 3.Verifică dacă x este număr par sau impar (x e int).
if int(x)%2 == 0:
    print(f'{x} e numar par')
else:
    print(f'{x} e numar impar')

# 4.x, y, z (int)
# Afișează care este cel mai mare dintre ele
y = int(input("Introduceti un numar pentru y: "))
z = int(input("Introduceti un numar pentru z: "))

if int(x)>(y and z):
    print(f'{x} e cel mai mare')
elif y >(x and z):
    print(f'{y} e cel mai mare')
else:
    print(f'{z} e cel mai mare')

# 5. X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
if int(x)+y+z==180:
    print("Triunghiul este valid")
else:
    print('Triunghiul nu e valid')

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
a = int(input("(Ex: 6) Introduceti numar pentru a: ")) # am folosit a, pentru ca x am folosit si mai devreme
sea = 'Coral is either the stupidest animal or the smartest rock'
print(f'Stringul sea fara ultimele {a} caractere este {sea[:-a]}')

# 7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
new_sea = sea[4:-5]
print(f'Stringul nou new_sea este {new_sea}')

# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '
sea = 'Coral is either the stupidest animal or the smartest rock'
rock_index = sea.index('rock')
print(rock_index)
print(sea[:rock_index])

# 9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat

string_nou = input("(Ex: 9) Introdu un string: ")
if string_nou[0:1] == string_nou[-1:]:
    print("Sunt aceleasi caractere")
else:
    print("Nu sunt aceleasi caractere")

# 10. Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)
exe = '0123456789'
lista_exe = [0,1,2,3,4,5,6,7,8,9]
for nr_par in lista_exe:
    if nr_par%2==0:
        print(nr_par, end="")

add_space = ""
print(add_space) #n-am stiut cum sa le separ si am folosit o variabila

for nr_impar in lista_exe:
    if nr_impar%2!=0:
        print(nr_impar,end="")