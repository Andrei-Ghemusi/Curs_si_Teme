print('-----EXERCITIUL 1------')
# 1.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in range(len(alte_numere)):
	if alte_numere[i]%2 == 0 and alte_numere[i]>0:
		numere_pare.append(alte_numere[i])
		numere_pozitive.append(alte_numere[i])
	elif alte_numere[i]%2 == 0 and alte_numere[i]<0:
		numere_pare.append(alte_numere[i])
		numere_negative.append(alte_numere[i])
	elif alte_numere[i]%2 != 0 and alte_numere[i]>0:
		numere_impare.append(alte_numere[i])
		numere_pozitive.append(alte_numere[i])
	else:
		numere_impare.append(alte_numere[i])
		numere_negative.append(alte_numere[i])

print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)


print('-----EXERCITIUL 2------')
# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4

for i in range(len(alte_numere)):
	for j in range(i+1, len(alte_numere)):
		if alte_numere[j] < alte_numere[i]:
			alte_numere[j], alte_numere[i] = alte_numere[i], alte_numere[j]

print(alte_numere)


print('-----EXERCITIUL 3------')
# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!

from random import randrange
numar_secret = randrange(30)
numar_ghicit = int(input('Alegeti un numar: '))
while numar_ghicit < 31:
	if numar_ghicit < numar_secret:
		print('Nr secret e mai mare')
		break
	elif numar_ghicit > numar_secret:
		print('Nr secret e mai mic')
		break
	else:
		print('Felicitări! Ai ghicit!')
		break


print('-----EXERCITIUL 4------')
# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

numar_tastatura = int(input('Introduceti un numar: '))
for i in range(numar_tastatura):
	for j in range(i+1):
		print(j+1, end='')
	print('')

#The end= “ ” in the print statement allows you to print on the same horizontal line with a space separating
#each printed element. If you don’t add this code, your output will appear as a vertical line.

print('-----EXERCITIUL 5------')
# 5.
# tastatura_telefon = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[0]]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
tastatura_telefon = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[0]]
for i in range(len(tastatura_telefon)):
	for j in range(len(tastatura_telefon[i])):
		print(tastatura_telefon[i][j], end="")