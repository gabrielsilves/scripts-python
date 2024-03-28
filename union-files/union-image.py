from PIL import Image
import img2pdf
from PyPDF2 import PdfMerger

# Lista de caminhos das imagens
image_files = [r'PATH', 
               r'PATH']


# Tamanho do A4 em pixels a 300 DPI
a4_size_in_pixels = (2480, 3508)

# Função para redimensionar a imagem mantendo proporção e preenchendo o tamanho A4
def resize_and_fill_image(image_path, output_size, temp_path):
    with Image.open(image_path) as img:
        # Manter a proporção e redimensionar para que a menor dimensão corresponda ao A4
        img_ratio = img.width / img.height
        a4_ratio = output_size[0] / output_size[1]

        if img_ratio > a4_ratio:
            # A imagem é mais larga que A4
            new_height = output_size[1]
            new_width = int(new_height * img_ratio)
        else:
            # A imagem é mais alta que A4
            new_width = output_size[0]
            new_height = int(new_width / img_ratio)

        img = img.resize((new_width, new_height))

        # Cortar/calcular o centro da imagem
        left = (new_width - output_size[0]) / 2
        top = (new_height - output_size[1]) / 2
        right = (new_width + output_size[0]) / 2
        bottom = (new_height + output_size[1]) / 2

        img = img.crop((left, top, right, bottom))

        # Salvar a imagem ajustada temporariamente
        img.save(temp_path, "JPEG")

# Caminhos temporários para as imagens ajustadas
temp_image_files = ['temp1.jpg', 'temp2.jpg']

# Ajustar as imagens e salvar temporariamente
for image_file, temp_file in zip(image_files, temp_image_files):
    resize_and_fill_image(image_file, a4_size_in_pixels, temp_file)

# Converter as imagens ajustadas para PDF no tamanho A4
with open("imagens_a4.pdf", "wb") as f:
    f.write(img2pdf.convert(temp_image_files))

print("Imagens convertidas para o formato A4 e unidas em um arquivo PDF com sucesso!")