import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Definir tamanho do conjunto de dados
n = 500  # Número de registros (clientes)

# Gerar dados 
np.random.seed(42)  # Para reprodutibilidade
dados_barbearia = {
    'Produto': np.random.choice(['Gel', 'Pomada'], size=n, p=[0.4, 0.6]),  # 40% Gel, 60% Pomada
    'Tipo_Corte': np.random.choice(['Infantil', 'Adulto'], size=n, p=[0.3, 0.7]),  # 30% Infantil, 70% Adulto
    'Forma_Pagamento': np.random.choice(['Cartão Crédito', 'Cartão Débito', 'Pix', 'Dinheiro'], 
                                         size=n, 
                                         p=[0.5, 0.3, 0.15, 0.05]),  # 50% Cartão Crédito, 30% Cartão Débito, 15% Pix, 5% Dinheiro
    'Dia_Semana': np.random.choice(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'], 
                                    size=n, 
                                    p=[0.1, 0.1, 0.15, 0.15, 0.2, 0.3])  # Distribuição de dias
}

# Criar DataFrame
df_barbearia = pd.DataFrame(dados_barbearia)

# Adicionando os nomes dos barbeiros
barbeiros = np.random.choice(['Thyago', 'Felipe', 'Ohana'], size=n, p=[0.6, 0.25, 0.15])
df_barbearia['Barbeiro'] = barbeiros

# Definindo preços para os produtos e cortes
preco_gel = 30.0  # Preço do gel
preco_pomada = 40.0  # Preço da pomada
preco_corte_adulto = 50.0  # Preço corte adulto
preco_corte_infantil = 40.0  # Preço corte infantil

df_barbearia['Faturamento'] = np.where(df_barbearia['Produto'] == 'Gel', preco_gel, preco_pomada) + \
                              np.where(df_barbearia['Tipo_Corte'] == 'Adulto', preco_corte_adulto, preco_corte_infantil)

# Gerar datas (mensais) para 4 anos
meses = pd.date_range(start='2020-01-01', periods=48, freq='ME')

# Gerar uma coluna de datas aleatórias correspondendo aos 4 anos
df_barbearia['Data'] = np.random.choice(meses, size=n)

# Agrupar o faturamento por mês
faturamento_mensal = df_barbearia.groupby(df_barbearia['Data'].dt.to_period('M'))['Faturamento'].sum()

# Ajustar faturamento para os meses de férias e outros
faturamento_mensal.loc['2020-12'] *= 1.5  # Aumentar faturamento de dezembro
faturamento_mensal.loc['2020-06'] *= 1.2  # Aumentar faturamento de junho
faturamento_mensal.loc['2020-07'] *= 1.2  # Aumentar faturamento de julho
faturamento_mensal.loc['2020-01'] *= 1.1  # Aumentar faturamento de janeiro
faturamento_mensal.loc['2020-02'] *= 1.1  # Aumentar faturamento de fevereiro

# Calcular as porcentagens de faturamento mensal
faturamento_mensal_normalizado = faturamento_mensal / faturamento_mensal.max() * 100

