#
# Exemplo de como criar classes
#
import emoji
print(emoji.emojize(':point_up:', use_aliases=True))

class minhaClasse():
    def __init__(self):
        self.meuAtributo = "Passou pelo construtor!"

    def meuMetodo(self):
        print("Passou pelo meuMetodo")
    
    def meuMetodo2(self, valor):
        self.outroAtributo = valor
        print(self.outroAtributo)

def criaObjeto():
    meuObj = minhaClasse()
    var1 = meuObj.meuAtributo
    print(var1)

    meuObj.meuMetodo()

    meuObj.meuMetodo2("Executando um método")

criaObjeto()

print(emoji.emojize(':point_up:', use_aliases=True))