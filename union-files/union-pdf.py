import PyPDF2

# Lista de caminhos dos arquivos PDF que serão unidos
pdf_files = [
    r'PATH',
    r'PATH'
    #r'C:\Users\Gabriel\Downloads\SIMPLES 02 2023.pdf'
]

# Criar um objeto PdfMerger da PyPDF2
pdf_merger = PyPDF2.PdfMerger()

# Adicionar os arquivos PDF ao objeto PDFMerger
for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as file:
        pdf_merger.append(file)

# Salvar o arquivo PDF unido
with open('arquivo_merge.pdf', 'wb') as file:
    pdf_merger.write(file)

print("Arquivos PDF unidos com sucesso!")