import csv

class Csv:
    def __init__(self):
        self.data = 'AgroPro/data.csv'
        
    def salvar(self, dados):
        with open(self.data, 'w', encoding='utf-8', newline='') as data:
            escritor = csv.writer(data)
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
            print(linha, coluna, sep='\n', end='\n\n')
            conteudo[linha, coluna] = substituir
            self.salvar(conteudo)
            print('Alterado com sucesso')

    def ler(self):
        with open(self.data) as a:
            leitor = csv.reader(a)
            cont_total = []
            cont_linha = []
            for linha in leitor:
                for elemento in linha:
                    cont_linha.append(elemento)
                cont_total.append(cont_linha)
                cont_linha = []
            return cont_total

if __name__ == '__main__':
    classe = Csv()
    #classe.salvar([['asdfhjk', 'sd53'],['as'], ['c', 's']])
    #dados = classe.ler()
    #print(dados[1:])
    classe.substituir('c', '12345678')
