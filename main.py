from time import sleep

posicao = 0
saldo_total = 0

def linhas(tamanho=40, cor='\033[32m'):
    """
    Função para imprimir uma linha personalizada.
    :param tamanho: Define o comprimento da linha (padrão: 40).
    :param cor: Código ANSI para cor do texto (padrão: verde).
    """
    print(f"{cor}{'-' * tamanho}\033[m")

def depositos_realizados():
    global posicao
    global saldo_total

    linhas ()
    valor_depositado = float (input ('Digite o valor a ser depositado: '))
    depositos.append (valor_depositado)
    saldo_total += depositos [posicao]
    posicao += 1

    print (f'\033[36mDepositando o valor de R$ {valor_depositado:.2f}\nGuarde...\033[m')
    sleep (1)
    print ('\033[32mDepósito realizado com sucesso!!\033[m')

vezes_utilizadas = 0
depositos = []
limite = 500
numero_saques = 0
limite_saques = 3

menu = f"""\033[34m
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Sair\033[m

=> """

linhas()
print(f'\033[36m{'Bem-Vindo ao Banco do Brasil':^40}\033[m')
linhas()
print('Escolha uma opção para começarmos: ')

while True:
    if vezes_utilizadas == 0:
        opcao = input(menu).lower()
        vezes_utilizadas = 1

    else:
        linhas ()
        print('Escolha sua próxima operação: ')
        opcao = input (menu).lower()

    if opcao == 'd':
        depositos_realizados()

    elif opcao == 's':
        linhas ()

        sleep (1)

    elif opcao == 'e':
        linhas ()
        print (f'Depósitos realizados: ')
        for valores in depositos:
            print(f'R$ {valores}')
        sleep (1)

    elif opcao == 'l':
        linhas ()
        print('Obrigado pela sua preferência. Ótimo dia!')
        sleep (1)
        break

    else:
        print('Operação inválida, por favor selecione novamente a operção desejada.')
        sleep (1)
