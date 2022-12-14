import os

produto = {
        "Código de barras": "",
        "Nome": "",
        "Descrição": "",
        "Preço": 0.0,
        "Quantidade em estoque": 0
    }

#Quantidade de atributos
qtd_prod = len(produto)


#Limpar terminal
def limpaTerminal():
    os.system('cls' if os.name == 'nt' else clear)


#SESSÃO DE PRODUTOS

#Cadastro de produto
def cadastrarProduto():
    while True:
        limpaTerminal()

        #Adicionando valores aos atributos de produto percorrendo dicionário
        for x in produto:
            produto[x] = input(x + ': ')
            #Passando informações do arquivo para uma lista
            with open("dbprodutos.txt", "r", encoding="utf8") as dbp:
                produtos = dbp.readlines()
            dbp.close()

            #Se o produto já estiver no banco...
            if x == "Código de barras" and produto[x] + "\n" in produtos:
                print("\nO Banco de Dados já possui esse produto!\n")
                break

            #Senão, adicione o novo produto ao banco
            else:
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

        #identificador do produto
        chave = input("Digite o código de barras: ")

        #Passando informações do arquivo para uma lista
        with open('dbprodutos.txt', 'r', encoding="utf8") as dbp:
            produtos = dbp.readlines()
        dbp.close()

        #for para percorrer a lista de produtos de 5 em 5, assim pega só códigos de barra
        for x in range(0, len(produtos), qtd_prod):
            if produtos[x] == chave + '\n':
                campo = input("[1] Nome\n[2] Descrição\n[3] Preço\n[4] Quantidade em estoque\n[0] Voltar\n\nQual campo deseja alterar: ")
                novo = input("\nDigite o novo valor: ")

                #Escrever no arquivo...
                with open('dbprodutos.txt', 'w', encoding="utf8") as dbp:
                    def escrever():
                        for y in produtos:
                            dbp.write(y)
                        dbp.close()

                    while True:
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
                            print("\nCampo inválido!\n")
                            escrever()
                            break
            
            #Se o produto não existir no banco...
            elif x == 0 and chave + "\n" not in produtos:
                    print("\nEsse produto não está cadastrado no banco de dados!\n")
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
        #Colocando dados do .txt em uma lista
        with open('dbprodutos.txt', 'r', encoding='utf8') as dbp:
            produtos = dbp.readlines() 

            #Percorrendo lista
            for x in range(0, len(produtos), qtd_prod):

                #Encontrando código de barras digitado pelo usuário
                if produtos[x] == chave + '\n':
                    print(f"\nNome: {produtos[x+1]}Descrição: {produtos[x+2]}Preço: {produtos[x+3]}Quantidade em estoque: {produtos[x+4]}Código de barras: {produtos[x]}")
                    break

                #Caso o código digitado não exista no banco
                elif x == 0 and chave + "\n" not in produtos:
                    print("\nEsse produto não está cadastrado no banco de dados!\n")
                    
            
            novoProduto = input('Consultar novo produto (s/n)? ').lower()
            if novoProduto == 'n': 
                break
        dbp.close()

#Exclusão de produto
def excluirProduto():
    while True:
        limpaTerminal()

        #Pedindo identificador do produto
        chave = input("Digite o código de barras: ")

        #Lista de produtos
        with open('dbprodutos.txt', 'r', encoding="utf8") as dbp:
            produtos = dbp.readlines()
        dbp.close()
         
        #for para percorrer a lista de produtos de 5 em 5, assim pega só códigos de barra
        for x in range(0, len(produtos), qtd_prod):
            #Se o código de barras for igual ao digitado...
            if produtos[x] == chave + '\n':

                #Confirmando a exclusão
                excluir = input(f"\nDeseja excluir o/a {' '.join(produtos[x+1].split())} (s/n)? ").lower()
                if excluir == 's':

                    #Escrevendo lista sem o arquivo apagado no arquivo
                    with open('dbprodutos.txt', 'w', encoding="utf8") as dbp:
                        del(produtos[x:x+5])
                        print("\nProduto excluído!\n")
                        for y in produtos:
                            dbp.write(y)
                        break
                
                dbp.close()
                break
            
            #Se o produto não estiver no bd
            else:
                if x == 0 and chave + "\n" not in produtos:
                    print("\nEsse produto não está cadastrado no banco de dados!\n")

        novaAlt = input('\nExcluir outro produto (s/n)? ').lower()
        if novaAlt == 'n': 
            break


