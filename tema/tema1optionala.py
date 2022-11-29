# 1
masina = "Volvo"
print(masina[2])

# 2
# -1 reverses a string, so string[::-1] is the reverse of the original
string = 'radar'
assert string == string[::-1], "Error: NOT a palindrome"
print("The string IS a palindrome")

# 3
sentence = "alabala portocala"; first_word = sentence[0:7]; second_word = sentence[-9:]; print(first_word); print(second_word)
first_word, second_word = sentence.split()


# 4
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

prop = input("Introduceti:")
caracter = prop[0]
prop2 = prop.replace(caracter, caracter.upper())
caracter_1 = prop2[0].lower()
caracter_2 = prop2[-1].lower()
propozitie_finala = caracter_1 + prop2[1:-1] + caracter_2
print(propozitie_finala)


# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

user = input("Introduceti username: ")
parola = int(input("Introduceti parola: "))
lungime_parola = len(str(parola))
parola_dinamica = ("x"*len(str(parola)))
print(f'Parola pentru {user} este {parola_dinamica} si are {lungime_parola} caractere')










