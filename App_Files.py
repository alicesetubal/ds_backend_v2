import pandas as pd
import streamlit as st
import PyPDF2 
import io
import docx2txt

#Primeiro tenho que definir as funções para extrair o texto dos arquivos
def extract_text_csv(file_csv):
    data_frame = pd.read_csv(file_csv)
    texto = data_frame.to_string(index=False)
    return texto

def extract_text_xlsx(file_xlsx):
    data_frame = pd.read_excel(file_xlsx)
    texto = data_frame.to_string(index=False)
    return texto

    
def extract_text_pdf(file_pdf):
    reader= PyPDF2.PdfReader(file_pdf)
    numPages = len(reader.pages)
    texto= ''
    for page in range(numPages):
        texto += reader.pages[page].extract_text()
    return texto
        

def extract_text_txt(file_txt):
    texto = file_txt.getvalue().decode()
    return texto

def extract_text_docx(file_txt):
    texto = docx2txt.process(file_txt)
    return texto
    
st.header("Welcome to Extract File :smile:") 
#Local onde o utilizador irá adicionar o arquivo
arquivo = st.file_uploader('Insira seu arquivo' , type=['csv', 'xlsx', 'pdf', 'txt', 'docx'])

#Utilizei o if para verificar qual tipo de arquivo

if arquivo is not None:
    if arquivo.type == 'text/csv':
        
        texto = extract_text_csv(arquivo)
    
    elif arquivo.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
          texto = extract_text_xlsx(arquivo)
    
    elif arquivo.type == 'application/pdf':
          texto = extract_text_pdf(arquivo)
          
    elif arquivo.type == 'text/plain':
          texto = extract_text_txt(arquivo)
          
    elif arquivo.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        texto = extract_text_docx(arquivo)
        
else:
  
  st.stop()

st.header("O texto extraido foi:")
st.code(texto)



