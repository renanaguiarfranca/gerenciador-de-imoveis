from main import *
def telaInicio():
    print(header)
    comandoInicio = str(input("Digite o comando\n|0|🔐 LOGIN\n|1|📃 CADASTRAR CLIENTE\n"))
    if(comandoInicio == str(0)):
        # login()
        autenticarLogin()
    elif(comandoInicio == str(1)):
        cadastro()
    else:
        telaInicio()

def validar_telefone(telefone):
    telefone = telefone.strip() 
    return telefone.isdigit() and len(telefone) in [10, 11]
    if validar_telefone(telefone):
       print('Telefone válido!')
    else:
       print('Telefone inválido! Digite apenas números, com 10 ou 11 dígitos.')

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False
    return True
    if validar_cpf(cpf):
     print("CPF válido!")
    else:
     print("CPF inválido! Tente novamente.")
def cadastro():
    print("|TELA CADASTRO|\n")
    nome = str(input('Digite seu nome::\n'))
    email = str(input('Coloque seu email:\n'))
    telefone = int(input('Coloque seu telefone (apenas números):\n'))
    senha2 = str(input('Crie sua senha:\n'))
    cpf2 = int(input('Digite seu CPF:\n'))
    main()
