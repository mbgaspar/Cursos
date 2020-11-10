##Autora: Carolina de Farias
##Professor: Robinson Pizzio,Dr Eng.
##Disciplina de sinais e sistemas
##Esse script contém o cálculo da serie de fourier das funções "c" e "e" propostas pelo professor


from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import cmath
import time
import warnings

warnings.filterwarnings('ignore')
global somaDn

soma = 0
positivos = []

passo = 100

valoresFase =[]

eixosY = []
eixosX = []

eixosYFourier = []

somaFourier = 0

t = Symbol('t')

x_ = np.linspace(-3,3, 20)


def plotarGrafico(eixoX, valores, xlabel, ylabel, titulo, eixoY = "", valoresY= ""):
    if(titulo == 'Fourier'):
        labelX, =plt.plot(eixoX, valores, label= 'Função original')
        labelY, = plt.plot(eixoY, valoresY , label='Função Fourier')
        plt.legend(handles=[labelX, labelY])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(titulo)
        plt.show()
    elif(titulo == 'Fourier Degrau'):
        labelX, = plt.step(np.array(eixoX), valores, label='Função original')
        labelY, = plt.step(np.array(eixoY), valoresY, label='Função Fourier')
        plt.legend(handles=[labelX, labelY])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(titulo)
        plt.show()
    else:
        plt.stem(eixoX, valores, linefmt='-')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(titulo)
        plt.show()


plt.style.use('ggplot')

def definePotenciaSinal(f1,f2):
    potenciaSinal = 0
    somaDn = 0
    for har in range(-n, n + 1):
        valorIntegral = nsimplify(Integral((((f1) * exp(complex(0, -1) * wZero * har * t)) / T), (t, -2, 0))).doit().evalf() + \
        nsimplify(Integral((((f2) *exp(complex(0, -1) * wZero * har * t) / T)), (t, 0, 1))).doit().evalf()
        if har == 0:
            d0 = (valorIntegral)**2
        elif (har >= 1 and har < n):
            dN = abs(valorIntegral)**2
            somaDn += 2*dN
        elif har ==n:
            dN = abs((valorIntegral)**2)
            somaDn += 2 * dN
            potenciaSinal= d0 + somaDn
    return potenciaSinal

def definePotenciaSinalFuncao2(f1,f2):
    potenciaSinal = 0
    somaDn = 0
    for har in range(-n, n + 1):
        valorIntegral = nsimplify(exp(complex(0, -1) * har * wZero * t) * Integral((exp(complex(0, -1) * har * wZero * t)) / T,(t, 0, 6)).doit().evalf())
        if har == 0:
            d0 = (valorIntegral)**2
        elif (har >= 1 and har < n):
            dN = abs(valorIntegral)**2
            somaDn += 2*dN
        elif har ==n:
            dN = abs((valorIntegral)**2)
            somaDn += 2 * dN
            potenciaSinal= d0 + somaDn
    return potenciaSinal

def definePotenciaSinalOriginal(f1,f2):
    valorIntegral = Integral((((f1)**2) / T), (t, -(T/2), T/2)).doit().evalf() +\
                    Integral((((f2)**2 /T)), (t, -(T/2), T/2)).doit().evalf()

    return valorIntegral


def defineFase(f1, f2):
    valoresFase = []
    for har in range(-n, n + 1):
        valorIntegral = nsimplify(Integral((((f1) * exp(complex(0, -1) * wZero * har * t)) / T),
                                 (t, -2, 0))).doit().evalf() + nsimplify(Integral(
            (((f2) * exp(complex(0, -1) * wZero * har * t)) / T), (t, 0, 1))).doit().evalf()
        valorConvertidoComplexToPolar = cmath.polar(valorIntegral)

        valorConvertidoImaginario = valorConvertidoComplexToPolar[1]

        valoresFase.append(valorConvertidoImaginario)
    return valoresFase

def defineFaseFuncao2():
    valoresFase = []
    for har in range(-n, n + 1):
        valorIntegral = (exp(-har*wZero*1j)*1j - exp(-har*wZero*2j)*1j - exp(-har*wZero*4j)*1j + exp(-har*wZero*5j)*1j)/(6*har*wZero)

        valorConvertidoComplexToPolar = cmath.polar(valorIntegral)

        valorConvertidoImaginario = valorConvertidoComplexToPolar[1]

        valoresFase.append(valorConvertidoImaginario)
    return valoresFase

