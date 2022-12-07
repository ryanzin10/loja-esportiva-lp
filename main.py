import dbprodutos, dbclientes, time

while True:
    dbprodutos.limpaTerminal()
    #Menu
    options = input('=======================\n[1] Venda\n[2] Produto\n[3] Cliente\n[0] Sair\n=======================\nOpção desejada: ')

    #Venda
    if options == '1':
        while True:
            
            optionVenda = input('\n=======================\n[1] Adicionar produto ao carrinho\n[2] Verificar carrinho\n[3] Concluir venda\n[0] Voltar\n=======================\nOpção desejada: ')
            #Adicionar produto ao carrinho
            if optionVenda == '1':
                addCarrinho = input('\nDigite o código de barras: ')
            
            #Verificar carrinho
            elif optionVenda == '2':
                print()
            
            #Concluir venda
            #elif optionVenda == '3':

            #Voltar
            elif optionVenda == '0':
                break
            else:
                print('Opção inválida!')

    #Produto
    elif options == '2':
        while True:
            dbprodutos.limpaTerminal()

            optionProduto = input('\n=======================\n[1] Consultar produto\n[2] Cadastrar produto\n[3] Alterar produto\n[4] Excluir produto\n[0] Voltar\n=======================\nOpção desejada: ')
            
            #Consultar produto
            if optionProduto == '1':
                dbprodutos.consultarProduto()
            
            #Cadastrar produto
            elif optionProduto == '2':
                dbprodutos.cadastrarProduto()

            #Alterar produto
            elif optionProduto == '3':
                dbprodutos.alterarProduto()
            
            #Excluir produto
            elif optionProduto == '4':
                dbprodutos.excluirProduto()

            #Voltar
            elif optionProduto == '0':
                break
            else:
                print('Opção inválida!')
                time.sleep(3)
    
    #CLiente
    elif options == '3':
        while True:
            optionCliente = input('\n=======================\n[1] Consultar cliente\n[2] Cadastrar cliente\n[3] Excluir cliente\n[0] Voltar\n=======================\nOpção desejada: ')

            if optionCliente == '2':
                dbclientes.cadastrarCliente()

    #Sair
    elif options == '0':
        print('\nSaindo...')
        time.sleep(3)
        dbprodutos.limpaTerminal()
        break

    else:
        print('\nDigite uma alternativa válida!')
        time.sleep(3)
                
