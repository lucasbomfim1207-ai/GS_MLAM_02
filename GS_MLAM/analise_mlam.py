# ==========================================
# GLOBAL SOLUTION - MLAM (2º Semestre)
# Tema: CitizenTech - Monitoramento de Cidades Inteligentes (Mobilidade e Meio Ambiente)
# Integrantes: Julia Johanson (RM 572220), Lucas Bomfim Leite (RM 570420), Eduardo Barcelos (RM 573274)
# Turma: 1 CCPJ
# ==========================================

import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# 1. Carregamento dos Dados (Item 08.a)
print("--- 1. CARREGAMENTO DOS DADOS ---")
try:
    df = pd.read_csv('dados_citizen_tech.csv')
except FileNotFoundError:
    df = pd.read_excel('dados_citizen_tech.xlsx')
print(f"Base carregada com sucesso! Total de registros: {len(df)}")

# 2. Distribuição Normal de Probabilidade (Item 02)
print("\n--- 2. DISTRIBUIÇÃO NORMAL DE PROBABILIDADE ---")
variavel = df['pm25']
media = variavel.mean()
mediana = variavel.median()
desvio_padrao = variavel.std(ddof=1)

print(f"Média: {media:.4f}, Mediana: {mediana:.4f}, Desvio Padrão: {desvio_padrao:.4f}")

prob_menor_media = stats.norm.cdf(media, loc=media, scale=desvio_padrao)
print(f"a) P(X < Média) = {prob_menor_media:.4f} (50.00% - Evento Probável)")

prob_maior_mediana = 1 - stats.norm.cdf(mediana, loc=media, scale=desvio_padrao)
print(f"b) P(X > Mediana) = {prob_maior_mediana:.4f} ({(prob_maior_mediana*100):.2f}% - Evento Probável)")

# 3. Testes de Hipóteses para a Média (Item 03)
print("\n--- 3. TESTES DE HIPÓTESES PARA A MÉDIA ---")
# a) Média amostral menor que a populacional, alfa = 6%, n = 20
alpha_a = 0.06
n_a = 20
amostra_a = variavel.sample(n=n_a, random_state=42)
t_stat_a, p_val_a = stats.ttest_1samp(amostra_a, media, alternative='less')
print(f"a) Teste Inferior (alfa = {alpha_a}, n = {n_a}): t = {t_stat_a:.4f}, p = {p_val_a:.4f}")

# b) Média amostral maior que a populacional, alfa = 9%, n = 25
alpha_b = 0.09
n_b = 25
amostra_b = variavel.sample(n=n_b, random_state=123)
t_stat_b, p_val_b = stats.ttest_1samp(amostra_b, media, alternative='greater')
print(f"b) Teste Superior (alfa = {alpha_b}, n = {n_b}): t = {t_stat_b:.4f}, p = {p_val_b:.4f}")

# 4. Análise Bivariada (Item 04)
print("\n--- 4. ANÁLISE BIVARIADA ---")
x_biv = df['pm25']
y_biv = df['tempo_deslocamento']

cov_biv = np.cov(x_biv, y_biv)[0, 1]
corr_biv, p_corr_biv = stats.pearsonr(x_biv, y_biv)
print(f"Covariância: {cov_biv:.4f} | Correlação de Pearson (r): {corr_biv:.4f} (p: {p_corr_biv:.4e})")

slope, intercept, r_value, p_value, std_err = stats.linregress(x_biv, y_biv)
r_squared = r_value ** 2
print(f"Regressão Simples: y = {intercept:.4f} + {slope:.4f} * x | R² = {r_squared:.4f}")

# Salvar Gráfico de Dispersão e Regressão Simples (Item 04.a e 04.d)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x_biv, y=y_biv, color='blue', label='Dados Reais')
plt.plot(x_biv, intercept + slope * x_biv, color='red', label=f'Regressão: y = {intercept:.2f} + {slope:.2f}x')
plt.title('Gráfico 01: Dispersão e Regressão Linear Simples (PM2.5 vs Tempo)')
plt.xlabel('Concentração de PM2.5 (ug/m^3)')
plt.ylabel('Tempo de Deslocamento (minutos)')
plt.legend()
plt.tight_layout()
plt.savefig('grafico_dispersao_simples.png', dpi=300)
plt.close()

pm25_pred = 25.0
pred_tempo = intercept + slope * pm25_pred
print(f"Previsão (PM2.5 = 25.0): {pred_tempo:.2f} minutos")

# 5. Regressão Linear Múltipla (Item 05)
print("\n--- 5. REGRESSÃO LINEAR MÚLTIPLA ---")
X_mult = df[['pm25', 'volume_trafego', 'temperatura']]
X_mult = sm.add_constant(X_mult)
y_mult = df['tempo_deslocamento']

mat_corr = X_mult.corr()
print("Matriz de Correlação Multivariada:")
print(mat_corr)

# Salvar Heatmap da Correlação Multivariada (Item 05.c)
plt.figure(figsize=(8, 6))
sns.heatmap(mat_corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Gráfico 02: Matriz de Correlação Linear de Pearson (Multivariada)')
plt.tight_layout()
plt.savefig('grafico_correlacao_multivariada.png', dpi=300)
plt.close()

modelo_mult = sm.OLS(y_mult, X_mult).fit()
print(modelo_mult.summary())

novo_dado_mult = pd.DataFrame({'const': [1], 'pm25': [25.0], 'volume_trafego': [1500], 'temperatura': [25.0]})
pred_mult = modelo_mult.predict(novo_dado_mult)[0]
print(f"Previsão Múltipla: {pred_mult:.2f} minutos")

# 6. Regressão Logística Binária (Item 06)
print("\n--- 6. REGRESSÃO LOGÍSTICA BINÁRIA ---")
X_log = df[['pm25', 'volume_trafego', 'temperatura']]
X_log = sm.add_constant(X_log)
y_log = df['alerta_poluicao']

modelo_log = sm.Logit(y_log, X_log).fit(disp=False)
print(modelo_log.summary())

y_pred_prob = modelo_log.predict(X_log)
y_pred_bin = (y_pred_prob >= 0.5).astype(int)

mat_conf = confusion_matrix(y_log, y_pred_bin)
acuracia = accuracy_score(y_log, y_pred_bin)
print("Matriz de Confusão:")
print(mat_conf)
print(f"Acurácia: {acuracia*100:.2f}%")

novo_dado_log = pd.DataFrame({'const': [1], 'pm25': [28.0], 'volume_trafego': [1700], 'temperatura': [27.0]})
prob_alerta = modelo_log.predict(novo_dado_log)[0]
classificacao = 1 if prob_alerta >= 0.5 else 0
print(f"Previsão Logística (PM2.5=28, Tráfego=1700, Temp=27): Probabilidade de Alerta = {prob_alerta*100:.2f}% (Classe: {classificacao})")
print("\n--- FIM DA ANÁLISE ---")