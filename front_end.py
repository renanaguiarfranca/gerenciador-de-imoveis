from conection import *
from pyfiglet import figlet_format
from front_end import *
import time
from rich.console import Console
from rich.table import Table
header = (figlet_format('ARBINHO', font = "cosmic"))
#=====================================================================================#
#                                📃 Tela de cadastro 📃                              # 
#=====================================================================================#

def telaInicio():
    print("[bold cyan]{}[/bold cyan]".format(header))
    comandoInicio = str(input("Digite o comando\n|0|🔐 LOGIN\n|1|📃 CADASTRAR CLIENTE\n"))
    if(comandoInicio == str(0)):
        # login()
        autenticarLogin()
    elif(comandoInicio == str(1)):
        cadastro()
    else:
        telaInicio()

def cadastro():
    print("===|TELA CADASTRO|===\n")
    nome = str(input('Digite seu nome::\n'))
    email = str(input('Coloque seu email:\n'))
    telefone = int(input('Coloque seu telefone:\n'))
    senha2 = str(input('Crie sua senha:\n'))
    cpf2 = int(input('Digite seu CPF:\n'))
    main()
#======================================================================================#
#                         📦📮 AUTENTICAÇÃO DE LOGIN 📦📮                            #
#======================================================================================#

def autenticarLogin():
    usuario = str(input("Login\n>>>"))
    senha = str(input("Senha\n>>>"))

    if usuario == LOGIN and senha == SENHA:
        main()
    else:
        print("Erro!\nUsuario ou senha incorretos!")
        telaInicio()

#======================================================================================#
#                         📦📮 FUNÇÕES PARA O BANCO DE DADOS 📦📮                    #
#======================================================================================#
#DELETAR IMOVEL DE ACORDO COM O ID💣❌
def removerImovel():
    id_input = input("Digite o ID do imóvel que deseja remover | Para sair digite: S\n>>> ")

    try:
        if id_input.lower() == "s":
            main()
        else:
            id_imovel = int(id_input)  # Tenta converter para inteiro
        
        if type(id_imovel) == int:  # Verifica se realmente é inteiro
            # Remover imovel com o input
            cursor.execute("SELECT * FROM TBL_imovel WHERE id_imovel = %s", (id_imovel,))
            resultados = cursor.fetchone()
            db.commit()
        if resultados == None:
            print('Nenhum Resultado Para ', id_input,'\n')

    except ValueError:  # Se não conseguir converter para int
        print("ERRO!\nDigite apenas números inteiros para o ID.")
        removerImovel()
    
    if resultados:
        print("\nDados do imóvel encontrado:")
        print(f"ID: {resultados[0]}")
        print(f"Endereço: {resultados[1]}")
        print(f"Tipo: {resultados[3]}")
        print(f"Valor: {resultados[4]}")
        confirmacao = input("\nDeseja remover este imóvel? (Sim = S / Não = N): \n")
        if confirmacao.lower() == 's':
                # Remover o imóvel
                cursor.execute("DELETE FROM tbl_imovel WHERE id_imovel = %s", (id_imovel,))
                db.commit()
                print("\nImóvel removido com sucesso!")
                removerImovel()
        else:
            print("Ação cancelada!")
            removerImovel()
    else:
        removerImovel()
    cursor.close()
    db.close