def defineAmplitude(f1, f2):
    valoresAmplitude = []
    for har in range(-n, n + 1):
        valorIntegral = nsimplify(Integral((((f1) * exp(complex(0, -1) * wZero * har * t)) / T),
                                 (t, -2, 0))).doit().evalf() + nsimplify(Integral(
            (((f2) * exp(complex(0, -1) * wZero * har * t)) / T), (t, 0, 1))).doit().evalf()
        valorConvertidoComplexToPolar = cmath.polar(valorIntegral)

        valorConvertidoReal = valorConvertidoComplexToPolar[0]

        valoresAmplitude.append(valorConvertidoReal)
    return valoresAmplitude

def defineAmplitudeFuncao2():
    valoresAmplitude = []
    for har in range(-n, n + 1):

        valorIntegral = (exp(-har*wZero*1j)*1j - exp(-har*wZero*2j)*1j - exp(-har*wZero*4j)*1j + exp(-har*wZero*5j)*1j)/(6*har*wZero)

        valorConvertidoComplexToPolar = cmath.polar(valorIntegral)

        valorConvertidoReal = valorConvertidoComplexToPolar[0]

        valoresAmplitude.append(valorConvertidoReal)
    return valoresAmplitude

def somaHarmonicas(tempo,somaHarmonica, f1,f2):
    start_time = time.time()
    for har in range(-n, n + 1):

        valorIntegral = nsimplify(Integral((((f1) * exp(complex(0, -1) * wZero * har * t)) / T), (t, -2, 0))).doit().evalf() + nsimplify(Integral((((f2) * exp(complex(0, -1) * wZero * har * t)) / T), (t, 0, 1))).doit().evalf()

        valorFuncao = valorIntegral * exp(complex(0, 1) * har * wZero * tempo)

        printPositivos(har, valorIntegral)

        somaHarmonica += valorFuncao
    print("--- %s seconds ---" % (time.time() - start_time))
    return cmath.polar(somaHarmonica)[0]

def somaHarmonicasFuncao2(tempo,somaHarmonica):
    start_time = time.time()
    for har in range(-n, n + 1):
        if(har == 0):
            continue
        valorIntegral = (exp((-har) * wZero * complex(0,1)) * complex(0,1) - exp((-har) * wZero * complex(0,2)) * complex(0,1) - exp((-har) * wZero * complex(0,4)) * complex(0,1) + exp((-har) * wZero * complex(0,5)) * complex(0,1)) / (6 * har * wZero)
        valorFuncao = valorIntegral.as_real_imag()[1] * exp(complex(0, 1) * har * wZero * tempo)

        somaHarmonica += valorFuncao
    print("--- %s seconds ---" % (time.time() - start_time))
    return somaHarmonica.as_real_imag()[1]

def defineFourier(lista,somaHarmonica, f1, f2):
    for i in range(0, passo):
        eixoX = lista[i]
        eixosX.append(eixoX)
        somaH = somaHarmonicas(lista[i],somaHarmonica,f1, f2)
        eixosYFourier.append(somaH)

def defineFourierFuncao2(lista,somaHarmonica):
    for i in range(0, passo):
        eixoX = lista[i]
        eixosX.append(eixoX)
        somaH = somaHarmonicasFuncao2(lista[i],somaHarmonica)
        eixosYFourier.append(somaH)

def printPositivos(har, valorIntegral):
    if (har > 0):
        positivo = {
            'valor': valorIntegral,
            'expoente': har
        }
        print("\nValor Dn: " + str(positivo['valor']) + "| Expoente = " + str(positivo['expoente']) + "\n")


def mostraOpcoes(lista, somaHarmonica,f1, f2, n):
    print("Escolha as seguintes opções\n")
    print("1- Amplitude\n")
    print("2- Fase\n")
    print("3- Espectro de frequência\n")
    print("4- Série de Fourier\n")
    print("5- Valor da distorção harmônica total?\n")

    resposta = input("Qual grafico você gostaria de visualizar?")

    if resposta == "1":
        x = np.linspace(-n, n, (n * 2) + 1)
        valoresAmplitude = defineAmplitude(f1 , f2)
        plotarGrafico(x, valoresAmplitude, 'n', '|Dn|', 'Amplitude')
    elif resposta == "2":
        # Grafico fase
        x = np.linspace(-n, n, (n * 2) + 1)
        valoresFase = defineFase(f1,f2)
        plotarGrafico(x, valoresFase, 'n', 'Dn((rad))', 'Fase')
    elif resposta == "3":
        x = np.linspace(-n, n, (n * 2) + 1)
        valoresAmplitude = defineAmplitude(f1, f2)
        valoresFase = defineFase(f1, f2)
        # Gráfico amplitude
        plotarGrafico(x, valoresAmplitude, 'nw', '|Dn|', 'Amplitude')
        # Grafico fase
        plotarGrafico(x, valoresFase, 'nw', 'Dn((rad))', 'Fase')
    elif resposta == "4":
        eixoX = [-6, -5, -3, -2, 0, 1, 3, 4, 6]
        eixoY = [2, 0,  2,  0, 2, 0, 2, 0, 2]
        defineFourier(lista,somaHarmonica,f1,f2)
        plotarGrafico(eixoX, eixoY, 'Funcao Original', 'f(t)', 'Fourier',eixosX,eixosYFourier)

    elif resposta == "5":
        potenciaSinalFourier = definePotenciaSinal(f1,f2)
        potenciaSinalOriginal = definePotenciaSinalOriginal(f1,f2)

        distorcao = (potenciaSinalFourier / potenciaSinalOriginal) * 100

        print("A distorção harmonica é " + str(distorcao) + "%")
    else:
        print("Não existe opção para entrada informada")

