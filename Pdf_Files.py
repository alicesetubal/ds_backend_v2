import PyPDF2

def extrair_texto_pdf(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        numPages= len(reader.pages)
        texto = ""
        for page in range(numPages):
            texto += reader.pages[page].extract_text()
            texto_pdf = extrair_texto_pdf(caminho_arquivo)
        return texto_pdf
    
       
    


print()