# Gráfico de faturamento mensal em porcentagem
plt.figure(figsize=(10, 6))
faturamento_mensal_normalizado.plot(kind='bar', color='#66b3ff')
plt.title('Faturamento Mensal da Barbearia (Porcentagem)')
plt.xlabel('Mês')
plt.ylabel('Faturamento Total (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráficos de média de faturamento por mês do ano em porcentagem
plt.figure(figsize=(10, 6))
faturamento_por_mes_ano = df_barbearia.groupby(df_barbearia['Data'].dt.month)['Faturamento'].mean()

# Ajuste
faturamento_por_mes_ano_normalizado = np.zeros(12)
faturamento_por_mes_ano_normalizado[0] = faturamento_por_mes_ano.loc[1] * 1.1  # Janeiro
faturamento_por_mes_ano_normalizado[1] = faturamento_por_mes_ano.loc[2] * 1.1  # Fevereiro
faturamento_por_mes_ano_normalizado[2] = faturamento_por_mes_ano.loc[3] * 0.8   # Março
faturamento_por_mes_ano_normalizado[3] = faturamento_por_mes_ano.loc[4] * 0.9   # Abril
faturamento_por_mes_ano_normalizado[4] = faturamento_por_mes_ano.loc[5] * 0.8   # Maio
faturamento_por_mes_ano_normalizado[5] = faturamento_por_mes_ano.loc[6] * 1.2   # Junho
faturamento_por_mes_ano_normalizado[6] = faturamento_por_mes_ano.loc[7] * 1.2   # Julho
faturamento_por_mes_ano_normalizado[7] = faturamento_por_mes_ano.loc[8] * 0.7   # Agosto
faturamento_por_mes_ano_normalizado[8] = faturamento_por_mes_ano.loc[9] * 0.6   # Setembro
faturamento_por_mes_ano_normalizado[9] = faturamento_por_mes_ano.loc[10] * 0.7  # Outubro
faturamento_por_mes_ano_normalizado[10] = faturamento_por_mes_ano.loc[11] * 0.8  # Novembro
faturamento_por_mes_ano_normalizado[11] = faturamento_por_mes_ano.loc[12] * 1.5  # Dezembro

# Normalizando para que dezembro seja 100
faturamento_por_mes_ano_normalizado = faturamento_por_mes_ano_normalizado / faturamento_por_mes_ano_normalizado.max() * 100

# Criar índice para os meses
meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# Gráfico de média de faturamento por mês do ano
plt.figure(figsize=(10, 6))
plt.bar(meses_nomes, faturamento_por_mes_ano_normalizado, color='#ff9999')
plt.title('Média de Faturamento por Mês do Ano (Porcentagem)')
plt.xlabel('Mês do Ano')
plt.ylabel('Faturamento Médio (%)')
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
axs[0, 0].bar(media_produtos.index, media_produtos.values / media_produtos.sum() * 100, color=['#ff9999','#66b3ff'])
axs[0, 0].set_title('Produto Mais Vendido (Gel vs Pomada)')
axs[0, 0].set_ylabel('Porcentagem (%)')

# Gráfico de Tipos de Corte
axs[0, 1].bar(media_cortes.index, media_cortes.values / media_cortes.sum() * 100, color=['#ffcc99','#99ff99'])
axs[0, 1].set_title('Tipo de Corte Mais Solicitado (Infantil vs Adulto)')
axs[0, 1].set_ylabel('Porcentagem (%)')

# Gráfico de Formas de Pagamento
axs[1, 0].bar(media_pagamentos.index, media_pagamentos.values / media_pagamentos.sum() * 100, color=['#c2c2f0','#ffb3e6','#c4e17f'])
axs[1, 0].set_title('Forma de Pagamento Mais Utilizada')
axs[1, 0].set_ylabel('Porcentagem (%)')

# Gráfico de Dias Mais Movimentados
axs[1, 1].bar(media_dias.index, media_dias.values / media_dias.sum() * 100, color=['#ffcc99','#99ff99', '#66b3ff', '#ff9999', '#ffb3e6', '#c2c2f0'])
axs[1, 1].set_title('Dias Mais Movimentados')
axs[1, 1].set_ylabel('Porcentagem (%)')

# Ajustar layout
plt.tight_layout()
plt.show()

# Contar cortes por barbeiro
cortes_por_barbeiro = df_barbearia['Barbeiro'].value_counts()

# Calcular porcentagem de cortes por barbeiro
cortes_por_barbeiro_porcentagem = cortes_por_barbeiro / cortes_por_barbeiro.sum() * 100

# Gráfico de cortes por barbeiro em porcentagem
plt.figure(figsize=(10, 6))
cortes_por_barbeiro_porcentagem.plot(kind='bar', color=['#66b3ff', '#ff9999', '#c2c2f0'])
plt.title('Porcentagem de Cortes por Barbeiro')
plt.xlabel('Barbeiro')
plt.ylabel('Porcentagem de Cortes (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Exibir médias e estatísticas descritivas
media_produtos, media_cortes, media_pagamentos, media_dias, faturamento_mensal.head(), faturamento_por_mes_ano.head()