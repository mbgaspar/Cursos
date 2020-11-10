#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def copiaArquivo():
    if path.exists("novo arquivo.txt"):
        pathAtual = path.realpath("novo arquivo.txt")
        novoPath = pathAtual + ".bkp"
        shutil.copy(pathAtual, novoPath)

        shutil.copystat(pathAtual, novoPath)

#copiaArquivo()

def renomeararquivo():
    if path.exists("novo arquivo.txt.bkp"):
        os.rename("novo arquivo.txt.bkp", "Arquivo alterado.txt")
renomeararquivo()