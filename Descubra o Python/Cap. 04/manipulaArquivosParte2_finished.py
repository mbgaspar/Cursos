#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def CriaZipModo1():
    shutil.make_archive("ArquivoCompactado", "zip", "C:\\Users\\marce\\Google Drive\\python.aulas - linkedinlearning\\Descubra o Python\\Cap. 03")

CriaZipModo1()

def CriaZipModo2():
    with ZipFile("ArquivoZipModo2.zip", "w") as novoZip:
        novoZip.write("Novo arquivo.bkp")
        novoZip.write("Novo arquivo.txt")
        novoZip.write("zipModo1.zip.zip")

#CriaZipModo2()

def DeletaArquivo():
    os.remove("ArquivoZipModo2.zip")

#DeletaArquivo()