#1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# Cu if controlam unde 'curge' codul, daca if e True atunci codul acestuia se va executa, daca if e False atunci
# se va executa codul din else (in cazul in care nu avem elif).

#2. Verifică și afișează dacă x este număr natural sau nu.
x = int(input("Introduceti un numar pentru x: "))
if x > 0:
    print(f'(Ex: 2) {x} e numar natural')
else:
    print(f'(Ex: 2) {x} nu e numar natural')


# Aici am aflat daca y e nr natural, daca e int sau float depinzand de input.
# E ceva bonus ca sa se lungeasca mai mult codul :)
y = input("(Ex:Bonus) Introduceti un numar pentru y: ")
if '.' in y:
    y = float(y)
else:
    y = int(y)
if (y > 0) and (isinstance(y, float) == False):
    print(f'{y} e numar natural')
else:
    print(f'{y} nu e numar natural')

#3. Verifică și afișează dacă a este număr pozitiv, negativ sau neutru.
if x > 0:
    print(f"(Ex: 3) {x} numar pozitiv")
elif x <0:
    print(f"(Ex: 3) {x} este numar negativ")
else:
    print(f'(Ex: 3) {x} este numar neutru')


#4. Verifică și afișează dacă z este între -2 și 13.
if (x>-2) and (x<13):
    print(f'(Ex: 4) {x} se afla intre -2 si 13')
else:
    print(f'(Ex: 4) {x} nu se afla intre -2 si 13')

#5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
if (x-y) < 5:
    print(f"(Ex: 5) Diferenta dintre {x} si {y} este mai mica decat 5")
else:
    print(f"(Ex: 5) Diferenta dintre {x} si {y} nu este mai mica decat 5")

#6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if not((x<5) and (x>27)):
    print(f'(Ex: 6) {x} se afla intre 5 si 27')
else:
    print(f'(Ex: 6) {x} nu se afla intre 5 si 27')

#7. x și y (int) Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

if x == y:
    print(f'(Ex: 7) {x} este egal cu {y}')
elif x>y:
    print(f'(Ex: 7) {x} este mai mare decat {y}')
else:
    print(f'(Ex: 7) {x} este mai mic decat {y}')

#8. X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

z = int(input("(Ex: 8) Introduceti un numar pentru z: "))
if x == y == z:
    print("Triunghiul este echilateral.")
elif (x == y !=z) or (x!=y==z) or (x==z!=y):
    print("Triunghiul este isoscel.")
else:
    print("Triunghiul este oarecare")

#9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu
vocale = ["a", "e", "i", "o", "u"]

litera = input("Introdu o litera: ")
if litera in vocale:
    print(f"{litera} este vocala")
else:
    print(f'{litera} nu este vocala')

#10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = input("(Ex:10) Introduceti o nota de la 1 la 10: ")
if '.' in nota:
    nota = float(nota)
    nota = round(nota + 0.1)
else:
    nota = int(nota)

if nota > 10:
    print("Error: nota nu poate fi mai mare decat 10")
elif nota <= 4:
    print("F")
elif 4<nota<=6:
    print("E")
elif 6<nota<=7:
    print("C")
elif 7<nota<=8:
    print("B")
else:
    print("A")












