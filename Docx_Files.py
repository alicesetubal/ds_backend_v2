import docx2txt
import pydocx

def extract_txt_docx():
  texto = docx2txt.process('Arquivos/documento.docx')
  return texto

print(extract_txt_docx())


