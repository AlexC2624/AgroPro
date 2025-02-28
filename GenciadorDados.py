import csv

class Data:
    def __init__(self, nome_do_arquivo= 'dados.csv'):
        caminho = 'AgroPro/'
        self.arq_Path = caminho + nome_do_arquivo

    def __ler__(self):
        print(self.arq_Path)
        with open(self.arq_Path, 'a+', encoding= 'utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            txt_total = []
            for for_linha in leitor:
                txt_total.append(for_linha)
        return txt_total

if __name__ == '__main__':
    clase = Data()
    txt_salvo = clase.__ler__()
    print(txt_salvo)
    