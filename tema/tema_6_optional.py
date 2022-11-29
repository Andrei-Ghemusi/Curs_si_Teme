from datetime import date
from tabulate import tabulate

print('\n---------EXERCITIUL 1 ----------')
# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

class Factura:
    seria = 123456
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitatea):
        self.cantitate=cantitatea

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        today = date.today()
        print(f'Data: {today}')
        print(f'Factura seria {self.seria}, numar {self.numar}.')

info = Factura(12,'Ariel', 100, '20 lei')
lista = [['Nokia 3370', 7, 700, 49000]]
info.genereaza_factura()
print(tabulate(lista, headers=['Produs', 'Cantitate', 'Pret bucata', 'Total']))



print('\n---------EXERCITIUL 2 ----------')
# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

class Masina:
    marca = 'Dacia'
    model = '1310'
    viteza_actuala = 0
    culoare = 'Gri'
    culori_disponibile = {'Albastru', 'Rosu', 'Galben', 'Maro', 'Verde'}
    viteza_maxima = 180
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Masina este {self.marca} {self.model}, de culoare {self.culoare} cu viteza maxima de {self.viteza_maxima}km/h.\n'
              f'E masina inmatriculata? {self.inmatriculata}.')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste_culoare(self,culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            print('Error, culoarea nu e disponibila')

    def accelereaza_viteza(self, viteza):
        self.viteza = viteza
        if viteza == 0:
            print('Masina stationeaza sau e oprita.')
        elif viteza >self.viteza_maxima:
            viteza = self.viteza_maxima
            return viteza
        elif viteza <0:
            print('Eroare, viteza nu poate fi negativa.')

    def franeaza(self):
        self.viteza = 0
        print(f'Am oprit masina si viteza e {self.viteza}')


masina_mea = Masina('1310', 180)
masina_mea.descrie()
masina_mea.inmatriculare()
masina_mea.descrie()
masina_mea.vopseste_culoare('Verde')
masina_mea.descrie()
print(masina_mea.accelereaza_viteza(202))
masina_mea.franeaza()


print('\n---------EXERCITIUL 3 ----------')
# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict

class TodoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        self.todo['curatenie'] = 'Facem curat.'
        self.todo['gatit'] = 'Gatim cu totii.'
        self.todo['curatenie2'] = 'Curatam dupa ce am gatit'
        self.todo['mancam'] = 'Mancam ce am gatit.'
        self.todo['dormim'] = 'Dormim dupa ce am mancat. Somn usor'
        if self.todo[nume] not in self.todo:
            raspuns = input('Doriti sa adaugati task-ul? Da sau Nu? ')
            if raspuns == 'Nu':
                print('La revedere')
            if raspuns == 'Da':
                print('Adaugam task-ul!')
                nume = input('Numeste task-ul: ')
                descriere = input('Descrie task-ul: ')
                self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        del self.todo[nume]

    def afiseaza_todo_list(self):
        return self.todo.keys()

    def afiseaza_detalii_suplimentare(self, nume_task):
        return self.todo[nume_task]

work = TodoList()
work.adauga_task('incepem', 'Sa lucram')
work.finalizeaza_task('curatenie')
print(f"Afiseaza cheile {work.afiseaza_todo_list()}")
print(f"Afisam valoarea {work.afiseaza_detalii_suplimentare('incepem')}")







