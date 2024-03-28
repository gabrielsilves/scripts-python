import tabula
import pandas as pd

# Definir o caminho para o arquivo PDF que você deseja converter
pdf_file = r"PATH\\file.pdf"

# Converter o arquivo PDF em uma lista de dataframes do pandas
dfs = tabula.read_pdf(pdf_file, pages="all", encoding="ISO-8859-1")

# Concatenar os dataframes em um único dataframe
df = pd.concat(dfs)

# Salvar o dataframe em um arquivo Excel
df.to_excel(r"PATH\\file.xlsx", index=False)
print(df)