from time import sleep # importa a biblioteca time para aplicar o método sleep() que proporciona um delay desejado

colaboradores = [
    {'status':1, 'código':7401,'nome':'Gabriel','telefone':'12345678','endereco':'Rua A','setor':'A','salario':3000},
    {'status':1, 'código':7402,'nome':'Iohana','telefone':'32145678','endereco':'Rua B','setor':'B','salario':3500},
    {'status':1, 'código':7403,'nome':'Fábio','telefone':'43215678','endereco':'Rua C','setor':'C','salario':3300},    
    ] # # cria-se o lista colaboradores
funcionario = dict() # cria-se o dicionário funcionario
id = 7404 # inicializa variavél Id, para ocorrer seu incremento na linha l.86

def cadastrar_funcionario(id): # cria-se função com parâmetro id
    string = 'Menu Cadastrar Funcionário'
    
    print(string.center(80,'-')) # printa menu

    funcionario['status']=1
    funcionario["código"] = id # No dicionário funcionário, criar-se-á uma chave 'código' que receberá o valor id (paramero da função)
    while True:
        funcionario["nome"] = str(input('Por favor entre com o Nome: ')).strip() # No dicionário funcionário, criar-se-á uma chave 'nome' que receberá o valor string inserido pelo usuário
        while funcionario['nome'] == '' or funcionario['nome'] == ' ':
            print('\033[0;31mCampo vazio. Digite seu nome\033[m')
            funcionario["nome"] = str(input('Por favor entre com o Nome: ')).strip()
        if funcionario['nome'] != '':
            break
    while True:
        funcionario["telefone"] = str(input('Por favor entre com o Telefone: ')).strip() # No dicionário funcionário, criar-se-á uma chave 'Telefone' que receberá o valor string inserido pelo usuário
        while not funcionario["telefone"].isnumeric():
            print('\033[0;31mCampo incorreto. Digite seu número com 9 dígitos mais 2 díditos do DDD.\033[m')
            funcionario["telefone"] = str(input('Por favor entre com o Telefone: '))
        if len(funcionario["telefone"]) == 11 and funcionario["telefone"].isnumeric():
            break
        print('\033[0;31mCampo incorreto. Digite seu número com 9 dígitos mais 2 díditos do DDD.\033[m')
    while True:
        funcionario["endereco"] = str(input('Por favor entre com o endereço: ')).strip() # No dicionário funcionário, criar-se-á uma chave 'endereco' que receberá o valor string inserido pelo usuário
        while funcionario["endereco"] == '':
            print('\033[0;31mCampo vazio. Digite seu Endereço válido.\033[m')
            funcionario["endereco"] = str(input('Por favor entre com o endereço: ')).strip()
        if funcionario["endereco"] != '' and funcionario["endereco"] != ' ':
            break 

    while True:
        setor = funcionario["setor"] = str(input('Por favor entre com o setor [A-Z]: ')).upper() # No dicionário funcionário, criar-se-á uma chave 'setor' que receberá o valor string inserido pelo usuário
        
        while  not setor.isalpha() :
            print('\033[0;31mCampo inválido. Digite um setor válido de A-Z.\033[m')
            setor =funcionario["setor"] = str(input('Por favor entre com o setor [A-Z]: ')).upper()
        if setor.upper()[0] != '' and setor.upper().strip()[0].isalpha():
            break    
    
    while True:
        try:
            funcionario["salario"] = float(input('Por favor entre com o salário: ')) # No dicionário funcionário, criar-se-á uma chave 'a' que receberá o valor float inserido pelo usuário
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um valor numérico válido maior que zero.\033[m')
        else:
            if funcionario["salario"]<=0:
                print('\033[0;31mSalário inválido. Insira um salário numérico superior a zero.\033[m')  
            else:
                break
        
    colaboradores.append(funcionario.copy()) # na lista colaboradores, ao seu final de comprimento, receberá como último ítem uma cópia do dicionário funcionário
    print('**'*30)
    nome = funcionario["nome"]
    print(f'\nFuncionário {nome} cadastrado(a) com sucesso!')

cadastrar_funcionario(id)
 
