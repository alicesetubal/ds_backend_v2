import pandas as pd
import streamlit as st
import PyPDF2 


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
    with open(file_pdf, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        texto = ''
        for page in reader.pages:
            texto += page.extract_text()
    return texto
    
#Local onde o utilizador irá adicionar o arquivo
arquivo = st.file_uploader('Insira seu arquivo' , type=['csv', 'xlsx', 'pdf'])

#Utilizei o if para verificar qual tipo de arquivo

if arquivo is not None:
    if arquivo.type == 'text/csv':
        texto = extract_text_csv(arquivo)
    
    elif arquivo.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
          texto = extract_text_xlsx(arquivo)
    
    elif arquivo.type == 'pdf':
        texto = extract_text_pdf(arquivo)
else:
  st.stop()

st.header("O texto extraido foi:")
#st.write(texto)
st.code(texto)



