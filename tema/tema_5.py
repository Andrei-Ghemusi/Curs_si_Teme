print('------EXERCITIUL 1------')
# 1.Funcție care să calculeze și să returneze suma a două numere
def calculeaza_suma_a_doua_numere(nr_1,nr_2):
    print(f'Suma a doua numere este {nr_1 + nr_2}')
calculeaza_suma_a_doua_numere(1,2)


print('------EXERCITIUL 2------')
# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def numar_par(nr):
    if (nr%2==0):
        print(True)
    else:
        print(False)

numar_par(1)


print('-----EXERCITIUL 3-------')
# 3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)
def numarul_complet_caractere(nume, prenume, nume_mijlociu):
    total = len(nume) + len(prenume) + len(nume_mijlociu)
    print(f'Numarul complet de caractere este {total}')

nume = 'Vasilescu'
prenume = 'Ion'
nume_mijlociu = 'Nane'
numarul_complet_caractere(nume, prenume, nume_mijlociu)


print('-----EXERCITIUL 4-------')
# 4. Funcție care returnează aria dreptunghiului
def aria_dreptunghi(lungimea,latimea):
    print(f'Aria dreptunghiului este {lungimea*latimea}')

aria_dreptunghi(5,2)


print('-----EXERCITIUL 5-------')
# 5. Funcție care returnează aria cercului
def aria_cercului(pi, raza):
    print(f'Aria cercului este {pi*(raza**2)}')

aria_cercului(3.14, 10)


print('-------EXERCITIUL 6-------')
# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
def caracterul_a(string):
    if 'a' in string:
        print(True)
    else:
        print(False)

caracterul_a('Margarina')


print('-------EXERCITIUL 7-------')
# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def nr_de_caractere(sentence):
    upper = 0
    for i in sentence:
        if i.isupper() == True:
            upper +=1
    print(f'Nr de caractere uppercase este {upper}')
    lower = 0
    for j in sentence:
        if j.islower() == True:
            lower +=1
    print(f'Nr de caractere lowercase este {lower}')

nr_de_caractere('Ariodjsf aAKJOAIojd')



print('-------EXERCITIUL 8-------')
# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive

def functia_primeste_si_returneaza(lista):
    comp = [i for i in lista if i>0]
    print(f'Numerele pozitive sunt {comp}')

numere = [0,1,2, -2, -3, -9, 102, 120]
functia_primeste_si_returneaza(numere)


print('-------EXERCITIUL 9-------')
# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def doua_numere(nr1, nr2):
    if nr1>nr2:
        print(f'{nr1} este mai mare decat al doilea nr {nr2}')
    elif nr1<nr2:
        print(f'Al doilea nr {nr2} este mai mare decat primul nr {nr1}')
    else:
        print('Numerele sunt egale')

doua_numere(1,2)


print('-------EXERCITIUL 10-------')
# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False

def nr_si_set_numere(nr,set):
        poate = False
        if nr in set:
            print(f'nu am adaugat numărul în set. Acesta există deja')
            return poate
        else:
            set.add(nr)
            poate = True
            print(f'am adaugat numărul nou în set')
            return poate

setul = {1,2,4,60,9,3}
print(nr_si_set_numere(5,setul))
