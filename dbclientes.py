import dbprodutos, time

cliente = {
        "CPF": "",
        "Nome": "",
        "Data de nascimento": "",
        "Telefone": "",
        "Email": "",
        }

#Quantidade de atributos
qtd_cli = len(cliente)


#Consulta de Cliente
def consultarCliente():
    while True:
        dbprodutos.limpaTerminal()
        
        #
        chave = input("Digite o CPF: ") 

        #Abrindo o arquivo em modo leitura
        with open('dbclientes.txt', 'r', encoding='utf8') as dbp:
            clientes = dbp.readlines() 
            for x in range(0, len(clientes), qtd_cli):
                if clientes[x] == chave + '\n':
                    print(f"\nCPF: {clientes[x]}Nome: {clientes[x+1]}Data de nascimento: {clientes[x+2]}Telefone: {clientes[x+3]}Email: {clientes[x+4]}")
                    break

                #Caso o CPF digitado não exista no banco
                elif x == len(clientes) - 1:
                    print("\nEsse Cliente não está cadastrado no banco de dados!\n")
                    
            
            novoCliente = input('Consultar novo Cliente (s/n)? ').lower()
            if novoCliente == 'n': 
                break
        dbp.close()


def cadastrarCliente():
    while True:
        dbprodutos.limpaTerminal()

        #Adicionando valores aos atributos de Cliente
        for x in cliente:
            #Adicionando valores aos atributos de cliente percorrendo dicionário
            cliente[x] = input(x + ': ')

            #Passando informações do arquivo para uma lista
            with open("dbclientes.txt", "r", encoding="utf8") as dbp:
                clientes = dbp.readlines()
            dbp.close()

            #Se o cliente já estiver no banco...
            if x == "CPF" and cliente[x] + "\n" in clientes:
                print("\nO Banco de Dados já possui esse cliente!\n")

            #Senão, adicione o novo cliente ao banco
            else:
                with open("dbclientes.txt", "a", encoding="utf8") as dbp:
                    dbp.write(str(cliente[x]) + '\n')
                dbp.close()

        novoCliente = input('Cadastrar novo cliente (s/n)? ').lower()
        if novoCliente == 'n':
            break


#Alteração de Cliente
def alterarCliente():
    while True:
        dbprodutos.limpaTerminal()

        #identificador do cliente
        chave = input("Digite o CPF: ")

        #Passando informações do arquivo para uma lista
        with open('dbclientes.txt', 'r', encoding="utf8") as dbp:
            clientes = dbp.readlines()
        dbp.close()
        
        #for para percorrer a lista de clientes de 5 em 5, assim pega só CPF
        for x in range(0, len(clientes), 5):

            #Se o CPF for igual a chave...
            if clientes[x] == chave + '\n':
                campo = input("[1] CPF\n[2] Nome\n[3] Data de nascimento\n[4] Telefone\n[5] Email\n[0] Voltar\n\nQual campo deseja alterar: ")
                novo = input("\nDigite o novo valor: ")

                #Escrever no arquivo...
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

                        elif campo == '2':
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
            
            #Se o cliente não existir no banco...
            elif x == 0 and chave + "\n" not in clientes:
                    print("\nEsse cliente não está cadastrado no banco de dados!\n")
                    time.sleep(3)
                    continue
            
        novaAlt = input('ALterar novo cliente (s/n)? ').lower()
        if novaAlt == 'n': 
            break                    


#Exclusão de cliente
def excluirCliente():
    while True:
        dbprodutos.limpaTerminal()

        #Lista de clientes
        chave = input("Digite o CPF: ")

        #Lista de clientes
        with open('dbclientes.txt', 'r', encoding="utf8") as dbp:
            clientes = dbp.readlines()
        dbp.close()
         
        #for para percorrer a lista de cliente de 5 em 5, assim pega só CPF
        for x in range(0, len(clientes), qtd_cli):

            #Se o CPF for igual ao digitado...
            if clientes[x] == chave + '\n':

                #Confirmando a exclusão
                excluir = input(f"\nDeseja excluir o/a {clientes[x+1]} (s/n)? ").lower()
                if excluir == 's':

                    #Escrevendo lista sem o cliente apagado no arquivo
                    with open('dbclientes.txt', 'w', encoding="utf8") as dbp:
                        del(clientes[x:x+5])
                        print("\nCliente excluído!\n")
                        for y in clientes:
                            dbp.write(y)
                        break
                dbp.close()
                break

            else:
                #Se o cliente não existir no banco...
                if x == 0 and chave + "\n" not in clientes:
                    print("\nEsse Cliente não está cadastrado no banco de dados!\n")
                    time.sleep(3)
                    continue

        novaAlt = input('Excluir outro cliente (s/n)? ').lower()
        if novaAlt == 'n': 
            break