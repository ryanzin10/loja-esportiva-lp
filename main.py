import db

while True:
    options = input('=======================\n[1] Venda\n[2] Produto\n[3] Cliente\n[4] Sair\n=======================\nOpção desejada: ')

    #Venda
    if options == '1':
        data.limpaTerminal()
        while True:
            optionVenda = input('\n=======================\n1. Adicionar produto ao carrinho\n2. Verificar carrinho\n3. Concluir venda\n4. Voltar\n=======================\nOpção desejada: ')
            
            if optionVenda == '1':
                addCarrinho = input('\nDigite o código de barras: ')
            
            elif optionVenda == '2':
                print()
            
            #elif optionVenda == '3':

            elif optionVenda == '4':
                break
            else:
                print('Opção inválida!')

    #Produto
    elif options == '2':
        while True:
            optionProduto = input('\n=======================\n[1] Consultar produto\n[2] Cadastrar produto\n[3] Excluir produto\n[4] Voltar\n=======================\nOpção desejada: ')
            
            if optionProduto == '1':
                print()
            


            elif optionProduto == '2':
                db.cadastrarProduto()

            elif optionProduto == '3':
                print("")    
            
            elif optionProduto == '4':
                break
            else:
                print('Opção inválida!')

    elif options == '3':
        while True:
            optionCliente = input('\n=======================\n[1] Cadastrar cliente\n[2] Excluir cliente\n[3] Consultar cliente\n[4] Voltar\n=======================\nOpção desejada: ')

            if optionCliente == '1':
                cliente = {
                    "Nome": "",
                    "CPF": "",
                    "Data de nascimento": ""
                }

                for x in cliente:
                    cliente[x] = input(x + ': ')
                