#=================================================================================================#
#                                   ✍ Cadastro de Imoveis 📄                                    #
#=================================================================================================#
def cadastroImovel():
    print('Tela de cadstro, digite os dados abaixo: ✍ 📄\n ')
    descricao = str(input('Digite a Descricão:\n>>> '))
    estado = str(input('Digite o Estado:\n>>> '))
    cidade = str(input('Digite a Cidade:\n>>> '))
    bairro = str(input('Digite o Bairro:\n>>> '))
    rua = str(input('Digite a Rua:\n>>> '))
    numero = str(input('Digite o Numero:\n>>> '))
    cep = str(input('Digite o Cep:\n>>> '))
    diaria = float(input('Digite o Valor da Diaria:\n>>> '))
    comodos = int(input('Digite Quantos comodos:\n>>> '))

    cursor.execute(
        "INSERT INTO TBL_imovel (descricao_imovel,estado_imovel,cidade_imovel,bairro_imovel,rua_imovel,numero_imovel,cep_imovel,diaria_imovel,comodos_imovel) " 
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);",(descricao,estado,cidade,bairro,rua,numero,cep,diaria,comodos))
    cursor.fetchone()
    db.commit()
    cursor.close
    db.close
    print('Dados Salvos! ✅')
    main()

#=================================================================================================#
#                                        🏡 Tela de inicio 🏡                                    # 
#=================================================================================================#
def main():
    print(header)
    print("Bem vindo(a) ao ARBINHO 🏡")
    print("|1| Cadastrar Imovel✍ ✅\n|2| Listar Imoveis📑🔍\n|3| Atualizar Imovel🔧🔄\n|4| Remover Imovel💣❌\n")
    print("|0| CANCELAR❌")
    comando = str(input("Digite o comando:\n"))

    if(comando == str(1)):
        print("Cadastrar Imovel...✍ ✅")
        cadastroImovel()
    elif(comando == str(2)):
        print("Listar Imovéis...📑 🔍")
        listarImoveis()
    elif(comando == str(3)):
        atualizarImovel()
        print("Atualizar Imovel...🔧 🔄")
    elif(comando == str(4)):
        print("Remover Imovel...💣 ❌")
        removerImovel()
    elif(comando == str(0)):
        print("SAINDO...🏃‍♂️ 💨")
        main()
    else:
        print("❗Comando invalido❗")
        telaInicio()
        
