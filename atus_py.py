import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Função para o ajuste de reta (y = a*x + b)
def linear_model(x, a, b):
    return a * x + b

#Função para ajuste com x^2
def square_model(x):
    return x**2

# Caminho para o arquivo Excel
file = 'Cecillya.xlsx'
planilhas = pd.read_excel(file, sheet_name=None)

# Iterando sobre cada planilha e plotando os dados com barras de erro e ajuste de reta
for nome_planilha, dados in planilhas.items():
    x = dados['x']
    y = dados['y']
    sigma_y = dados['sigma_y']
    #sigma_x = dados['sigma_x']
    
    # Ajuste de reta usando os dados (x, y)
    params, covariance = curve_fit(linear_model, x, y)
    a, b = params  # a é o coeficiente angular, b é o intercepto

    # Cálculo do número de graus de liberdade
    n = len(x)
    DoF = n - 2
    
    # Cálculo do chi^2
    y_ajustado = linear_model(x, a, b)
    chi2 = np.sum(((y - y_ajustado) / sigma_y) ** 2)
    
    # Plotando o gráfico para cada planilha com barras de erro e linha de ajuste
    plt.figure()
    plt.errorbar(x, y ,yerr=sigma_y, fmt='o', label=f'Dados: {nome_planilha}', ecolor='red', capsize=3)
    plt.plot(x, linear_model(x, a, b), color='blue', label=f'Ajuste de reta: y = {a:.6f}x + {b:.6f}')
    plt.xlabel('Tempo')
    plt.ylabel('Velocidade')
    plt.title(f'Aceleração da Gravidade')
    plt.legend()
    plt.show()
    
    # Exibindo os coeficientes, graus de liberdade e chi-quadrado no console
    print(f'Coeficiente angular (a) para {nome_planilha}: {a:.6f}')
    print(f'Intercepto (b) para {nome_planilha}: {b:.6f}')
    print(f'Número de Graus de Liberdade (DoF) para {nome_planilha}: {DoF}')
    print(f'Chi-quadrado (χ²) para {nome_planilha}: {chi2:.6f}\n')
