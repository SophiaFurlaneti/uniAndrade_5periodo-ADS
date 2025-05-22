class Item:
    def __init__(self, tipo:str, efeito:int):
        self.tipo = tipo
        self.efeito = efeito

class Inventario:
    def __init__(self):
        self.itens = [] #Agregação
        
    def adicionar_item(self, item: Item):
        if not item:
            print("Escolha um item para inserir")
            
        self.itens.append(item)
    
    def listar_itens(self):
        for item in self.itens:
            print(f"Itens {item.tipo}")

class Armadura:
    def __init__(self, nome:str, protecao:int):
        self.nome = nome
        self.protecao = protecao
        
    def blind(self):
        print("Sua proteção aumentou!")

class Player:
    def __init__(self, nome, nome_armadura: Armadura, protecao:int):
        self.nome = nome
        self.energia = 100
        self.vivo = True
        self.armadura: Armadura(nome_armadura, protecao) # Composição
        self.inventario = Inventario() # Agregação
        
    def usar_pocao(self, pocao):
        if not self.vivo:
            print("Game Over!")
            return
        
        efeito_pocao = pocao.usar() # Número + ou -
        nova_energia = efeito_pocao + self.energia
        
        # Trator casos (0 e 100+)
        if nova_energia <=0:
            nova_energia = 0
            self.vivo = False
            
        if nova_energia >= 100:
            nova_energia = 100
            print("Impossível usar cura!")
            
        self.energia = nova_energia
        self.status()
        
    def status(self):
        print(f"\n----- STATUS ----- \n")
        print(f"Vivo {self.vivo} - Energia: {self.energia}%")
        print(f"\n-------------------\n")

class PocaoVerde:
    def __init__(self, tipo:str, efeito:int):
        self.tipo = tipo
        self.efeito = efeito
        
    def usar(self):
        return self.efeito #Número

class PocaoRoxa:
    def __init__(self, tipo:str, efeito:int):
        self.tipo = tipo
        self.efeito = efeito
        
    def usar(self):
        return -self.efeito #Número


p1 = Player("Kronus")
cura = PocaoVerde("Cura Verde", 15)
veneno = PocaoRoxa("Morte certa", 25)
# p1.usar_pocao(cura)
# p1.usar_pocao(cura)
# p1.usar_pocao(cura)
# p1.usar_pocao(veneno)
# p1.usar_pocao(veneno)
# p1.usar_pocao(veneno)
# p1.usar_pocao(veneno)

inventario = Inventario()
faca = Item("faca Tramontina", 120)
escudo = Item("Escudo do rei", 90)
m500 = Item("Pistola m500", 247)


# inventario.adicionar_item(faca)
# inventario.adicionar_item(escudo)
# inventario.listar_itens()
# inventario.adicionar_item(m500)

