import csv

class MyCsv:
    def __init__(self):
        self.data = 'AgroPro/data.csv'
        
    def salvar(self, dados):
        with open(self.data, 'w', encoding='utf-8', newline='') as data:
            escritor = MyCsv.writer(data)
            escritor.writerows(dados)
    
    def procurar(self, procurar):
        with open(self.data, 'r', encoding='utf-8', newline='') as data:
            leitor = csv.reader(data)

            dados_armazenados = []
            for linha in leitor:
                dados_armazenados.append(linha)
            print('tessste', dados_armazenados)

            n_lin, n_col = 0, 0
            for linha in dados_armazenados:
                for valor in linha:
                    print('test:', valor, '==', procurar)
                    if valor == procurar:
                        return n_lin, n_col

                    n_col += 1
                n_lin += 1
                n_col = 0
            return None, 'Não encontrado'

    def substituir(self, procurar, substituir):
        linha, coluna = self.procurar(procurar)
        if not linha:
            print(coluna)
        else:
            conteudo = self.ler()
            print('cooont', conteudo)
            print(f'Endereço encontrado: ({linha}, {coluna})')
            conteudo[linha, coluna] = substituir
            self.salvar(conteudo)
            print('Alterado com sucesso')

    def ler(self):
        try:
            with open(self.data, mode='r', encoding='utf-8', newline='') as a:
                leitor = csv.reader(a)
                # print(leitor)
                total = []
                linha = []
                for for_linha in leitor:
                    for elemento in for_linha:
                        linha.append(elemento)
                    total.append(for_linha)
                    linha = []
                return total
        except:
            print('Ocoreu erro durante a leitura do arquivo')

if __name__ == '__main__':
    classe = MyCsv()
    #classe.salvar([['asdfhjk', 'sd53'],['as'], ['c', 's']])
    dados = classe.ler()
    for linha in dados:
        print(linha)
    print('----------////-----------------////------------------')
    classe.substituir('c', '12345678')
