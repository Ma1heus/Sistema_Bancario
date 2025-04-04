from time import sleep

posicao = 0 #arrumar isso depois


def linhas(tamanho=40, cor='\033[32m'):
    """
    Função para imprimir uma linha personalizada.
    :param tamanho: Define o comprimento da linha (padrão: 40).
    :param cor: Código ANSI para cor do texto (padrão: verde).
    """
    print(f"{cor}{'-' * tamanho}\033[m")


def menu () :
    menu = f"""\033[34m
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [l] Sair\033[m

    => """
    return input (menu).lower()


def depositos_realizados(saldo, extrato):
    global posicao

    linhas ()
    valor_depositado = float (input ('Digite o valor a ser depositado: '))
    linhas ()
    if valor_depositado > 0:
        extrato += f'\nDepósito: \033[32m{f'R$ {valor_depositado:.2f}':^15}\033[m'
        saldo += valor_depositado
        posicao += 1
        print (f'\033[36mDepositando o valor de R$ {valor_depositado:.2f}\nGuarde...\033[m')
        sleep (1)
        print ('\033[32mDepósito realizado com sucesso!!\033[m')
    else:
        print('\033[31m Operação falhou! O valor informado é inválido.\033[m')

    return saldo, extrato


def saques(*, saldo, extrato, numero_saques):
    linhas ()
    valor_saque = float (input ('Informe o valor do saque: '))
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > 500
    excedeu_saque = numero_saques >= 3
    numero_saques += 1

    if excedeu_saque:
        print('\033[31m Operação falhou! Limite de saque diário atingido.\033[m')
    elif excedeu_limite:
        print ('\033[31m Operação falhou! O valor excedeu o limite permitido.\033[m')
    elif excedeu_saldo:
        print ('\033[31m Operação falhou! O valor excedeu o saldo disponível.\033[m')
    else:
        saldo -= valor_saque
        print(f'\033[32mSaque Autorizado!\033[m')
        sleep (1)
        extrato += f'\nSaque: \033[31m{f'- R$ {valor_saque:.2f}':^18}\033[m'

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    linhas()
    print('Não foram realizadas movimentações.' if not extrato else f'Extrato Completo:\n {extrato}')
    print(f'\nSaldo:\t\033[33m{f'R$ {saldo:.2f}':^19}\033[m')
    sleep(1)


def criar_usuario(usuarios):
    linhas()
    cpf = input('Informe o CPF (somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n\033[31mJá existe usuário com esse CPF!\033[m')

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro/bairro - cidade/sigla estado): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print('\033[33mUsuário criado com sucesso!\033[m')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    linhas()
    cpf = input('Digite seu CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[32mConta criada com sucesso!\033[m")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n\033[31mUsuário não encontrado, fluxo de criação de conta encerrado! \033[m")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        linhas()
        print(linha)


def main():
    AGENCIA = "0001"
    saldo = 0
    vezes_utilizadas = 0
    extrato = ''
    usuarios = []
    contas = []
    numero_saques = 0

    linhas()
    print(f'\033[36m{'Bem-Vindo ao Banco do Brasil':^40}\033[m')
    linhas()
    print('Escolha uma opção para começarmos: ')

    while True:
        if vezes_utilizadas == 0:
            opcao = menu()
            vezes_utilizadas = 1

        else:
            linhas ()
            print('Escolha sua próxima operação: ')
            opcao = menu()

        if opcao == 'd':
            saldo, extrato = depositos_realizados(saldo, extrato)

        elif opcao == 's':
            saldo, extrato = saques(saldo=saldo, extrato=extrato, numero_saques=numero_saques)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario (usuarios)

        elif opcao == 'nc':
            numero_conta = len (contas) + 1
            conta = criar_conta (AGENCIA, numero_conta, usuarios)

            if conta :
                contas.append (conta)

        elif opcao == 'lc' :
            listar_contas (contas)

        elif opcao == 'l':
            linhas ()
            print('Obrigado pela sua preferência. Ótimo dia!')
            linhas ()
            sleep (1)
            break

        else:
            linhas()
            print('\033[31mOperação inválida, por favor selecione novamente a operação desejada.\033[m')
            sleep (1)

main()