# Importação das bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from matplotlib.offsetbox import AnchoredText as at

st.set_option('deprecation.showPyplotGlobalUse', False)

# Importação dos dados file *.csv
df = pd.read_csv('C:/Users/profc/OneDrive/Documentos/COMUSA.csv', sep=';', encoding='utf8', decimal=',', usecols = [0,1,10,11,13,14,15,16])

# Excluir os campos de 'Total a Pagar (R$)' até 'Valor Água (R$)' para anonimizar

# Cálculo da média de todos os indicadores
cor = df['Cor (UC)'].mean()
coliformes = df['% Coliformes Totais'].mean()
turbidez = df['Turbidez (NTU)'].mean()
cloro_livre = df['Cloro Livre (mg/l)'].mean()
fluor = df['Flúor (mg/l)'].mean()
pH = df['pH'].mean()

st.write("""
## Projeto de monitoramento da *qualidade da água* fornecida pela **COMUSA** em Novo Hamburgo (RS)
### por Claudio Fagundes Pereira, (C) 2021
#### Aviso Legal: as informações disponíveis neste dashboard são oriundas dos relatórios da qualidade da água que são informadas nas contas de água dos consumidores finais!
#####
""")


st.sidebar.header('')
st.sidebar.image('./AQ_logo.png', width=160)
st.sidebar.header('Selecione o indicador desejado:')

st.write(""
         "Gráfico do Indicador"
         "")

# Gráfico do pH
my_dpi = 200
plt.figure(figsize=(1100 / my_dpi, 400 / my_dpi), dpi=my_dpi)

# Plot do pH
plt.plot(df['Mês/Ano Referência'], df['pH'], marker='', color='black', linewidth=1.5)
plt.title('pH', fontsize=12, fontweight=0, color='black', loc='center')
plt.xlabel('Período', fontsize=6)
plt.ylabel('pH', fontsize=6, rotation=0)
plt.xticks(fontsize=4, rotation=70)
plt.yticks(fontsize=4)

# Add limits to Y axis
yinf, ysup = 5, 11
plt.ylim(yinf, ysup)

# Add lines for pH Parameters
plt.axhline(9.5, color='b', linestyle="dashdot")
plt.axhline(6, color='b', linestyle="dashdot")

st.pyplot()

# Gráfico do Cloro
my_dpi = 200
plt.figure(figsize=(1100 / my_dpi, 400 / my_dpi), dpi=my_dpi)

# Plot do pH
plt.plot(df['Mês/Ano Referência'], df['Cloro Livre (mg/l)'], marker='', color='black', linewidth=1.5)
plt.title('Cloro Livre (mg/l)', fontsize=12, fontweight=0, color='black', loc='center')
plt.xlabel('Período', fontsize=6)
plt.ylabel('Cloro Livre (mg/l)', fontsize=6, rotation=90)
plt.xticks(fontsize=4, rotation=70)
plt.yticks(fontsize=4)

# Add limits to Y axis
yinf, ysup = 0, 6
plt.ylim(yinf, ysup)

# Add lines for pH Parameters
plt.axhline(5, color='b', linestyle="dashdot")
plt.axhline(0.2, color='b', linestyle="dashdot")

st.pyplot()

# Gráfico do Flúor
my_dpi = 200
plt.figure(figsize=(1100 / my_dpi, 400 / my_dpi), dpi=my_dpi)

# Plot do Flúor
plt.plot(df['Mês/Ano Referência'], df['Flúor (mg/l)'], marker='', color='black', linewidth=1.5)
plt.title('Flúor (mg/l)', fontsize=12, fontweight=0, color='black', loc='center')
plt.xlabel('Período', fontsize=6)
plt.ylabel('Flúor (mg/l)', fontsize=6, rotation=90)
plt.xticks(fontsize=4, rotation=70)
plt.yticks(fontsize=4)

# Add limits to X and Y axis
yinf, ysup = 0, 1.5
plt.ylim(yinf, ysup)

# Add lines for Parameters
plt.axhline(0.9, color='b', linestyle="dashdot")
plt.axhline(0.6, color='b', linestyle="dashdot")

st.pyplot()

# Gráfico dos % Coliformes Totais
my_dpi = 200
plt.figure(figsize=(1100 / my_dpi, 400 / my_dpi), dpi=my_dpi)

# Plot do pH
plt.plot(df['Mês/Ano Referência'], df['% Coliformes Totais'], marker='', color='black', linewidth=1.5)
plt.title('Coliformes Totais (%)', fontsize=12, fontweight=0, color='black', loc='center')
plt.xlabel('Período', fontsize=6)
plt.ylabel('Coliformes Totais (%)', fontsize=6, rotation=90)
plt.xticks(fontsize=4, rotation=70)
plt.yticks(fontsize=4)

# Add limits to Y axis
yinf, ysup = 0, 10
plt.ylim(yinf, ysup)

# Add lines for pH Parameters
plt.axhline(5, color='b', linestyle="dashdot")
plt.axhline(0.1, color='b', linestyle="dashdot")

st.pyplot()

# Gráfico da Cor
my_dpi = 200
plt.figure(figsize=(1100 / my_dpi, 400 / my_dpi), dpi=my_dpi)

# Plot do pH
plt.plot(df['Mês/Ano Referência'], df['Cor (UC)'], marker='', color='black', linewidth=1.5)
plt.title('Cor (UC)', fontsize=12, fontweight=0, color='black', loc='center')
plt.xlabel('Período', fontsize=6)
plt.ylabel('Cor (UC)', fontsize=6, rotation=90)
plt.xticks(fontsize=4, rotation=70)
plt.yticks(fontsize=4)

# Add limits to X and Y axis
yinf, ysup = 0, 20
plt.ylim(yinf, ysup)

# Add lines for Parameters
plt.axhline(15, color='b', linestyle="dashdot")
plt.axhline(0.1, color='b', linestyle="dashdot")

st.pyplot()

# Gráfico da Turbidez
my_dpi = 200
plt.figure(figsize=(1100 / my_dpi, 400 / my_dpi), dpi=my_dpi)

# Plot do pH
plt.plot(df['Mês/Ano Referência'], df['Turbidez (NTU)'], marker='', color='black', linewidth=1.5)
plt.title('Turbidez (NTU)', fontsize=12, fontweight=0, color='black', loc='center')
plt.xlabel('Período', fontsize=6)
plt.ylabel('Turbidez (NTU)', fontsize=6, rotation=90)
plt.xticks(fontsize=4, rotation=70)
plt.yticks(fontsize=4)

# Add limits to X and Y axis
yinf, ysup = 0,10
plt.ylim(yinf, ysup)

# Add lines for Parameters
plt.axhline(5, color='b', linestyle="dashdot")
plt.axhline(0.1, color='b', linestyle="dashdot")

st.pyplot()