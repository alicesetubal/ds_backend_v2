import xml.etree.ElementTree as ET

# Carregue o arquivo XML
tree = ET.parse('Arquivos/Arquivo.xml')

# Obter a raiz do XML
root = tree.getroot()



# Crie uma função recursiva para percorrer os elementos e extrair o texto
def extrair_texto(elemento):
    texto = elemento.text.strip() if elemento.text else ''
    for filho in elemento:
        texto += extrair_texto(filho)
    return texto

# Extraia o texto do XML
texto_extrato = extrair_texto(root)

# Imprima o texto extraído
print(texto_extrato)
