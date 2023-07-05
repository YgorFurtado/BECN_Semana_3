import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sci

#Importa a tabela de dados
sheet = pd.read_csv("Tabela 1(Aluminio).csv")

#Converte os valores da tabela em arrays 1d:
massa = (sheet[["massa"]].to_numpy()).flatten()
diam_p = ((sheet[["Ø paq"]].to_numpy()).flatten())
diam_r = ((sheet[["Ø reg"]].to_numpy()).flatten())
erro_p = (sheet[["desvio paq"]].to_numpy()).flatten()
erro_r = (sheet[["desvio reg"]].to_numpy()).flatten()

#Cria log de massa e diâmetro
log_massa = np.log(massa)
log_paquimetro = np.log(diam_p)
log_regua = np.log(diam_r)

#Faz uma regressão linear no gráfico e retorna os seus coeficientes
coef_ang_paq, coef_lin_paq,a ,b ,c = sci.linregress(log_paquimetro,log_massa)
coef_ang_reg, coef_lin_reg,d ,e ,f = sci.linregress(log_regua,log_massa)
y_paq = coef_ang_paq*1 + coef_lin_paq
y_reg= coef_ang_reg*1 + coef_lin_reg
print("O Coeficiente angular medido no paquímetro é:" + str(coef_ang_paq))
print("O Coeficiente angular medido na régua é:" + str(coef_ang_paq))

#Cria os gráficos Diâmetro x Massa:
plt.subplot(221)
plt.errorbar(diam_r,massa,xerr = erro_r,fmt = "D:",label="Régua")
plt.errorbar(diam_p,massa,xerr = erro_p,fmt = "s--",label="Paquímetro")
plt.grid()
plt.xlabel("Diametro(mm)")                         
plt.ylabel("Massa(g)")
plt.title("Gráfico Diametro x Massa")
plt.legend()

#Cria os gráficos LogxLog - Diâmetro x Massa:
plt.subplot(222)
plt.plot(log_regua,log_massa,"s--",label="Régua",)
plt.plot(log_paquimetro,log_massa,"D:",label="Paquímetro",)
plt.grid()
plt.xlabel("Log(Diametro)")                         
plt.ylabel("Log(Massa)")
plt.title("LogxLog(Diametro X Massa)")
plt.legend()
plt.xlim(1,3.75)
plt.ylim(-4.95,1.2)

#Cria gráfico logXlog ajeitados
plt.subplot(212)
plt.axline((1,y_reg),slope=coef_ang_reg,ls = (5, (10, 3)),label = "Régua")
plt.axline((1,y_paq),slope=coef_ang_paq,ls = (0, (3, 1, 1, 1, 1, 1)),label="Paquímetro",color = "orange")
plt.grid()
plt.xlabel("Log(Diametro)")                         
plt.ylabel("Log(Massa)")
plt.title("Log x Log Ajustado")
plt.legend()
plt.xlim(1,3.75)
plt.ylim(-4.95,1.2)

#Mostra os gráficos
plt.suptitle("Gráficos do Papel Alumínio")
plt.show()