import os

def main():
    conjunto_path = os.getcwd() + '/conjunto.txt'
    desconsiderar_path = os.getcwd() + "/desconsiderar.txt"

    texts_path = listWordsOnFile(conjunto_path)
    desconsiderar = listWordsOnFile(desconsiderar_path)

    dicio = genIndices(texts_path, desconsiderar)

    testeBusca = ['amor', 'casar']
    searchOnIndeces(dicio, testeBusca)
    

# def generate_conjunto(conjunto_path: str):
#     """Gera um arquivo 'conjunto.txt' com o caminho para todos os arquivos no diretorio indicado"""
#
#     with open(conjunto_path, 'w') as conjunto:
#         for dir, subdirs, files in os.walk('texts'):
#             for file in files:
#                 conjunto.write( dir + '/' + file + "\n")

def listWordsOnFile(path: str):
    """Retona uma lista com todas as palavras contida em um arquivo"""

    list = []

    with open(path, 'r') as file:
        for line in file:
            for word in line.split():
                list.append(word)

    return list

def genIndices(arqs: str, desconsidera: list):
    """"Gera um arquivo de indices e retorna um dicionario com os indices"""

    dicio = {}
    ind = 1
    for a in arqs:
        arq = open(a, 'r')
        for linha in arq:
            palavra = linha.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('@', '').split()
            for pl in palavra:
                if pl not in desconsidera:
                    if pl in dicio:
                        if ind in dicio[pl]:
                            dicio[pl][ind] += 1 
                        else:
                            dicio[pl].update({ind:1})
                    else:
                        dicio.update({pl:{ind:1}})
        ind += 1

    # Gera arquivo indices.txt
    dicio = dict(sorted(dicio.items()))
    ind_arq = open('indices.txt', 'w')
    for key, val in dicio.items():
        ind_arq.write(f'{key}:')
        for v, o in val.items():
            ind_arq.write(f' {v},{o}')
        ind_arq.write('\n')

    ind_arq.close()

    return dicio

def searchOnIndeces(dicio: dict, busca: list):
    """"""


    dicioTeste = dicio.items()
    resp = []

    for word in busca:
        for item in dicioTeste:
            if word in item:
                resp.append(item)

    respD = dict(resp)
    a = ''

    print(respD)





if __name__ == '__main__':
    main()