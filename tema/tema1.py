# 1
# Variabila este acea adresa de memorie in care stocam informatii

# 2
# string
culoare_masina = 'rosie'

# integer
numar_roti = 6

# float
consum = 25.2

# boolean
este_noua_masina = True

# 3
print(type(culoare_masina))
print(type(numar_roti))
print(type(consum))
print(type(este_noua_masina))

# 4
print(round(consum))

# 5
print(culoare_masina)
print(numar_roti)
print(consum)
print(este_noua_masina)

# 6
numele = 'Ghemusi'
prenumele = 'Andrei'
print('Numele complet are ' + str(len('Ghemusi' + 'Andrei')) + ' caractere')

# 7
lungimea = 7
latimea = 3
print('Aria dreptunghiului este ' + str(lungimea*latimea))

# 8
sentence = 'Coral is either the stupidest animal or the smartest rock'
print(f'"the" apare de {sentence.count("the")} ori')

# 9
sentence2 = sentence.replace("the", "THE")
print(f' "THE" apare de {sentence2.count("THE")} ori')

# 10
assert sentence.isnumeric() == False, ' sunt doar numere'
print('nu sunt numere')




