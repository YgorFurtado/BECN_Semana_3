import numpy as np

#Pede ao usuário 3 valores.
valor_1 = input("Valor 1:  ")
valor_2 = input("Valor 2:  ")
valor_3 = input("Valor 3:  ")

#Converte os valores em float:
lista = [float(valor_1),float(valor_2),float(valor_3)]

#Calcula o desvio padrão da Lista e Imprime no Terminal
Desvio = np.std(lista)
print(Desvio)
