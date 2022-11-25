import os

def main():
    conjunto_path = os.getcwd() + '/conjunto.txt'
    desconsiderar_path = os.getcwd() + "/desconsiderar.txt"

    texts_path = listWordsOnFile(conjunto_path)
    desconsiderar = listWordsOnFile(desconsiderar_path)

    dicio = genIndices(texts_path, desconsiderar)

    testeBusca = ['bom']
    searchOnIndices(dicio, testeBusca, texts_path)

# def generate_conjunto(conjunto_path: str):
#     """Gera um arquivo 'conjunto.txt' com o caminho para todos os arquivos no diretorio indicado"""
#
#     with open(conjunto_path, 'w') as conjunto:
#         for dir, subdirs, files in os.walk('texts'):
#             for file in files:
#                 conjunto.write( dir + '/' + file + "\n")

def listWordsOnFile(path: str) -> list:
    """
    Retona uma lista com todas as palavras contida em um arquivo
    
    :param path: str

    :return list
    """

    list = []

    with open(path, 'r') as file:
        for line in file:
            for word in line.split():
                list.append(word)

    return list

def genIndices(arqs_path: list, desconsidera: list) -> dict:
    """
    Gera um arquivo de indices e retorna um dicionario com os indices
    
    :param arqs: list
    :param desconsidera: list

    :return dict    
    """

    dicio = {}
    ind = 1
    for arq_path in arqs_path:
        with open(arq_path, 'r') as arq:
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
    
    with open('indices.txt', 'w') as ind_arq:   
        for key, val in dicio.items():
            ind_arq.write(f'{key}:')
            for v, o in val.items():
                ind_arq.write(f' {v},{o}')
            ind_arq.write('\n')

    return dicio
    
def searchOnIndices(dicio: dict, busca: list, names: list) -> list:
    """
    Gera um arquivo informando quantos arquivos contém as palavras de busca e seus respectivos nomes.
    Retorna uma lista indicando qual arquivo contém as palavras de busca.
    
    :param dicio: dict
    :param busca: list

    :return list    
    """
    i = 0
    a = []
    b = []

    for word in busca:
        if word in dicio:
            inds = dicio[word]
            b = [k for k in inds]
            if i == 0:
                a = b.copy()
            else:
                a = [i for i in a if i in b]
            b.clear()
            i += 1

    print(a)
    # Cria o arquivo 'resposta.txt' e escreve quantos e 
    # quais arquivos possuem as palavras de busca
    with open('resposta.txt', 'w') as arq:
        arq.write(str(len(a))+'\n')
        for i in a:
            arq.write(names[i-1]+'\n')
    

if __name__ == '__main__':
    main()