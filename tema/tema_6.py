# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

print('---------EXERCITIUL 1 ----------')

class Cerc:
        raza = None
        culoare = None
        pi = 3.14

        def __init__(self,raza, culoare):
            self.raza = raza
            self.culoare = culoare

        def descriere_cerc(self):
            return f'Cercul are raza de {self.raza} si este {self.culoare}.'

        def aria_cerc(self):
            aria = self.pi*(self.raza**2)
            return aria

        def diametru_cerc(self):
            diametru = self.raza * 2
            return diametru

        def circumferinta_cerc(self):
            circumferinta = self.pi*self.diametru_cerc()
            return circumferinta

cercul_meu = Cerc(12, 'Maro')
print(cercul_meu.descriere_cerc())
print(f'Aria cercului este de {cercul_meu.aria_cerc()}')
print(f'Diametrul cercului este {cercul_meu.diametru_cerc()}')
print(f'Circumferinta cercului este {cercul_meu.circumferinta_cerc()}')



print('\n---------EXERCITIUL 2 ----------')
# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        return f'Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}'

    def aria(self):
        arie_dreptunghi = self.lungime*self.latime
        return arie_dreptunghi

    def perimetru(self):
        perimetru_dreptunghi = 2*(self.lungime+self.latime)
        return perimetru_dreptunghi

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare

dreptunghiul_meu = Dreptunghi(10, 5, 'Albastru')
print(f'Dreptunghiul meu are aria de {dreptunghiul_meu.aria()}')
print(dreptunghiul_meu.descrie())
print(f'Dreptunghiul are perimetrul de {dreptunghiul_meu.perimetru()}')
print(dreptunghiul_meu.schimba_culoarea('Rosie'))
print(dreptunghiul_meu.descrie())


print('\n---------EXERCITIUL 3 ----------')
# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        return f'Numele si prenumele angajatului: {self.nume} {self.prenume}\nSalariul sau este de {self.salariu} $.'

    def nume_complet(self):
        return f'Numele complet este {self.nume + " " + self.prenume}.'

    def salariu_lunar(self):
        return f'Salariul lunar este de {self.salariu} $.'

    def salariu_anual(self):
        salariu_tot = self.salariu * 12
        return f'Salariul anual este {salariu_tot}'

    def marire_salariu(self, procent):
        self.salariu = self.salariu * (procent/100)
        return self.salariu


employee = Angajat('Vasile', 'Ion', 3000)
print(employee.descrie())
print(employee.nume_complet())
print(employee.salariu_lunar())
print(employee.salariu_anual())
print(f'Salariul va fi marit cu {employee.marire_salariu(10)} $.')


print('\n---------EXERCITIUL 4 ----------')
# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei'

    def debitare_cont(self, suma):
        self.sold -=suma
        return f'In urma unei plati de {suma}, soldul nostru a scazut la {self.sold}.'

    def creditare_cont(self, suma):
        self.sold += suma
        return f'In urma unui credit de {suma}, soldul nostru se afla la {self.sold}.'

contul_meu = Cont(12345, 'Timon Pumba', 25000)
print(contul_meu.afisare_sold())
print(contul_meu.debitare_cont(5000))
print(contul_meu.creditare_cont(10000))