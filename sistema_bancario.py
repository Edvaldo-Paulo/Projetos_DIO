from colorama import Fore, init

init()

def menu():
    tam = '_' * 36
    print(Fore.BLUE +   tam)
    print(Fore.BLUE + '|                                    |')
    print(Fore.BLUE + '|================Menu================|')
    print(Fore.BLUE + f'|{tam}|')
    print(Fore.BLUE + '|                                    |')
    print(Fore.BLUE + '|1 - Cadastrar Usuário               |')
    print(Fore.BLUE + '|2 - Cadastrar conta                 |')
    print(Fore.BLUE + '|3 - Listar contas                   |')
    print(Fore.BLUE + '|4 - Depósitar                       |')
    print(Fore.BLUE + '|5 - Sacar                           |')
    print(Fore.BLUE + '|6 - Extornar Valor                  |')
    print(Fore.BLUE + '|0 - Sair                            |')      
    print(Fore.BLUE + f'|{tam}|')
    escolha = input(Fore.BLUE + 'Escolha uma opção: ' + Fore.RESET)
    return escolha


def novo_usuario(usuarios):
    usuario = {}
    cpf = input('Informe seu cpf (apenas números): ')

    try:
        cpf = int(cpf)

        if usuario_existe(usuarios, cpf): #Verifica se o usuário já existe
            print(Fore.RED + 'CPF já cadastrado!' + Fore.RESET)
        else: #Caso o usuário não exista, cadastra-o
            nome = input('Informe seu nome: ')
            data_nascimento = input('Informe a sua data de nascimento (dd/mm/aaaa): ')
            telefone = input('Informe seu telefone: ')
            endereco = input('Informe seu endereço (logradouro - bairro - cidade/sigla do estado): ')
            usuario['cpf'] = cpf
            usuario['nome'] = nome
            usuario['data de nascimento'] = data_nascimento
            usuario['telefone'] = telefone
            usuario['endereco'] = endereco
            usuarios.append(usuario)
            print(Fore.GREEN + 'Usuário cadastrado com sucesso' + Fore.RESET)
    except ValueError: 
        print(Fore.YELLOW + 'Insira números inteiros para o cpf' + Fore.RESET)
    return usuarios

def usuario_existe(usuarios, cpf):
    """Verifica se um usuário já existe com base no CPF."""
    return any(usuario['cpf'] == cpf for usuario in usuarios)

numero = 0  # Mova esta linha para fora da função

def nova_conta(contas,usuarios):
    global numero  # Adicione numero à lista de variáveis globais
    conta = {}
    AGENCIA = '0001'
    num_conta = []
    

    cpf = input('Informe seu cpf: ')

    try: 
        cpf = int(cpf)
        if usuario_existe(usuarios, cpf):
            numero += 1
            num_conta.append(numero)
            conta['AGENCIA'] = AGENCIA
            conta['Nº da conta'] = num_conta
            conta['usuario'] = usuarios
            contas.append(conta)
            print(Fore.GREEN + 'Conta criada com sucesso' + Fore.RESET)
        else:
            print(Fore.RED + 'Usuário não encontrado' + Fore.RESET)
    except ValueError:
        print(Fore.YELLOW + 'Insira números inteiros para o cpf' + Fore.RESET)
    return contas

def listar_contas(contas):
    for conta in contas:
        print (f'Agencia: {conta['AGENCIA']}')
        for num_conta in conta['Nº da conta']:
            print(f'C/C: {num_conta}')
        for usuario in conta['usuario']:
            print(f'Titular: {usuario['nome']}')
        print('-' * 35)
    return contas

def depositar(saldo, extrato, valor, /):
    try:
        valor = float(valor)
    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f'{Fore.GREEN} Depósito realizado com sucesso!{Fore.RESET}')
        else:
            print(f'{Fore.RED} Insira um valor maior que zero!{Fore.RESET}')
    except ValueError:
        print(f'{Fore.YELLOW} Insira um valor numérico!{Fore.RESET}')
    
    return saldo, extrato

<<<<<<< HEAD
def sacar(*, saldo, valor, extrato, numero_saques, limite, limite_saques):
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print(f'{Fore.RED} Saldo insuficiente!{Fore.RESET}')
        elif excedeu_limite:
            print(f'{Fore.RED} O valor do saque excede o limite!{Fore.RESET}')
        elif excedeu_saques:
            print(f'{Fore.RED} Limite de saques excedido!{Fore.RESET}')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t R${valor:.2f} \n"
            numero_saques += 1       
            print(f'{Fore.GREEN} Saque realizado com sucesso!{Fore.RESET}')
        else:
            print(f'{Fore.YELLOW} Insira um valor numérico!{Fore.RESET}')
    
        return saldo, extrato
=======
                    if valor_saque <= 500.00:
                        print('Saque realizado com sucesso!')
                        total_saques += + valor_saque

                    
                        if cont_saques == 1:
                            saque1 = valor_saque
                    
                        if cont_saques == 2:
                            saque2 = valor_saque
                        if cont_saques == 3:
                            saque3 = valor_saque
                    else:
                        print('Você não pode sacar um valor maior que R$500,00!')
                        
                except ValueError:
                    print('Isto não é um número. Tente novamente!')
                
                print('Você deseja Continuar?')
                decisao = input('Digite 1 para sim ou 2 para não: ')

                if decisao == '2':
                    stop_structures = True
                                
            if stop_structures:
                break

    elif menu.lower() == 'e':
        saldo_atual = (SALDO_INICIAL + valor_deposito) - total_saques
        
        print(f"""
        #####Cliente####
            
        Nome: André Vieira
                    
        #####Atividades da Conta#####
        Depósito: R${valor_deposito}
            
        Saques: 
        01 - R${saque1}
        02 - R${saque2}
        03 - R${saque3}
            
        #####Situação da conta#####
            
        Saldo atual: R${saldo_atual}
        """)
>>>>>>> ef47bbbf102a586b82ebec119af531f75ee39a18

def extornar_conta(saldo, /, *, extrato):
    print(f'{Fore.LIGHTGREEN_EX}==========>>>Extrato<<<==========')
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'\nSaldo: R${saldo:.2f}{Fore.RESET}')

def main():
    limite = 500
    LIMITE_SAQUES = 3
    numero_saques = 0
    usuarios = []
    contas = []
    saldo = 0
    extrato = ""

    while True:
        opcao = (menu())

        if opcao == '1':
            novo_usuario(usuarios)
        elif opcao == '2':
            nova_conta(contas, usuarios)
        elif opcao == '3':
            listar_contas(contas)
        elif opcao == '4':
            valor = input('Insira o valor que deseja depositar: ')
            saldo, extrato = depositar(saldo, extrato, valor)
        elif opcao == '5':
            valor = float(input('Insira o valor que deseja sacar: '))
        
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == '6':
            extornar_conta(saldo, extrato=extrato)
        elif opcao == '0':
            break
        else:
            print(Fore.YELLOW + 'Opção inválida!' + Fore.RESET)

main()