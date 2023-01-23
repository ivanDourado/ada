from time import sleep # importa a biblioteca time para aplicar o método sleep() que proporciona um delay desejado

colaboradores = list() # # cria-se o lista colaboradores
funcionario = dict() # cria-se o dicionário funcionario
id = 7401 # inicializa variavél Id, para ocorrer seu incremento na linha l.86
def cadastrar_funcionario(id): # cria-se função com parâmetro id
    print(f""" {'**'*30}
    {'--'*15} Menu Cadastrar Funcionário  {'--'*15}  
     """) # printa menu
    funcionario['status']=1
    funcionario["código"] = id # No dicionário funcionário, criar-se-á uma chave 'código' que receberá o valor id (paramero da função)
    funcionario["nome"] = str(input('Por favor entre com o Nome: ')) # No dicionário funcionário, criar-se-á uma chave 'nome' que receberá o valor string inserido pelo usuário
    funcionario["telefone"] = str(input('Por favor entre com o Telefone: ')) # No dicionário funcionário, criar-se-á uma chave 'Telefone' que receberá o valor string inserido pelo usuário
    funcionario["endereco"] = str(input('Por favor entre com o endereço: ')) # No dicionário funcionário, criar-se-á uma chave 'endereco' que receberá o valor string inserido pelo usuário
    funcionario["setor"] = str(input('Por favor entre com o setor [A-Z]: ')).upper().strip()[0] # No dicionário funcionário, criar-se-á uma chave 'setor' que receberá o valor string inserido pelo usuário
    funcionario["salario"] = float(input('Por favor entre com o salário: ')) # No dicionário funcionário, criar-se-á uma chave 'a' que receberá o valor float inserido pelo usuário
    colaboradores.append(funcionario.copy()) # na lista colaboradores, ao seu final de comprimento, receberá como último ítem uma cópia do dicionário funcionário
    print('**'*30)
    nome = funcionario["nome"]
    print(f'\nFuncionário {nome} cadastrado(a) com sucesso!')



def consultar_funcionarios(): # cria-se função
    opcao = '' # inicializa variavél opcao de modo a iniciar o laço while
    while opcao != 4: # enquanto a opcao for distinta de 4 
        print(f""" {'**'*30}
        {'--'*15} Menu Consultar Funcionário {'--'*15}
        Escolha a opção desejada:
        1) Consultar Todos os Funcionários
        2) Consultar Funcionário por Id
        3) Consultar Funcionário(s) por Setor
        4) Retornar  
        """) # printa menu
        opcao = int(input('>>>> ')) # solicita o dado ao usuário
        
        if opcao == 1: # se opcao = 1
            for funcionario in colaboradores: #para cada funcionario (dict) em colaboradores(list)
                for key, value in funcionario.items(): # para cada chave e valor em funcionário
                    if funcionario["status"] == 1:
                        if key != "status":
                            print(f'{key} : {value}.') # imprime  chave e valor
                            sleep(.4)
                print('-'*10)
        if opcao == 2: # se opcao = 2
            busca = int(input('Digite o ID do Funcionário: (999 para parar) ')) # burcar ID
            print('--'*15)
            if busca == 999: # se valor = 999 , interrompe
                break
            for funcionario in colaboradores: #para cada funcionario (dict) em colaboradores(list)
                for k,v in funcionario.items(): # para cada chave e valor em funcionário
                    if busca == funcionario["código"]: # se busca for igual ao valor da chave 'código'
                        print(f'{k} : {v}') # imprime  chave e valor
                print() # pula linha
        if opcao == 3: # se opcao = 3
            busca = str(input('Digite o setor dos Funcionários [A-Z]: (999 para parar) ')).upper().strip()[0] # burcar setor
            print('--'*15) # imprime divisoria 
            if busca == '999': # se valor = 999 , interrompe
                break
            for funcionario in colaboradores: #para cada funcionario (dict) em colaboradores(list)
                for k,v in funcionario.items(): # para cada chave e valor em funcionário
                    if busca == funcionario["setor"]: # se busca for igual ao valor da chave 'setor'
                        print(f'{k} : {v}')  # imprime  chave e valor
                print() # pula linha
        if opcao == 4: # se opcao = 4
            break # interrompe
          

def remover_funcionario():  # cria-se função
     print(f""" {'**'*30}
    {'--'*15} Menu Remover Funcionário  {'--'*15}  
     """)# printa menu
     remove = int(input('Digite o código/ID do funcionário a ser removido: ')) # solicita o dado ao usuário[id]
     for funcionario in colaboradores: #para cada funcionario (dict) em colaboradores(list)
        for k,v in funcionario.items(): # para cada chave e valor em funcionário
            if k == "código" and remove == v: # se a chave = código e valor = remove
                funcionario["status"] = 0 # Altera-se o status do 'funcionario' (dict) da lista colaboradores para zero, afim de ocultá-lo

