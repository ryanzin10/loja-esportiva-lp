import os
'''
category = {
    '1': {'name': 'Chuteira', 'sub': {'1': {'tipo': 'Campo'}, '2': {'tipo': 'Society'}, '3': {'tipo': 'Futsal'}}},
    '2': {'name': 'Luva', 'sub': {'1': {'tipo': 'Flat'}, '2': {'tipo': 'Rollfinger'}}},
    '3': {'name': 'Meia', 'sub': {'1': {'tipo': 'Cano alto'}, '2': {'tipo': 'Cano baixo'}}}
}
'''
produto = {
        "Código de barras": "",
        "Nome": "",
        "Descrição": "",
        "Preço": 0.0,
        "Quantidade em estoque": 0
    }

#Limpar terminal
def limpaTerminal():
    os.system('cls' if os.name == 'nt' else clear)


def cadastrarProduto():
    while True:
        limpaTerminal()
        
        for x in produto:
            produto[x] = input(x + ': ')
            with open("dbprodutos.txt", "a", encoding="utf8") as dbp:
                dbp.write(str(produto[x]) + '\n')
            dbp.close()

        novoProduto = input('Cadastrar novo produto (s/n)? ').lower()
        if novoProduto == 'n':
            break

def alterarProduto():
    while True:
        limpaTerminal()

        chave = input("Digite o código de barras: ")
        campo = input("Qual campo deseja alterar:\n[1] Nome\n[2] Descrição\n[3] Preço\n[4] Quantidade em estoque\n\n")

        with open('dbprodutos.txt', 'r') as dbp:
            produtos = dbp.readlines()
            for x in range(len(produtos)):
                if produtos[x] == produto + '\n':
                    print(f"\nNome: {produtos[x+1]}Descrição: {produtos[x+2]}Preço: {produtos[x+3]}Quantidade em estoque: {produtos[x+4]}Código de barras: {produtos[x]}")
            
            novoProduto = input('Consultar novo produto (s/n)? ').lower()
            if novoProduto == 'n':
                break
        dbp.close()


def consultarProduto():
    while True:
        limpaTerminal()
        #Chave primária do produto
        chave = input("Digite o código de barras: ") 

        with open('dbprodutos.txt', 'r', encoding='utf8') as dbp:
            #Colocando dados do .txt em uma lista
            produtos = dbp.readlines() 
            #Percorrendo lista
            for x in range(len(produtos)):
                #Encontrando código de barras digitado pelo usuário
                encontrou = False
                if produtos[x] == chave + '\n' and (x+5)%5 == 0:
                    print(f"\nNome: {produtos[x+1]}Descrição: {produtos[x+2]}Preço: {produtos[x+3]}Quantidade em estoque: {produtos[x+4]}Código de barras: {produtos[x]}")
                    encontrou = True
                    break
                #Caso o código digitado não exista no banco
                elif x == len(produtos) - 1 and encontrou == False:
                    print("\nEsse produto não está cadastrado no banco de dados!\n")
                    
            
            novoProduto = input('Consultar novo produto (s/n)? ').lower()
            if novoProduto == 'n': 
                break
        dbp.close()