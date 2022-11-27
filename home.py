while True:
    options = input('=======================\n1. Venda\n2. Produto\n3. Cliente\n4. Sair\n=======================\nOpção desejada: ')

    #Venda
    if options == '1':
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
            optionProduto = input('\n=======================\n1. Consultar produto\n2. Cadastrar produto\n3. Excluir produto\n4. Voltar\n=======================\nOpção desejada: ')
            
            if optionProduto == '1':
                print()
            
            elif optionProduto == '2':
                codigo = input('Digite o código de barras: ')

            elif optionProduto == '3':
                print()    
            
            elif optionProduto == '4':
                break
            else:
                print('Opção inválida!')