import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Definir tamanho do conjunto de dados
n = 500  # Número de registros (clientes)

# Gerar dados aleatórios
np.random.seed(42)  # Para reprodutibilidade
dados_barbearia = {
    'Produto': np.random.choice(['Gel', 'Pomada'], size=n, p=[0.4, 0.6]),  # 40% Gel, 60% Pomada
    'Tipo_Corte': np.random.choice(['Infantil', 'Adulto'], size=n, p=[0.3, 0.7]),  # 30% Infantil, 70% Adulto
    'Forma_Pagamento': np.random.choice(['Cartão', 'Dinheiro', 'Pix'], size=n, p=[0.5, 0.3, 0.2]),  # 50% Cartão, 30% Dinheiro, 20% Pix
    'Dia_Semana': np.random.choice(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'], size=n, p=[0.1, 0.1, 0.15, 0.15, 0.2, 0.3])  # Distribuição de dias
}

# Criar DataFrame
df_barbearia = pd.DataFrame(dados_barbearia)

# Adicionando os nomes dos barbeiros
barbeiros = np.random.choice(['Thyago', 'Jhonatan', 'Ohana'], size=n, p=[0.6, 0.2, 0.2])  # Thyago corta mais
df_barbearia['Barbeiro'] = barbeiros

# Definindo preços para os produtos e cortes
preco_gel = 30.0  # Preço do gel
preco_pomada = 40.0  # Preço da pomada
preco_corte_adulto = 50.0  # Preço corte adulto
preco_corte_infantil = 40.0  # Preço corte infantil

df_barbearia['Faturamento'] = np.where(df_barbearia['Produto'] == 'Gel', preco_gel, preco_pomada) + \
                              np.where(df_barbearia['Tipo_Corte'] == 'Adulto', preco_corte_adulto, preco_corte_infantil)

# Gerar datas (mensais) para 4 anos
meses = pd.date_range(start='2019-01-01', periods=48, freq='ME')  # Alterado para 'ME'

# Gerar uma coluna de datas aleatórias correspondendo aos 4 anos
df_barbearia['Data'] = np.random.choice(meses, size=n)

# Agrupar o faturamento por mês
faturamento_mensal = df_barbearia.groupby(df_barbearia['Data'].dt.to_period('M'))['Faturamento'].sum()

# Ajustar faturamento para os meses de férias
faturamento_mensal.loc['2019-12'] *= 2  # Dobrar faturamento de dezembro
faturamento_mensal.loc['2019-06'] *= 1.5  # Aumentar faturamento de junho em 50%
faturamento_mensal.loc['2019-07'] *= 1.5  # Aumentar faturamento de julho em 50%

# Gráfico de faturamento mensal ao longo de 4 anos
plt.figure(figsize=(10, 6))
faturamento_mensal.plot(kind='bar', color='#66b3ff')
plt.title('Faturamento Mensal da Barbearia (Comparação entre Meses)')
plt.xlabel('Mês')
plt.ylabel('Faturamento Total (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Comparação entre os meses do ano (média)
faturamento_por_mes_ano = df_barbearia.groupby(df_barbearia['Data'].dt.month)['Faturamento'].mean()

# Ajustar média de faturamento para os meses de férias
faturamento_por_mes_ano.loc[6] *= 1.5  # Aumentar média de junho em 50%
faturamento_por_mes_ano.loc[7] *= 1.5  # Aumentar média de julho em 50%
faturamento_por_mes_ano.loc[12] *= 2   # Dobrar média de dezembro

# Ajustar média de faturamento para os meses de fevereiro a abril
faturamento_por_mes_ano.loc[2] *= 0.8  # Diminuir média de fevereiro em 20%
faturamento_por_mes_ano.loc[3] *= 0.85  # Diminuir média de março em 15%
faturamento_por_mes_ano.loc[4] *= 0.9  # Diminuir média de abril em 10%

# Ajustar média de faturamento para os meses de agosto a outubro
faturamento_por_mes_ano.loc[8] *= 0.72 # Diminuir média de fevereiro em 28%
faturamento_por_mes_ano.loc[9] *= 0.7  # Diminuir média de março em 30%
faturamento_por_mes_ano.loc[10] *= 0.64 # Diminuir média de abril em 36%

# Gráfico de comparação entre meses do ano (média)
plt.figure(figsize=(10, 6))
faturamento_por_mes_ano.index = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
faturamento_por_mes_ano.plot(kind='bar', color='#ff9999')
plt.title('Média de Faturamento por Mês do Ano')
plt.xlabel('Mês do Ano')
plt.ylabel('Faturamento Médio (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Estatísticas descritivas dos produtos, cortes, formas de pagamento e dias
media_produtos = df_barbearia['Produto'].value_counts()
media_cortes = df_barbearia['Tipo_Corte'].value_counts()
media_pagamentos = df_barbearia['Forma_Pagamento'].value_counts()
media_dias = df_barbearia['Dia_Semana'].value_counts()

# Gráficos de análise de produtos, cortes, pagamentos e dias da semana
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico de Produtos
axs[0, 0].bar(media_produtos.index, media_produtos.values, color=['#ff9999','#66b3ff'])
axs[0, 0].set_title('Produto Mais Vendido (Gel vs Pomada)')
axs[0, 0].set_ylabel('Quantidade')

# Gráfico de Tipos de Corte
axs[0, 1].bar(media_cortes.index, media_cortes.values, color=['#ffcc99','#99ff99'])
axs[0, 1].set_title('Tipo de Corte Mais Solicitado (Infantil vs Adulto)')
axs[0, 1].set_ylabel('Quantidade')

# Gráfico de Formas de Pagamento
axs[1, 0].bar(media_pagamentos.index, media_pagamentos.values, color=['#c2c2f0','#ffb3e6','#c4e17f'])
axs[1, 0].set_title('Forma de Pagamento Mais Utilizada')
axs[1, 0].set_ylabel('Quantidade')

# Gráfico de Dias Mais Movimentados
axs[1, 1].bar(media_dias.index, media_dias.values, color=['#ffcc99','#99ff99', '#66b3ff', '#ff9999', '#ffb3e6', '#c2c2f0'])
axs[1, 1].set_title('Dias Mais Movimentados')
axs[1, 1].set_ylabel('Quantidade')

# Ajustar layout
plt.tight_layout()
plt.show()

# Contar cortes por barbeiro
cortes_por_barbeiro = df_barbearia['Barbeiro'].value_counts()

# Gráfico de cortes por barbeiro
plt.figure(figsize=(10, 6))
cortes_por_barbeiro.plot(kind='bar', color=['#66b3ff', '#ff9999', '#c2c2f0'])
plt.title('Número de Cortes por Barbeiro')
plt.xlabel('Barbeiro')
plt.ylabel('Número de Cortes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Exibir médias e estatísticas descritivas
media_produtos, media_cortes, media_pagamentos, media_dias, faturamento_mensal.head(), faturamento_por_mes_ano.head()