#
# Lendo arquivos com funções do Python
#
def leituraArquivo():
    arquivo = open ("Novo Arquivo.txt", "r")
    if (arquivo.mode == "r"):
        conteudo = arquivo.read() #caso tenha um arquivo grande todo o arquivo irá para essa variavel, pode não ser boa ideia. 
        print (conteudo)

    arquivo.close()

leituraArquivo()