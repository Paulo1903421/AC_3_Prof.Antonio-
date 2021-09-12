from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def executar(self):
        pass



class Divisao(Operacao):
    def executar(self, va1, va2):
        return va1 / va2




class Soma(Operacao):
    def executar(self, va1, va2):
        return va1 + va2



class Subtracao(Operacao):
    def executar(self, va1, va2):
        return va1 - va2




class Multiplicacao(Operacao):
    def executar(self, va1, va2):
        return va1 * va2
