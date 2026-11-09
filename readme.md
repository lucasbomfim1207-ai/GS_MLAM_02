# Global Solution - MLAM (2º Semestre)

## Desafio CitizenTech: Monitoramento de Mobilidade Urbana e Qualidade do Ar

### Integrantes e RM
- **Julia Johanson** - RM: 572220
- **Lucas Bomfim Leite** - RM: 570420
- **Eduardo Barcelos** - RM: 573274
- **Turma:** 1 CCPJ

---

## 1. Apresentação do Problema e Objetivo
O desafio **CitizenTech** propõe a utilização de tecnologia e análise de dados para solucionar problemas urbanos e melhorar a qualidade de vida nas cidades. Este projeto analisa a correlação entre a poluição atmosférica (Material Particulado PM2.5), o volume de tráfego veicular, a temperatura ambiente e o impacto direto no tempo de deslocamento dos cidadãos, além de prever alertas de poluição crítica através de modelos de Machine Learning e estatística applied.

---

## 2. Descrição da Base de Dados e Fonte
A base de dados utilizada (`dados_citizen_tech.csv` / `dados_citizen_tech.xlsx`) contém registros reais de monitoramento urbano contendo as seguintes variáveis:
- **id_medicao:** Identificador único da medição.
- **pm25:** Concentração de Material Particulado PM2.5 (µg/m³) [Quantitativa Contínua].
- **volume_trafego:** Volume médio de veículos por hora [Quantitativa Contínua].
- **temperatura:** Temperatura ambiente em graus Celsius (°C) [Quantitativa Contínua].
- **tempo_deslocamento:** Tempo médio de deslocamento na via em minutos [Quantitativa Contínua].
- **alerta_poluicao:** Indicador binário de poluição crítica (0 = Normal, 1 = Alerta Crítico) [Qualitativa Binária].

### Fonte dos Dados e Acesso Original
* **Fonte Primária:** Dados extraídos de portais de dados abertos de monitoramento ambiental e mobilidade urbana (plataforma **OpenAQ** e repositórios do **Portal Brasileiro de Dados Abertos**).
* **Endereço de Acesso Original:** [https://openaq.org/](https://openaq.org/) e [https://dados.gov.br/](https://dados.gov.br/)
* **Tratamento dos Dados:** A amostragem passou por procedimento de seleção e padronização das medições para 50 pontos de monitoramento viário de alta densidade, sem remoção de outliers ou inclusão de dados artificiais.

---

## 3. Estrutura do Repositório
- `dados_citizen_tech.csv`: Base de dados estruturada em formato CSV.
- `dados_citizen_tech.xlsx`: Base de dados estruturada em formato Excel.
- `analise_mlam.py`: Script em Python contendo todos os cálculos estatísticos, testes de hipóteses, regressões lineares (simples e múltipla), regressão logística e geração dos gráficos.
- `Relatório Estatístico - Global Solution MLAM.pdf`: Relatório estatístico completo com as análises, gráficos e interpretações.
- `Imagens/grafico_dispersao_simples.png`: Gráfico de dispersão com reta de regressão linear simples.
- `Imagens/grafico_correlacao_multivariada.png`: Matriz de correlação linear de Pearson (heatmap multivariado).
- `README.md`: Documentação oficial do projeto.

---

## 4. Visualizações e Resultados Gráficos

### Gráfico 01: Dispersão e Regressão Linear Simples (PM2.5 vs Tempo de Deslocamento)
![Dispersão e Regressão Simples](Imagens/grafico_dispersao_simples.png)

### Gráfico 02: Matriz de Correlação Linear de Pearson (Análise Multivariada)
![Matriz de Correlação Multivariada](Imagens/grafico_correlacao_multivariada.png)

---

## 5. Instruções de Execução
1. Certifique-se de possuir o Python instalado com as bibliotecas necessárias:
   ```bash
   pip install pandas numpy scipy statsmodels scikit-learn matplotlib seaborn
   ```
2. Execute o script de análise estatística para gerar os resultados e gráficos:
   ```bash
   python analise_mlam.py
   ```

---

## 6. Síntese dos Principais Resultados
- **Distribuição Normal:** A análise probabilística mostrou que a probabilidade de valores de PM2.5 estarem abaixo da média é de exatamente 50.00%, classificada como um evento provável.
- **Testes de Hipóteses:** Os testes paramétricos para a média confirmaram o comportamento amostral sob os níveis de significância de 6% e 9%.
- **Análise Bivariada:** Identificou-se uma forte correlação linear positiva entre a concentração de PM2.5 e o tempo de deslocamento ($r = 0.95$), evidenciando que vias mais congestionadas e poluídas geram maior retenção no trânsito.
- **Regressão Linear Múltipla:** O modelo multivariado demonstrou alta adequação ($R^2 \text{ Ajustado} > 0.90$), indicando que o tráfego e a poluição explicam de forma robusta a variação no tempo de trânsito.
- **Regressão Logística Binária:** Acurácia superior a 92% na predição de alertas críticos de poluição urbana, auxiliando gestores públicos na tomada de decisão em tempo real.

---

## 7. Limitações das Análises
O estudo baseia-se em uma amostra representativa de 50 pontos de monitoramento, sendo recomendada a expansão para bases contínuas de sensores IoT em tempo real para análises preditivas de longo prazo.