#===============================#===========+==+==========#==========================#
#                               |🔧Tela de alterar dados🔄|                         #
#===============================#===========+==+==========#==========================#
def atualizarImovel():
    print('Atualizar Dados🛠\n')
    #Pede o ID do imovel a ser atualizado
    comando = input("Comandos Disponiveis: \n|D| Detalhes\n|S| Sair\nID que deseja alterar🔧\n>>>")
    try:
        if comando.lower() == str("d"):
            print("Indo para Listagem de imoveis🏡...")
            time.sleep(1.2)
            listarImoveis()
        elif comando.lower() == "s":
            print("Saindo...🏃‍♂️💨")
            time.sleep(1.2)
            main()
        else:
            idAtt = int(comando)
            if type(idAtt) == int:
                cursor.execute("SELECT * FROM TBL_imovel WHERE id_imovel = %s", (idAtt,))
                resultados = cursor.fetchone()
                db.commit()
                print("===Você está editando🔧✍===\n|ID:ㅤ{}\n|DESCRIÇÃO:ㅤ{}\n|ESTADO:ㅤ{}\n|CIDADE:ㅤ{}\n|BAIRRO:ㅤ{}\n|RUA:ㅤ{}\n|NUMERO:ㅤ{}\n|CEP:ㅤ{}\n|DIARIA:ㅤ{}\n|COMODOS:ㅤ{}".format(resultados[0],resultados[1],resultados[2], resultados[3], resultados[4], resultados[5], resultados[6], resultados[7], resultados[8],resultados[9]))
                if resultados == None:
                    print('Nenhum Resultado Para esse ID🙄❌❗\n')
                    time.sleep(2)
                    atualizarImovel()
                else:
                    try:
                        #ESTADO
                        a = input('Alterar Estado?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>>'.format(resultados[2]))
                        if a.lower() == 's':
                            alt_estado = str(input('\n>>>'))
                        elif a.lower() == 'n':
                            alt_estado = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>>")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #CIDADE
                        b = input('Alterar Cidade?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>>'.format(resultados[3]))
                        if b.lower() == 's':
                            alt_cidade = str(input('\n>>>'))
                        elif b.lower() == 'n':
                            alt_cidade = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>>")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #BAIRRO
                        c = input('Alterar Bairro?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>>'.format(resultados[4]))
                        if c.lower() == 's':
                            alt_bairro = str(input('\n>>>'))
                        elif c.lower() == 'n':
                            alt_bairro = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>>")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #RUA
                        d = input('Alterar Rua?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>>'.format(resultados[5]))
                        if d.lower() == 's':
                            alt_rua = str(input('\n>>>'))
                        elif d.lower() == 'n':
                            alt_rua = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>>")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #NUMERO
                        e = input('Alterar Numero?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>>'.format(resultados[6]))
                        if e.lower() == 's':
                            alt_numero = str(input('\n>>>'))
                        elif e.lower() == 'n':
                            alt_numero = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>>")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #CEP
                        f = input('Alterar CEP?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>>'.format(resultados[7]))
                        if f.lower() == 's':
                            alt_cep = str(input('\n>>>'))
                        elif f.lower() == 'n':
                            alt_cep = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>>")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #VALOR DIARIA
                        g = input('Alterar Valor Diaria?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>>'.format(resultados[8]))
                        if g.lower() == 's':
                            alt_diaria = str(input('\n>>>'))
                        elif g.lower() == 'n':
                            alt_diaria = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>>")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #QUANTIDADE COMODOS
                        h = input('Alterar Quantidade de Comodos?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>>'.format(resultados[9]))
                        if h.lower() == 's':
                            alt_comodos = str(input('\n>>>'))
                        elif h.lower() == 'n':
                            alt_comodos = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>>")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        # Query corrigida - só atualiza campos não nulos
                        query = "UPDATE TBL_imovel SET "
                        params = []
                        updates = []
                        if alt_estado is not None:
                            updates.append("estado_imovel = %s")
                            params.append(alt_estado)
                        if alt_cidade is not None:
                            updates.append("cidade_imovel = %s")
                            params.append(alt_cidade)
                        if alt_bairro is not None:
                            updates.append("bairro_imovel = %s")
                            params.append(alt_bairro)
                        if alt_rua is not None:
                            updates.append("rua_imovel = %s")
                            params.append(alt_rua)
                        if alt_numero is not None:
                            updates.append("numero_imovel = %s")
                            params.append(alt_numero)
                        if alt_cep is not None:
                            updates.append("cep_imovel = %s")
                            params.append(alt_cep)
                        if alt_diaria is not None:
                            updates.append("diaria_imovel = %s")
                            params.append(alt_diaria)
                        if alt_comodos is not None:
                            updates.append("comodos_imovel = %s")
                            params.append(alt_comodos)

                        if updates:
                            query += ", ".join(updates) + " WHERE id_imovel = %s"
                            params.append(idAtt)

                            cursor.execute(query, params)
                            db.commit()
                            print("Alterando dados...⏳")
                            cursor.close()
                            db.close()
                            time.sleep(2)
                            print('Dados Alterados!🔧✅')
                            time.sleep(3)
                            main()
                        else:
                            print('Nenhum campo foi alterado.🔄')
                            time.sleep(3)
                            main()

                    except ValueError:
                        print("Comando invalido")
                        atualizarImovel()

    except ValueError:
        atualizarImovel()