def atualizar_funcionario(): # cria-se função 
    print(f""" {'**'*30}
    {'--'*15} Menu atualizar Funcionário  {'--'*15}  
     """)# printa menu
    atualiza = int(input('Digite o código/ID do funcionário a ser atualizado: ')) # solicita o dado ao usuário[id]
    for funcionario in colaboradores: #para cada funcionario (dict) em colaboradores(list)
        for k,v in funcionario.items(): # para cada chave e valor em funcionário
            if k == "código" and atualiza == v: # se a chave = código e valor = atualiza
                opcao = '' # inicializa variavél opcao de modo a iniciar o laço while
                while opcao != 6: # enquanto a opcao for distinta de 6 
                    print(f""" {'**'*30}
                    {'--'*15} Qual informação deseja alterar? {'--'*15}
                    Escolha a opção desejada:
                    1) Alterar Nome
                    2) Alterar Telefone
                    3) Alterar Endereço
                    4) Alterar Setor
                    5) Alterar Salário
                    6) Retornar  
                    """) # printa menu atualiza
                    opcao = input('>>>> ') # solicita o dado ao usuário
                    if opcao not in ['1','2','3','4','5','6']:
                        continue
                    if opcao == '1': # se opcao = 1                    
                        for key, value in funcionario.items(): # para cada chave e valor em funcionário
                            if key == "nome":
                                novo_nome = input('Insira novo nome: ')
                                if novo_nome == '999':
                                    break
                                value = funcionario["nome"] = novo_nome  
                                print(f'{key} : {value}.') # imprime  chave e valor
                                print('Nome Atualizado com Sucesso! ')
                                sleep(.4)
                        print('-'*10)
                    if opcao == '2': # se opcao = 2
                        telefone = input('Insira o novo telefone: (999 para parar) ') # altera telefone
                        print('--'*15)
                        if telefone == '999': # se valor = 999 , interrompe
                            continue                    
                        for k,v in funcionario.items(): # para cada chave e valor em funcionário
                            if k == "telefone":
                                v = funcionario["telefone"] = telefone
                                print(f'{k} : {v}') # imprime  chave e valor
                                print('Telefone Atualizado com Sucesso! ')
                        print() # pula linha
                    if opcao == '3': # se opcao = 3
                        endereco = str(input('Insira o novo endereço do Funcionário: (999 para parar) ')) # atualizar endereco
                        print('--'*15) # imprime divisoria 
                        if endereco == '999': # se valor = 999 , interrompe
                            break                    
                        for k,v in funcionario.items(): # para cada chave e valor em funcionário
                            if k == "endereco": # se busca for igual ao valor da chave 'setor'
                                v = funcionario["endereco"] = endereco
                                print(f'{k} : {v}')  # imprime  chave e valor
                                print('Endereço Atualizado com Sucesso! ')
                        print() # pula linha
                    if opcao == '4': # se opcao = 4
                        setor = str(input('Insira o novo setor do Funcionário [A-Z]: (999 para parar) ')).upper().strip()[0] # atualizar setor
                        print('--'*15) # imprime divisoria 
                        if setor == '999': # se valor = 999 , interrompe
                            break                    
                        for k,v in funcionario.items(): # para cada chave e valor em funcionário
                            if k == "setor": # se busca for igual ao valor da chave 'setor'
                                v = funcionario["setor"] = setor
                                print(f'{k} : {v}')  # imprime  chave e valor
                                print('Setor Atualizado com Sucesso! ')
                        print() # pula linha
                    if opcao == '5': # se opcao = 5
                        salario = float(input('Insira o novo salario do Funcionário : (aperte enter para parar) ')) # atualizar salario
                        print('--'*15) # imprime divisoria 
                        if salario == '': # se valor = '' , interrompe
                            break                    
                        for k,v in funcionario.items(): # para cada chave e valor em funcionário
                            if k == "salario": # se busca for igual ao valor da chave 'salario'
                                v = funcionario["salario"] = salario
                                print(f'{k} : {v}')  # imprime  chave e valor
                                print('Salário Atualizado com Sucesso! ')
                        print() # pula linha
                    if opcao == '6': # se opcao = 6
                        break # interrompe
               
                

                
   
print(f""" Bem vindo ao controle de funcionários Do time Azul
{'**'*30} """) # boas- vindas ao meu programa
opcao = '' # inicializa opçao
while opcao != 5: # se opcao diferente de 4, faça-se :
    print(f""" {'--'*15} Menu Principal {'--'*15}
        1. Cadastrar Funcionário
        2. Consultar Funcionários(s)
            1) Consultar Todas as Funcionários
            2) Consultar Funcionário por Id
            3) Consultar Funcionário(s) por Setor
            4) Retornar
        3. Atualizar Funcionário
        4. Remover Funcionário
        5. Sair  """)    # printa menu
    opcao = int(input('>>>> ')) # solicita o dado ao usuário do tipo numérico
    if opcao == 1: #se opcao = 1
        cadastrar_funcionario(id) #chama função cadastro com parametro
        #print(f'Funcionário {colaboradores[funcionario["código"]] == id }')
        id +=1 # incremento do ID para cada fncionario novo cadastrado
    if opcao == 2: #se opcao = 2
        consultar_funcionarios() #chama função consulta
    if opcao == 3: # se opcao = 3
        atualizar_funcionario()
    if opcao == 4: #se opcao = 3
        remover_funcionario() #chama função remove
    if opcao == 5: #se opcao = 4
        print('>>> Obrigado! Volte Sempre <<<') # imprime saudaçao de termino da aplicação
        print('**'*30)
        break #Interrompe laço e aplicação   