def mostraOpcoesFuncao2(lista, somaHarmonica,n):
    print("Escolha as seguintes opções\n")
    print("1- Amplitude\n")
    print("2- Fase\n")
    print("3- Espectro de frequência\n")
    print("4- Série de Fourier\n")

    resposta = input("Qual grafico você gostaria de visualizar?")

    if resposta == "1":
        x = np.linspace(-n, n, (n * 2) + 1)
        valoresAmplitude = defineAmplitudeFuncao2()
        plotarGrafico(x, valoresAmplitude, 'n', '|Dn|', 'Amplitude','','')
    elif resposta == "2":
        # Grafico fase
        x = np.linspace(-n, n, (n * 2) + 1)
        valoresFase = defineFaseFuncao2()
        plotarGrafico(x, valoresFase, 'n', 'Dn((rad))', 'Fase')
    elif resposta == "3":
        x = np.linspace(-n, n, (n * 2) + 1)
        valoresAmplitude = defineAmplitudeFuncao2()
        valoresFase = defineFaseFuncao2()
        # Gráfico amplitude
        plotarGrafico(x, valoresAmplitude, 'nw', '|Dn|', 'Amplitude')
        # Grafico fase
        plotarGrafico(x, valoresFase, 'nw', 'Dn((rad))', 'Fase')
    elif resposta == "4":
        eixoX = np.array([-12,-11,-10,-9,-8 ,-7 ,-6, -5 ,-4 ,-3, -2 ,-1 ,0  ,1  ,2  ,3,  4  ,5  ,6  ,7  ,8  ,9  ,10, 11, 12 ])
        eixoY = np.array([0,1,1,0,-1 ,-1 , 0 , 1 , 1 , 0 ,-1 ,-1 , 0 , 1 , 1 , 0 ,-1 ,-1 , 0 ,1 ,1 , 0 , -1, -1, 0, ])
        defineFourierFuncao2(lista, somaHarmonica)
        plotarGrafico(eixoX, eixoY, 'Funcao Original', 'f(t)', 'Fourier Degrau',eixosX,eixosYFourier)
    else:
        print("Não existe opção para entrada informada")

while(True):
    print("Qual função você deseja visualizar?\n")
    print("Digite 1 para a função (c)\n")
    print("Digite 2 para a função (e)\n")

    res = input("")

    if res == "1":
        T = 3
        wZero = 2 * pi / T
        f1 = t+2
        f2 = -2*t+2
        lista = np.linspace(-3 * 2, 3*2, passo)
        somaHarmonica = 0

        n = int(input("Digite harmonica: "))
        mostraOpcoes(lista, somaHarmonica, f1,f2, n)


    elif res == "2":
        T = 6
        wZero = 2 * pi / T
        somaHarmonica = 0

        lista = np.linspace(-6*2, 6*2, passo)

        n = int(input("Digite harmonica: "))
        mostraOpcoesFuncao2(lista, somaHarmonica,n)


    else:
        print("Resposta inválida!")

#x_ = np.linspace(-3,3, 100)

#alterar
#lista = np.linspace(-2*3.14, 2*3.14, 100)
#lista = np.linspace(-2*2, 2*2, 100)
#lista = np.linspace(-2*3, 2*3, 100)

print("Escolha as seguintes opções\n")
print("1- Amplitude\n")
print("2- Fase\n")
print("3- Espectro de frequência\n")
print("4- Série de Fourier\n")
print("5- Valor da distorção harmônica total?\n")
resposta = input("Qual grafico você gostaria de visualizar?")

