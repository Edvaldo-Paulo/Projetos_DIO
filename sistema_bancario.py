SALDO_INICIAL = 500.00
total_saques = 0
saque1 = 0
saque2 = 0
saque3 = 0
valor_deposito = 0

while True:

    menu = input("""
####Selecionar Operação####
    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [q] - Sair
###########################

""").strip()
    
    if menu.lower() == 'd':
        valor_deposito = input('Insira um valor para depositar: ')

        try: 
            valor_deposito = float(valor_deposito)
            
            if valor_deposito > 0:
                print('Valor depositado com sucesso!')
            else: 
                print('Você não pode depositar valor negativo')
        except ValueError:
            print('Isto não é um número. Tente novamente!')
    elif menu.lower() == 's':
        cont_saques = 0
        stop_structures = False
        while cont_saques <= 3:
            while stop_structures == False:

                cont_saques += 1

                valor_saque = input('Insira o valor que deseja sacar: ')

                try: 
                
                    valor_saque = float(valor_saque)

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

    elif menu.lower() == 'q':
        break
    else:
        print('Não reconheço esta opção. Tente novamente!') 