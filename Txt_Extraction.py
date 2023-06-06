#abrir e ler o aquivo txt
with open('Arquivo.txt', 'r') as arquivo:
    text= arquivo.read()
print(text)

arquivo.close()