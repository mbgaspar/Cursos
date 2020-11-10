
import pandas as pd
import matplotlib.pyplot
import numpy as np
from scipy.stats.stats import pearsonr


import seaborn as sns
caminho = 'C:\\Users\\marce\\Google Drive\\python.aulas - linkedinlearning\\python_para_ciencia_dados_basico\\dados\\mtcars.csv'
carros = pd.read_csv(caminho)
carros.columns = ['nomes','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'qtd_marchas', 'carb']
X = carros[['mpg', 'hp', 'wt', 'qsec']]
sns.pairplot(X)

#Seção 4 - Investigando valores numéricos
'''caminho = 'C:\\Users\\marce\\Google Drive\\python.aulas - linkedinlearning\\python_para_ciencia_dados_basico\\dados\\mtcars.csv'
carros = pd.read_csv(caminho)
carros.columns = ['nomes','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'qtd_marchas', 'carb']
print(carros.head())
print(carros.sum())'''

#imprimindo multiplicação matriz.
''' 
a = np.arange(3) #vetor
aa = np.array([[2.,4.,6.], [1.,3.,5.], [10.,20.,30.]]) #matriz
bb = np.array([[4.,6.,7.], [0.,7.,7.], [1.,4.,0.]]) #matriz 
z = np.dot(aa,bb) #multiplação de matriz
print (z)
'''
#grafico
'''meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]
matplotlib.pyplot.plot(meses, valores)
matplotlib.pyplot.show()'''