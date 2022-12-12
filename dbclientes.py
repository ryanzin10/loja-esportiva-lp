import dbprodutos, time

cliente = {
        "CPF": "",
        "Nome": "",
        "Data de nascimento": "",
        "Telefone": "",
        "Email": "",
        }

qtd_cli = len(cliente)

def cadastrarCliente():
    while True:
        dbprodutos.limpaTerminal()

        #Adicionando valores aos atributos de produto
        y = 0
        for x in cliente:
            cliente[x] = input(x + ': ')

            with open("dbprodutos.txt", "r", encoding="utf8") as dbp:
                clientes = dbp.readlines()
            dbp.close()

            if y==0 and cliente[x] in clientes:
                print("\nO Banco de Dados já possui esse cliente!\n")

            else:
                with open("dbclientes.txt", "a", encoding="utf8") as dbp:
                    dbp.write(str(cliente[x]) + '\n')
                dbp.close()
            y = y+1

        novoCliente = input('Cadastrar novo cliente (s/n)? ').lower()
        if novoCliente == 'n':
            break

    #Alteração de produto
def alterarCliente():
    while True:
        dbprodutos.limpaTerminal()

        chave = input("Digite o código de barras: ")

        with open('dbclientes.txt', 'r', encoding="utf8") as dbp:
            clientes = dbp.readlines()
        dbp.close()
         
        for x in range(0, len(clientes), 5):
            if clientes[x] == chave + '\n':
                campo = input("[1] CPF\n[2] Nome\n[3] Data de nascimento\n[4] Telefone\n[5] Email\n[0] Voltar\n\nQual campo deseja alterar: ")
                novo = input("\nDigite o novo valor: ")

                with open('dbclientes.txt', 'w', encoding="utf8") as dbp:
                    def escrever():
                        for y in clientes:
                            dbp.write(y)
                        dbp.close()

                    while True:
                        if campo == '1':
                            clientes[x] = novo + '\n'
                            print("\nCPF alterado!\n")
                            escrever()
                            break

                        if campo == '2':
                            clientes[x+1] = novo + '\n'
                            print("\nNome alterado!\n")
                            escrever()
                            break

                        elif campo == '3':
                            clientes[x+2] = novo + '\n'
                            print("\nData de nascimento alterada!\n")
                            escrever()
                            break

                        elif campo == '4':
                            clientes[x+3] = novo + '\n'
                            print("\nTelefone alterado!\n")
                            escrever()
                            break
                        
                        elif campo == '5':
                            clientes[x+4] = novo + '\n'
                            print("\nEmail alterado!\n")
                            escrever()
                            break

                        else:
                            print("\nCampo inválido!\n")
                            escrever()
                            break

            elif x == len(clientes) - 1 and clientes[x] != chave + '\n':
                    print("\nEsse produto não está cadastrado no banco de dados!\n")
                    time.sleep(3)
                    continue
            
        novaAlt = input('ALterar novo produto (s/n)? ').lower()
        if novaAlt == 'n': 
            break                    
