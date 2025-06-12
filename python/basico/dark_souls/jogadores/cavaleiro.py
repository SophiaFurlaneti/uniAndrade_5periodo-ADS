from jogador import Jogador
class Cavaleiro(Jogador): # Herança
    def __init__(self, nome:str, dano:int, armadura="bronze", resistencia=85):
        super().__init__(nome, dano)
        self.armadura = armadura # Atributos extras
        self.resistencia = resistencia # Atributos extras


    @property # Decorador retorna apenas como propriedade
    def saude(self):
        return self.__saude

    @saude.setter # Decorador retorna apenas como propriedade
    def saude(self, valor):
        self.saude += max(0, valor)

    def atacar(self):
        print("Atacar Polimorfico")
        print(f"{self.nome} atacou!")

    def defender(self):
        print("Defender Polimorfico")
        print(f"{self.nome} defendeu!")

if __name__ == '__main__':
    cavaleiro = Cavaleiro("Rei Artur", 80)
    cavaleiro.atacar()