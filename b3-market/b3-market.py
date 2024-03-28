import pandas as pd 

# Caminho do arquivo
file_path = r"C:\Users\Gabriel\Downloads\03-01-2024_NEGOCIOSAVISTA\03-01-2024_NEGOCIOSAVISTA.txt"

# Carregando o DataFrame do arquivo CSV
df = pd.read_csv(file_path, delimiter=";")

# Filtrando o DataFrame
df_dolar = df[df['CodigoInstrumento'] == 'DOLG24']

# Exibindo as primeiras linhas do DataFrame filtrado
print(df_dolar)

