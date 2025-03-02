import os
import time

def main():
    menu_exibir = ['Cadastro de Rebanho', 'Cadastro de Lote', 'Manejo Sanitário', 'Reprodução', 'Produção Leiteira',
                   'Pesagem e Desenvolvimento', 'Registro de Movimentações', 'Registro de Insumos', 'Sair']
    menu_funcao = [cads_rebanho, cads_lote, cads_manejoSanit, cads_reproducao, cads_prodLeite, cads_pesoDesenv,
                   cads_financas, cads_insumo, sair]
    esperar = False
    while True:
        if esperar:
            input('ENTER para continuar ')
        esperar = True

        os.system('clear')
        for idx, cmd in enumerate(menu_exibir, 1):
            print(idx, ' => ', cmd, sep='')
        
        try:
            ent_usuario = int(input(' >>> ').strip())
            if not (ent_usuario - 1) in range(0, len(menu_exibir)):
                print('Número informado esta fora do intervalo esperado!!!')
                continue

        except ValueError:
            print('Informe um número!!!')
            continue

        esperar = False
        retorno = menu_funcao[ent_usuario - 1]()
        if retorno == 'sair':
            break

def cads_rebanho():
    os.system('clear')
    print('\tNovo cadastro de rebanho\n')
    nome = input('Nome: ')
    peso = input('Peso: ')
    idade = input('Idade: ')
    
    return
def cads_lote():
    pass
def cads_manejoSanit():
    pass
def cads_reproducao():
    pass
def cads_prodLeite():
    pass
def cads_pesoDesenv():
    pass
def cads_financas():
    pass
def cads_insumo():
    pass
def sair():
    return 'sair'

if __name__ == "__main__":
    main()
