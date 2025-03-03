
class Gerenciador:
    def __init__(self, nome_do_banco):
        """

        Args:
            nome_do_banco (string): O nome do banco de dados a ser manipulado.
        """
        pass
    def salvar_registro(self, valores):
        """
        Ajusta os dados para serem salvos

        Args:
            volores (list[list]): Cada lista dentro da lista representa uma linha.
        """
        sucesso = False
        try:
            print(valores)
            banco = Banco('data.csv')
            print(banco.ler())
            input()
            sucesso = True
        except:
            sucesso = []
        return sucesso

class Banco:
    def __init__(self, nome_banco_data):
        self.banco_nome = nome_banco_data
    def ler(self):
        try:
            with open(self.banco_nome, 'r') as arquivo_r:
                return arquivo_r.read()
        except FileNotFoundError:
            with open(self.banco_nome, 'w') as arquivo_w:
                arquivo_w.write('1')
            return 'escrita'
                
    def escrever(self):
        pass
