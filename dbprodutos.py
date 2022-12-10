import os, time

produto = {
        "Código de barras": "",
        "Nome": "",
        "Descrição": "",
        "Preço": 0.0,
        "Quantidade em estoque": 0
    }

#Quantidade de produtos
qtd_prod = len(produto)

#SESSÃO DE PRODUTOS

#Limpar terminal
def limpaTerminal():
    os.system('cls' if os.name == 'nt' else clear)

#Cadastro de produto
def cadastrarProduto():
    while True:
        limpaTerminal()

        #Adicionando valores aos atributos de produto
        for x in produto:
            produto[x] = input(x + ': ')
            with open("dbprodutos.txt", "a", encoding="utf8") as dbp:
                dbp.write(str(produto[x]) + '\n')
            dbp.close()
        
        novoProduto = input('Cadastrar novo produto (s/n)? ').lower()
        if novoProduto == 'n':
            break

#Alteração de produto
def alterarProduto():
    while True:
        limpaTerminal()

        chave = input("Digite o código de barras: ")

        with open('dbprodutos.txt', 'r', encoding="utf8") as dbp:
            produtos = dbp.readlines()
        dbp.close()
         
        for x in range(len(produtos)):
            if produtos[x] == chave + '\n' and (x+qtd_prod)%qtd_prod == 0:
                campo = input("[1] Nome\n[2] Descrição\n[3] Preço\n[4] Quantidade em estoque\n[0] Voltar\n\nQual campo deseja alterar: ")
                novo = input("\nDigite o novo valor: ")

                with open('dbprodutos.txt', 'w', encoding="utf8") as dbp:
                    def escrever():
                        for y in produtos:
                            dbp.write(y)
                        dbp.close()
                    
                    if campo == '1':
                        produtos[x+1] = novo + '\n'
                        print("\nNome alterado!\n")
                        escrever()
                        break

                    elif campo == '2':
                        produtos[x+2] = novo + '\n'
                        print("\nDescrição alterada!\n")
                        escrever()
                        break

                    elif campo == '3':
                        produtos[x+3] = novo + '\n'
                        print("\nPreço alterado!\n")
                        escrever()
                        break
                    
                    elif campo == '4':
                        produtos[x+4] = novo + '\n'
                        print("\nEstoque alterado!\n")
                        escrever()
                        break

                    else:
                        print("\nCampo inválido, digite novamente!\n")
                        continue

            elif x == len(produtos) - 1:
                    print("\nEsse produto não está cadastrado no banco de dados!\n")
                    time.sleep(3)
                    continue
            
        novaAlt = input('ALterar novo produto (s/n)? ').lower()
        if novaAlt == 'n': 
            break                    

#Consulta de produto
def consultarProduto():
    while True:
        limpaTerminal()
        #Chave primária do produto, no caso o Código de barras
        chave = input("Digite o código de barras: ") 
        #Abrindo o arquivo em modo leitura
        with open('dbprodutos.txt', 'r', encoding='utf8') as dbp:
            #Colocando dados do .txt em uma lista
            produtos = dbp.readlines() 
            #Percorrendo lista
            for x in range(len(produtos)):
                #Encontrando código de barras digitado pelo usuário
                
                if produtos[x] == chave + '\n' and (x+qtd_prod)%qtd_prod == 0:
                    print(f"\nNome: {produtos[x+1]}Descrição: {produtos[x+2]}Preço: {produtos[x+3]}Quantidade em estoque: {produtos[x+4]}Código de barras: {produtos[x]}")
                    
                    break
                #Caso o código digitado não exista no banco
                elif x == len(produtos) - 1:
                    print("\nEsse produto não está cadastrado no banco de dados!\n")
                    
            
            novoProduto = input('Consultar novo produto (s/n)? ').lower()
            if novoProduto == 'n': 
                break
        dbp.close()

#Exclusão de produto
def excluirProduto():
    while True:
        limpaTerminal()

        chave = input("Digite o código de barras: ")

        with open('dbprodutos.txt', 'r', encoding="utf8") as dbp:
            produtos = dbp.readlines()
        dbp.close()
         
        for x in range(len(produtos)):
            if produtos[x] == chave + '\n' and (x+qtd_prod)%qtd_prod == 0:
                excluir = input(f"\nDeseja excluir o/a {produtos[x+1].split()} (s/n)? ").lower()
                if excluir == 's':
                    with open('dbprodutos.txt', 'w', encoding="utf8") as dbp:
                        del(produtos[x:x+5])
                        print("\nProduto excluído!\n")
                        for y in produtos:
                            dbp.write(y)
                        break
                dbp.close()
                break

            elif x == len(produtos) - 1:
                    print("\nEsse produto não está cadastrado no banco de dados!\n")
                    time.sleep(3)
                    continue

        novaAlt = input('Excluir outro produto (s/n)? ').lower()
        if novaAlt == 'n': 
            break


#SESSÃO DE VENDAS
carrinho = []
def addCarrinho():
    while True:
        limpaTerminal()

        chave = input("Digite o código de barras: ")
        unidades = int(input("Quantas unidades: "))

        with open('dbprodutos.txt', 'r', encoding="utf8") as dbp:
            produtos = dbp.readlines()
        dbp.close()

        for x in range(len(produtos)):
            if produtos[x] == chave + '\n' and (x+qtd_prod)%qtd_prod == 0:
                add = input(f"Deseja adicionar {produtos[x+1]} ao carrinho (s/n)?").lower()
                if add == 's':
                    for x in range(unidades):
                        for y in range(len(produto)):
                            carrinho.append(produtos[x+y])
                    



def verCarrinho():
    limpaTerminal()

    print("Produtos no carrinho:\n\n")

    for x in range(len(carrinho)):
        if x > 0 and x%len(produto)!=0:
            print(carrinho[x])

#def comprar()