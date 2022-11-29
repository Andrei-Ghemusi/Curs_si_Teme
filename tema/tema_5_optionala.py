
print('-----EXERCITIUL 1--------')
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
luni_an = {'Ianuarie': 31, 'Februarie': 28, 'Martie': 31, 'Aprilie': 30, 'Mai': 31, 'Iunie': 30, 'Iulie': 31,
           'August': 31, 'Septembrie': 30, 'Octombrie': 31, 'Noiembrie': 30, 'Decembrie':31}

def zile_luna_din_an(luna):
    for key, value in luni_an.items():
        if luna == key:
            return value

print(zile_luna_din_an('Ianuarie'))



print('-----EXERCITIUL 2--------')
# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

def calculator(nr1, nr2):
    suma = nr1 + nr2
    diferenta = nr1 -nr2
    inmultirea = nr1*nr2
    impartirea = nr1/nr2
    return suma, diferenta, inmultirea, impartirea

a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


print('-----EXERCITIUL 3--------')
# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]

def numaratoare_in_dict(lista):
    dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for i in dict.keys():
        for j in lista:
            if i == j:
                dict[i] = dict[i] +1
    return dict

print(numaratoare_in_dict(lista))




print('-----EXERCITIUL 4--------')
# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def functie_trei_numere(nr1, nr2, nr3):
    numar_maxim = max(nr1, nr2, nr3)
    return numar_maxim

print(functie_trei_numere(2,10,12))



print('-----EXERCITIUL 5--------')
# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

def suma_tuturor_numerelor(nr2):
    total = sum(range(nr2+1))
    return total

print(suma_tuturor_numerelor(10))


# def functie(nr2):
#     suma = 0
#     i = 0
#     while i <=nr2:
#         suma +=i
#         i +=1
#     return suma
#
# print(functie(10))
# varianta de la lucru in echipa
