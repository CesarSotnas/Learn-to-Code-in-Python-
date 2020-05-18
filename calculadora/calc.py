class Calculadora:

    def __init__(self, valor1, valor2):
        self.__valor1 = valor1
        self.__valor2 = valor2

    @property
    def soma(self):
        return self.__valor1 + self.__valor2
        
    @property
    def subtracao(self):
        return self.__valor1 - self.__valor2
        
    @property
    def multiplicacao(self):
        return self.__valor1 * self.__valor2
        
    @property
    def divisao(self):
        return self.__valor1 / self.__valor2
        