#SESSÃO DE VENDAS
carrinho = []

#Preço dos produtos no carrinho
def verPreco():
    preco = 0
    for x in range(3, len(carrinho), qtd_prod):
        preco = preco + (float(carrinho[x]))
    print(f"\nPreço: R${preco:.2f}")

#Adicionando produtos no carrinho
def addCarrinho():

    while True:
        limpaTerminal()

        #Lista de produtos
        with open('dbprodutos.txt', 'r', encoding="utf8") as dbp:
            produtos = dbp.readlines()
        dbp.close()

        #Pedindo chave e quantidade daquele produto
        chave = input("Digite o código de barras: ")
        unidades = int(input("Quantas unidades: "))

        #for para percorrer a lista de produtos de 5 em 5, assim pega só códigos de barra
        for x in range(0, len(produtos), qtd_prod):

            #Se o código de barras for igual ao digitado...
            if produtos[x] == chave + '\n':

                #Adicionar ao carrinho o produto
                for z in range(unidades):
                    for y in range(len(produto)):
                        carrinho.append(produtos[x+y])
            
            else:
                if x == 0 and chave + "\n" not in produtos:
                    print("\nEsse produto não está cadastrado no banco de dados!")
                    break

        #Mostrando nomes que contém no carrinho atualizado
        for x in range(1, len(carrinho), qtd_prod):
            print("\n", " ".join(carrinho[x].split()))
        verPreco()

        novo = input('\nAdicionar outro produto (s/n)? ').lower()
        if novo == 'n': 
            break

def verCarrinho():
    while True:
        limpaTerminal()

        print("Produtos no carrinho:\n\n")

        #Mostrando nomes dos produtos no carrinho
        for x in range(1, len(carrinho), qtd_prod):
            print(" ".join(carrinho[x].split()))

        verPreco()

        voltar = input('\nVolte pressionando enter: ').lower()
        if voltar == '': 
            break
    

def vender():
    while True:
        limpaTerminal()

        #Lista de produtos
        with open('dbprodutos.txt', 'r', encoding="utf8") as dbp:
            produtos = dbp.readlines()
        dbp.close()

        #Mostrando carrinho e preço final
        for x in range(1, len(carrinho), 5):
            print("\n"," ".join(carrinho[x].split()), end="")
        verPreco()

        #Confirmação de venda
        finalizar = input("\nFinalizar venda (s/n)? ")
        if finalizar == 's':
    
            #identificando produtos pelo código de barras
            for x in range(0, len(carrinho), qtd_prod):

                #quantidade de produtos a serem vendidos e atualização de estoque
                qtd = carrinho.count(carrinho[x])
                estoque = int(carrinho[x+4]) - qtd
                carrinho[x+4] = str(estoque) + "\n"

                #Atualizando valor do estoque na lista geral de produtos
                with open("dbprodutos.txt", "w", encoding="utf8") as dbp:
                    for y in range(0, len(produtos), qtd_prod):
                        if carrinho[x] == produtos[y]:
                            for z in range(qtd_prod):
                                produtos[y+z] = carrinho[x+z]

                    #Escrevendo produtos no arquivo
                    for i in produtos:
                        dbp.write(i)
                dbp.close()
            
            print(f"\nCompra finalizada!\n")
            carrinho.clear()
            voltar = input('Volte pressionando enter: ').lower()
            if voltar == '': 
                break
        else:
            break    