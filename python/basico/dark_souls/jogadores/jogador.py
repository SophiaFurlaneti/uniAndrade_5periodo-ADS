from abc import ABC, abstractmethod
class Jogador(ABC): #Herança
    def __init__(self, nome:str, dano:int):
        self.nome = nome
        self.dano = dano
        self.__saude = 100 #encapsulamento
    
    @property # Decorador retorna apenas como propriedade
    def saude(self):
        return self.__saude
    
    @saude.setter # Decorador retorna apenas como propriedade
    def saude(self, valor):
        self.saude += max(0, valor)
    
    @abstractmethod # Obriga as classes filhas a implementarem
    def atacar(self):
        print(f"{self.nome} atacou!")
    
    @abstractmethod # Obriga as classes filhas a implementarem
    def defender(self):
        print(f"{self.nome} defendeu!")

if __name__ == '__main__':
    p1 = Jogador("Jow", 50)
    p1.atacar()
    print(p1.saude)