import matplotlib.pyplot as plt
import pandas as pd

#Pede ao usuário qual gráfico ele ira querer
print("Para os gráficos sobre papel aluminio,digite 1")
print("Para os gráficos sobre papel normal,digite 2")
qual_gráfico = input("Insira o valor desejado:")

#Importa a tabela de dados com base no input do usuário:
if (int(qual_gráfico) == 1):
    sheet = pd.read_csv("Tabela 1(Aluminio).csv")
    nome = "alumínio"
elif (int(qual_gráfico) == 2):
    sheet = pd.read_csv("Tabela 2(Papel).csv")
    nome = "papel"
else:
    print("Valor invalido,encerrando")
    exit()

#Converte os valores da tabela em arrays 1d:
massa = (sheet[["massa"]].to_numpy()).flatten()
diam_p = (sheet[["Ø paq"]].to_numpy()).flatten()
diam_r = (sheet[["Ø reg"]].to_numpy()).flatten()
erro_p = (sheet[["desvio paq"]].to_numpy()).flatten()
erro_r = (sheet[["desvio reg"]].to_numpy()).flatten()

#Cria os gráficos Massa x Diametro:
plt.errorbar(massa,diam_r,yerr = erro_r,fmt = "D:",label="Regua")
plt.errorbar(massa,diam_p,yerr = erro_p,fmt = "s--",label="Paquimetro")

#Estiliza o gráfico para melhor leitura:
plt.grid()
plt.title("Gráfico para bolas de " + nome)
plt.xlabel("Massa(g)")                         
plt.ylabel("Diametro(mm)")
plt.legend()
plt.show()