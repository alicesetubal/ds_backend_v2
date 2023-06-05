import PyPDF2
def extrair_texto_pdf(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        texto = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            texto += page.extract_text()
    return texto

# Solicitar o caminho do arquivo PDF ao usuário
caminho_arquivo_pdf = input("Digite o caminho para o arquivo PDF: ")

# Extrair o texto do PDF
texto_pdf = extrair_texto_pdf(caminho_arquivo_pdf)

# Imprimir o texto extraído
print("Texto extraído do PDF:")
print(texto_pdf)