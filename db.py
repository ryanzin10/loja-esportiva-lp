import os

category = {
    '1': {'name': 'Chuteira', 'sub': {'1': {'tipo': 'Campo'}, '2': {'tipo': 'Society'}, '3': {'tipo': 'Futsal'}}},
    '2': {'name': 'Luva', 'sub': {'1': {'tipo': 'Flat'}, '2': {'tipo': 'Rollfinger'}}},
    '3': {'name': 'Meia', 'sub': {'1': {'tipo': 'Cano alto'}, '2': {'tipo': 'Cano baixo'}}}
}


#Limpar terminal
def limpaTerminal():
    os.system('cls' if os.name == 'nt' else clear)


def cadastrarProduto():
    produto = {
        "Código de barras": "",
        "Nome": "",
        "Descrição": "",
        "Preço": 0.0,
        "Data de validade": ""
    }

    while True:
        limpaTerminal()
        
        for x in produto:
            produto[x] = input(x + ': ')

            with open("dbprodutos.txt", "r", encoding="utf8") as dbp:
                for y in dbp:
                    if produto["Código de barras"] == y.strip():
                        print('Esse produto já foi cadastrado!')
                        break
            dbp.close()

            if contador == 0:
                with open("dbprodutos.txt", "a", encoding="utf8") as dbp:
                    dbp.write(str(produto[x]) + '\n')

        novoProduto = input('Cadastrar novo produto (s/n)? ').lower()
        if novoProduto == 'n':
            break