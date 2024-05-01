import pandas as pd
import plotly.express as px

# Carregar os dados do arquivo Excel
df = pd.read_excel('/home/willian/Documentos/Dados/BaseDados.xlsx')

# Criar um gráfico de dispersão com Plotly Express
fig = px.scatter(df, x='Data', y='Movimentação', color='Tipo', size='ID Produto')

# Mostrar o dashboard
fig.show()