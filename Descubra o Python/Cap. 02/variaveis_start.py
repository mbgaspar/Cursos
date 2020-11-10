
# Declarando e inicializando uma variável
f = 0 
print(f)

# declarando a mesma variável novamente
f = "abc"
print(f)

# Gerando um erro, tentando unir variáveis de tipos diferentes


# Variável Global X Variável local 
def algumafx ():
    global f
    f="def"
    print(f)

algumafx() # impressão  da linha 16
print(f) # mesma impressão da linha 8