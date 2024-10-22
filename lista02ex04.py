import json

def listar(dicionario):
    if 'filhos' not in dicionario:
        print(dicionario['nome'])
        return
    else:
        print(dicionario['nome'])
        for filho in dicionario['filhos']:
            listar(filho)

with open('familia5.json', 'r', encoding='utf-8') as arquivo:
    familia = json.load(arquivo)

listar(familia)