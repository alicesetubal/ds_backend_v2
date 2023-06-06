import streamlit as st
import PyPDF2 
st.title("Olá")

arquivo= st.file_uploader("Adicione seu arquivo", type =['xml', 'pdf', ' txt'] )

if arquivo:
    print(arquivo.loads)
    print(arquivo.read)
    match arquivo.type:
        case 'pdf':
         def extrair_texto_pdf(arquivo):
          with open(arquivo, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            texto = ''
          for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            texto += page.extract_text()
            return texto
else:
    None          