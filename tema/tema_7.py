from abc import abstractmethod, ABC

# 2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum împreună).
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi.')


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura_patrat(self):
        pass

    @latura_patrat.getter
    def latura_patrat(self):
        return self.__latura

    @latura_patrat.setter
    def latura_patrat(self, latura):
        self.__latura = latura

    @latura_patrat.deleter
    def latura_patrat(self):
        self.__latura = None

    def aria(self):
        aria = self.__latura ** 2
        return aria

    def colturi(self, nr_colturi=0):
        nr_colturi = 4
        if nr_colturi == 0:
            print('Eu nu am colturi.')
        else:
            self.descrie()


obiect = Patrat(2)
print(f'Aria patratului este: {obiect.aria()}')
print(f'Obiectul inainte de update, prin getter: {obiect.latura_patrat}')
obiect.latura_patrat = 5
print(f'Obiectul dupa update, prin getter: {obiect.latura_patrat}')
del obiect.latura_patrat
print(f'Obiectul returnat dupa deleter: {obiect.latura_patrat}')


class Cerc(FormaGeometrica):

    def __init__(self,raza):
        self.__raza = raza

    @property
    def raza_cerc(self):
        pass

    @raza_cerc.getter
    def raza_cerc(self):
        return self.__raza

    @raza_cerc.setter
    def raza_cerc(self, raza):
        self.__raza = raza

    @raza_cerc.deleter
    def raza_cerc(self):
        self.__raza = None

    def aria(self):
        print(f'Aria cercului este {self.__raza*self.PI}')

    def colturi(self, nr_colturi=0):
        if nr_colturi == 0:
            print('Eu nu am colturi.')
        else:
            self.descrie()

obiect2 = Cerc(9)
obiect2.aria()
print(f'Obiectul 2 inainte de update, prin getter este {obiect2.raza_cerc}')
obiect2.raza_cerc = 4
print(f'Obiectul 2 dupa update este {obiect2.raza_cerc}')
del obiect2.raza_cerc
print(f'Obicetul 2 dupa deleter este {obiect2.raza_cerc}')


obiect_colturi_patrat = Patrat(3)
obiect_colturi_patrat.colturi()

obiect_colturi_cerc = Cerc(7)
obiect_colturi_cerc.colturi()


