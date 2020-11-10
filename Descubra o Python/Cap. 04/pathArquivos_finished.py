#
# Arquivo com exemplos de como trabalhar com paths
#

from os  import path
import time

def DadosArquivo():
    ArquivoExiste = path.exists("Novo Arquivo.txt")
    ehDiretorio = path.isdir("Novo Arquivo.txt")
    pathArquivo = path.realpath("Novo Arquivo.txt")
    pathRelativo = path.relpath("Novo Arquivo.txt")
    dataCriacao = time.ctime(path.getctime("Novo Arquivo.txt"))
    dataModificacao = time.ctime(path.getmtime("Novo Arquivo.txt"))

    print(ArquivoExiste)
    print(ehDiretorio)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)

DadosArquivo()