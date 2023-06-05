import PyPDF2

# Abre o arquivo PDF
pdf_file = open('/mnt/c/Users/ana.a.almeida/Documents/TestePDF.pdf', 'rb')

# Cria um objeto PdfReader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Obtém o número total de páginas
num_pages = len(pdf_reader.pages)

# Itera sobre as páginas do PDF
#for page_num in range(num_pages):
    # Obtém o objeto da página
page_num = 1
page = pdf_reader.pages[page_num]
   
    # Extrai o texto da página
text = page.extract_text()
    
    
    # Imprime o texto da página
print(f"Texto da página {page_num + 1}:")
print(text)
    




