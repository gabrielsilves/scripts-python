import os
import pandas as pd


# Declaração da variável com o caminho do diretório
data_folder = r'CAMINHO DO DIRETÓRIO'

def merge_data(data_folder):
    # Lista para armazenar os DataFrames temporários
    frames = []

    # Itera sobre todos os arquivos na pasta especificada
    for filename in os.listdir(data_folder):
        # Verifica se o arquivo é um arquivo CSV
        if filename.endswith('.csv'):
            # Lê o arquivo CSV e o anexa ao DataFrame
            df = pd.read_csv(os.path.join(data_folder, filename))
            frames.append(df)
        # Verifica se o arquivo é um arquivo Excel (XLS ou XLSX)
        elif filename.endswith(('.xls', '.xlsx')):
            # Lê o arquivo Excel e o anexa ao DataFrame
            df = pd.read_excel(os.path.join(data_folder, filename))
            frames.append(df)

    # Concatena todos os DataFrames na lista
    all_data = pd.concat(frames, ignore_index=True)

    # Salva o DataFrame combinado em um novo arquivo CSV
    all_data.to_csv('union_files.csv', index=False, sep=";")
    print("Dados unidos com sucesso. Arquivo criado: 'union_files.csv'")

# Verifica se o script está sendo executado como principal
if __name__ == "__main__":
    # Chama a função para iniciar o processo de união dos dados
    merge_data(data_folder)
