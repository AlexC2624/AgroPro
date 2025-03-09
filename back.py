
class Gerenciador:
    def __init__(self, nome_do_banco):
        """
        Args:
            nome_do_banco (string): O nome do banco de dados a ser manipulado.
        """
        self.cBanco = Banco(nome_do_banco)

    def verif_duplicidade(self, coluna, valor):
        """
        Args:
            coluna (int): Id da coluna a procurar no arquivo.
            valor (strg/int): Pode ser uma string ou um integer que será para comparar.
        
        Returns:
            list: Lista com as linhas em que foi encontrado.
        """
        try:
            dados_salvos = self.cBanco.ler()
            cont_linha = 0  # Indica a linha atual dentro do for
            ocorencias = [] # Armazena as ocoerencias
            for linha in dados_salvos:
                if linha[coluna] == valor:
                    ocorencias.append(cont_linha)
                cont_linha += 1
            return ocorencias
        except FileNotFoundError:
            return []
        
    def salvar_registro(self, valores, verificar_duplicidade=[None]):
        """
        Verifica se foi informado os valores a verificar a duplicidade
            - True
                - Consulta os registros
                - Inicia o loop para cada elemento a verificar a duplicidade
                    - Verifica os dados que devem ser únicos
                        - Dados
                            - Verifica se os dados já estão salvos
                                - True
                                    - Cria uma mensagem de erro personalizada para o caso
                                    - Armazena a mensagem
                                    - Volta para o início do loop
                                - False
                                    - Volta para o início do loop
                - Salva/Adiciona os dados n arquivo data
        Args:
            valores (list): Lista com os dados a serem salvos, a lista representa a linha.
            verificar_duplicidade (list, optional): Índices das colunas para verificar duplicatas. Defaults to None.
        
        Returns:
            str: Uma mensagem se deu certo ou se deu erro, retorna a mensagem com o erro.
        """
        erros = []
        if verificar_duplicidade != [None]:
            for idx in verificar_duplicidade:
                resultado = self.verif_duplicidade(idx, valores[idx])
                if resultado != []:
                    erros.append()

class Banco:
    def __init__(self, nome_banco_data):
        self.banco_nome = nome_banco_data
    def ler(self):
        """Lê o arquivo csv

        Returns:
            list[list]: Cada linha estará dentro da lista que, por sua vez estará dentro da da lista principal.

        Raises:
            FileNotFoundError: Pode retornar se o arquivo não existir.
        """
        with open(self.banco_nome, 'r') as arquivo_r:
            return arquivo_r.read()
                
    def adicionar(self, dados):
        """
        Args:
            dados (list[list]): Dados para serem escritos no arquivo
        """
        with open(self.banco_nome, 'a') as arquivo_w:
            for linha in dados:
                arquivo_w.write(linha + ', ')
            arquivo_w.write('\n')

###########################################

if __name__ == '__main__':
    