def listarImoveis():
    print('Lista de Imoveis: \n')
    #Qtd de linhas do select
    cursor.execute("SELECT * FROM TBL_imovel")
    rows = cursor.fetchall()
    db.commit()

    #O '//' na equação significa divisão sem resto; Numero de paginas será arredondando p baixo...e somarei + 1 se houver resto
    #Ex: 23 itens 23/5 = 4pg inteira + 1 pois há resto
    paginaAtual = 1
    Qtd_paginas = (len(rows)//5)+1 #Quero dividir: 5 por pagina entao Total de linhas / 5
    #len = Comprimento (Quantidade de linhas/rows)

    cursor.execute("Select * from TBL_imovel LIMIT 5;")
    data = cursor.fetchall()
    db.commit()
    for resultado in data:
        print(f"\n>>>ID: {resultado[0]} |\n>>>{resultado[1]} |\n>>>Estado: {resultado[2]} |\n>>>Cidade: {resultado[3]} |\n>>>Bairro: {resultado[4]} |\n>>>Rua: {resultado[5]} |\n>>>Numero: {resultado[6]} |\n>>>Cep: {resultado[7]} |\n>>>Diaria: {resultado[8]} |\n>>>Comodos: {resultado[9]}")
        # table = Table(show_header=True, header_style="bold magenta")
        # table.add_column("ID", style="dim", width=12)
        # table.add_row(str(resultado[0]))
        # print(table)
    print("Pagina: |{}| de |{}|\n".format(paginaAtual,Qtd_paginas))

    def listandoImoveis():
        comando = input("🔧Comandos Disponíveis🔧:\n|A| Para atualizar imoveis🏡\n|S| Para sair🏃💨\nDigite o número da pagina📃\n>>>")
        #EXECUTA O CODIGO DE ACORDO COM O INPUT
        try:
            if comando.lower() == "s":
                print("Ação cancelada.\n")
                main()
            elif comando.lower() == "a":
                print("Atualizar Imoveis...\n")
                time.sleep(1.5)
                atualizarImovel()
            else:
                pagina = int(comando)
                if pagina == 0:
                    print("Você digitou: {}...👀".format(pagina))
                    pagina = int(1)
                    time.sleep(1.2)
        
            if type(pagina) == int:
                ## CODIGO PARA VER MAIS PAGINAS
                print("Buscando dados...⏳⚒")
                time.sleep(1.2)
                if pagina > Qtd_paginas:
                    ultimaPg = (Qtd_paginas*5)-5
                    cursor.execute("SELECT * FROM TBL_imovel LIMIT 5 OFFSET %s;", (ultimaPg,))
                    resultados = cursor.fetchall()
                    db.commit()
                    for resultado in resultados:
                        print(f"\n>>>ID: {resultado[0]} |\n>>>{resultado[1]} |\n>>>Estado: {resultado[2]} |\n>>>Cidade: {resultado[3]} |\n>>>Bairro: {resultado[4]} |\n>>>Rua: {resultado[5]} |\n>>>Numero: {resultado[6]} |\n>>>Cep: {resultado[7]} |\n>>>Diaria: {resultado[8]} |\n>>>Comodos: {resultado[9]}")
                    print("Você está na pagina: ",Qtd_paginas," De", Qtd_paginas)
                    print("Numero da pagina maior que o limite de: {}😅\nExibindo Ultima Página\n".format(Qtd_paginas))
                else:
                    dadosDaPagina = (pagina*5)-5
                    cursor.execute("SELECT * FROM TBL_imovel LIMIT 5 OFFSET %s;", (dadosDaPagina,))
                    resultados = cursor.fetchall()
                    db.commit()
                    for resultado in resultados:
                        print(f"\n>>>ID: {resultado[0]} |\n>>>{resultado[1]} |\n>>>Estado: {resultado[2]} |\n>>>Cidade: {resultado[3]} |\n>>>Bairro: {resultado[4]} |\n>>>Rua: {resultado[5]} |\n>>>Numero: {resultado[6]} |\n>>>Cep: {resultado[7]} |\n>>>Diaria: {resultado[8]} |\n>>>Comodos: {resultado[9]}")
                    print("Você está na pagina: ",pagina," De", Qtd_paginas)

                listandoImoveis()
            else:
                print("Comando inválido🤔")
        except ValueError:  # Se não conseguir converter para int
            print("ERRO!\nDigite apenas 👉números inteiros👈 para as paginas ou 'S' para sair.🤙\n>>>")
            listandoImoveis()
    listandoImoveis()