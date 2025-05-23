#======================================================================================#
#                                  📃 Imports 📃                                      # 
#======================================================================================#
import time
import math
from datetime import datetime
from conection import *
#======================================================================================#
#                             📃 Variaveis Globais 📃                                 # 
#======================================================================================#
header = str("""
██╗░░██╗░█████╗░███╗░░░███╗███████╗███████╗██╗░░░██╗
██║░░██║██╔══██╗████╗░████║██╔════╝██╔════╝╚██╗░██╔╝
███████║██║░░██║██╔████╔██║█████╗░░█████╗░░░╚████╔╝░
██╔══██║██║░░██║██║╚██╔╝██║██╔══╝░░██╔══╝░░░░╚██╔╝░░
██║░░██║╚█████╔╝██║░╚═╝░██║███████╗██║░░░░░░░░██║░░░
╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░░░░╚═╝░░░
|============|Seu Gerenciador de Imoveis|==========|""")
#======================================================================================#
#                                 📃 Tela Index 📃                                    # 
#======================================================================================#
def telaInicio():
    print(header)
    comandoInicio = str(input(">>>Digite o comando\n|0|🔐 LOGIN\n|1|📃 CADASTRAR USUÁRIO\n>>> "))
    if(comandoInicio == str(0)):
        autenticarLogin()
    elif(comandoInicio == str(1)):
        cadastroADM()
    else:
        telaInicio()
#======================================================================================#
#                          📦📮 Autenticação de Login 📦📮                           #
#======================================================================================#
def autenticarLogin():
    usuario = input("Login\n>>> ")
    senha = input("Senha\n>>> ")
    cursor.execute("SELECT nome_adm,email_adm,senha_adm FROM tbl_adm WHERE email_adm = %s and senha_adm = %s;",(usuario,senha,))
    login = cursor.fetchone()
    if login == None:
        print("Login ou usuário incorretos!\n")
        time.sleep(2)
        telaInicio()
    else:
        try:
            admNome = login[0]
            admLogin = login[1]
            admSenha = login[2]
            if usuario == admLogin and senha == admSenha:
                print(('Seja Bem Vindo {} Ao...').format(admNome))
                time.sleep(2)
                main()
            else:
                print("Erro!\nUsuario ou senha incorretos!")
                telaInicio()
        except ValueError:
            print("Erro com login\n")
            telaInicio()
#======================================================================================#
#                        🏡👈❌ Remoção de Imoveis 🏡👈❌                           #
#======================================================================================#
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
        print(f"Descrição: {resultados[1]}")
        print(f"Estado: {resultados[2]}")
        print(f"Cidade: {resultados[3]}")
        print(f"Bairro: {resultados[4]}")
        print(f"Rua: {resultados[5]}")
        print(f"Numero: {resultados[6]}")
        print(f"Cep: {resultados[7]}")
        print(f"Diaria: {resultados[8]}")
        print(f"Comodos: {resultados[9]}")
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
#======================================================================================#
#                            ✍ Cadastro de Imoveis 📄                                #
#======================================================================================#
def cadastroImovel():
    cadastrandoImovel = True
    while cadastrandoImovel:
        print('Tela de cadastro, digite os dados abaixo: ✍ 📄\n')
        print('Para cancelar❌:\nDeixe o campo vazio e aperte "ENTER"\n')
        descricao = str(input('Digite a Descricão:\n>>>  '))
        if descricao == "":
            print("Saindo...\n")
            time.sleep(1)
            break
        estado = str(input('Digite o Estado:\n>>> '))
        if estado == "":
            print("Saindo...\n")
            time.sleep(1)
            break
        cidade = str(input('Digite a Cidade:\n>>> '))
        if cidade == "":
            print("Saindo...\n")
            time.sleep(1)
            break
        bairro = str(input('Digite o Bairro:\n>>> '))
        if bairro == "":
            print("Saindo...\n")
            time.sleep(1)
            break
        rua = str(input('Digite a Rua:\n>>> '))
        if rua == "":
            print("Saindo...\n")
            time.sleep(1)
            break

        #PODE TER LETRA EX: 123-B
        numero = input('Digite o Numero:\n>>> ')
        if numero == "":
            print("Saindo...\n")
            time.sleep(1)
            break

        #CEP
        cep = str(input('Digite o Cep:\n>>> ').strip())
        if cep == "":
            print("Saindo...\n")
            time.sleep(1)
            break
        #VERIFICAR SE DIÁRIA É NUMERO E/OU FLOAT
        diaria = input('Digite o Valor da Diaria:\n>>> ')
        if diaria == "":
            print("Saindo...\n")
            time.sleep(1)
            break
        else:
            try:
                #VERIFICA SE ESCREVEU CERTO
                floatDiaria = float(diaria)
                if type(floatDiaria) == float:
                    diaria = floatDiaria
                #SE ESCREVEU ERRADO MANDA MENSAGEM E VAI PARA O EXCEPT:
                else:
                    print("Diária digitada de forma errada...\n")
                    print("Você digitou:",diaria)
                    time.sleep(2)
            except ValueError:
                    # VAMOS FICAR AQUI ATÉ ELA RESOLVER DIGITAR CORRETAMENTE:
                    while type(diaria) != float:
                        diaria = input('Digite o Valor da Diaria de forma correta.\nEX: 19.99\n>>> ')
                        #VERIFICA SE DIGITOU CERTO
                        try:
                            floatDiaria = float(diaria)
                            if type(floatDiaria) == float:
                                diaria = floatDiaria
                                continue
                        #SE NÃO DIGITOU DA ERRO E VOLTA E DA O EXEMPLO
                        except ValueError:
                            print("Vamos tentar novamente🔄️\n>>> ")
                            time.sleep(1)

        comodos = input('Digite Quantos comodos:\n>>> ')
        if comodos == "":
            print("Saindo...\n")
            time.sleep(1)
            break
        else:
            try:
                #VERIFICA SE ESCREVEU CERTO
                intComodos = int(comodos)
                if type(intComodos) == int:
                    comodos = intComodos
                #SE ESCREVEU ERRADO MANDA MENSAGEM E VAI PARA O EXCEPT:
                else:
                    print("Comodos apenas numeros inteiros...\n")
                    print("Você digitou:",comodos)
                    time.sleep(2)
            except ValueError:
                    # VAMOS FICAR AQUI ATÉ ELA RESOLVER DIGITAR CORRETAMENTE:
                    while type(comodos) != int:
                        comodos = input('Digite a quantidade de comodos de forma correta.\nEX: 5\n>>> ')
                        #VERIFICA SE DIGITOU CERTO
                        try:
                            intComodos = int(comodos)
                            if type(intComodos) == int:
                                comodos = intComodos
                                continue
                        #SE NÃO DIGITOU DA ERRO E VOLTA E DA O EXEMPLO
                        except ValueError:
                            print("Vamos tentar novamente🔄️\n")
                            time.sleep(1)
        print('Deseja cadastrar o seguinte imovel?\n>>> Descrição: {}\n>>> Estado: {}\n>>> Cidade: {}\n>>> Bairro: {}\n>>> Rua: {}\n>>> Numero: {}\n>>> Cep: {}\n>>> Diária: {}\n>>> Comodos: {}'.format(descricao,estado,cidade,bairro,rua,numero,cep,diaria,comodos))
        comando = input('|S| Sim \n|N| Não\n')
        if comando.lower() == 's':
            cursor.execute(
            "INSERT INTO TBL_imovel (descricao_imovel,estado_imovel,cidade_imovel,bairro_imovel,rua_imovel,numero_imovel,cep_imovel,diaria_imovel,comodos_imovel) " 
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);",(descricao,estado,cidade,bairro,rua,numero,cep,diaria,comodos))
            cursor.fetchone()
            db.commit()
            print('Dados Salvos! ✅')
            time.sleep(2)
            main()
            cadastrandoImovel = False
        elif comando.lower() == "n":
            print("Ok...")
            time.sleep(2)
        else:
            print('Voltando a pagina inicial...')
            time.sleep(2)
            break
    cadastrandoImovel = False
    main()
#======================================================================================#
#                                🏡 Tela de Inicio 🏡                                 # 
#======================================================================================#
def main():
    print(header)
    print("Bem vindo(a) ao ARBINHO 🏡")
    print("|1| Cadastrar Imovel✍ ✅\n|2| Listar Imoveis📑🔍\n|3| Atualizar Imovel🔧🔄\n|4| Remover Imovel💣❌\n|5| Cadastro Cliente📃✍\n|6| Listar Cliente e Editar🔧✍🕴\n|7| Atribuir Cliente ao Imovel...🏡🏃💨\n|8| Adicionar ADM...👨\n|9| Remover ADM❌👨\n|10| Pagamentos💵\n")
    print("|0| SAIR❌")
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
    elif(comando == str(5)):
        print("Cadastro Cliente...📃✍")
        cadastroClinte()
    elif(comando == str(6)):
        print("Listar e Editar Cientes...🔧✍🕴")
        listarCliente()
    elif(comando == str(7)):
        print("Atribuir Cliente ao Imovel...🏡🏃💨")
        time.sleep(1.5)
        atribuirCliente()
    elif(comando == str(8)):
        print("Adicionar ADMc")
        cadastroADM()
    elif(comando == str(9)):
        print("Remover ADM")
        removerADM()
    elif(comando == str(10)):
        print("Pagamentos...")
        time.sleep(1)
        pagamentos()
    elif(comando == str(0)):
        print("SAINDO...🏃💨")
        telaInicio()
        main()
    else:
        print("❗Comando invalido❗")
        main()
#======================================================================================#
#                            🔧Tela de alterar dados🔄                                #
#======================================================================================#
def atualizarImovel():
    print('Atualizar Dados🛠\n')
    #Pede o ID do imovel a ser atualizado
    comando = input("Comandos Disponiveis: \n|D| Detalhes\n|S| Sair\nID que deseja alterar🔧\n>>> ")
    try:
        if comando.lower() == str("d"):
            print("Indo para Listagem de imoveis🏡...")
            time.sleep(1.2)
            listarImoveis()
        elif comando.lower() == "s":
            print("Saindo...🏃💨")
            time.sleep(1.2)
            main()
        else:
            idAtt = int(comando)
            if type(idAtt) == int:
                cursor.execute("SELECT * FROM TBL_imovel WHERE id_imovel = %s", (idAtt,))
                resultados = cursor.fetchone()
                print("===Você está editando🔧✍===\n|ID:ㅤ{}\n|DESCRIÇÃO:ㅤ{}\n|ESTADO:ㅤ{}\n|CIDADE:ㅤ{}\n|BAIRRO:ㅤ{}\n|RUA:ㅤ{}\n|NUMERO:ㅤ{}\n|CEP:ㅤ{}\n|DIARIA:ㅤ{}\n|COMODOS:ㅤ{}".format(resultados[0],resultados[1],resultados[2], resultados[3], resultados[4], resultados[5], resultados[6], resultados[7], resultados[8],resultados[9]))
                if resultados == None:
                    print('Nenhum Resultado Para esse ID🙄❌❗\n')
                    time.sleep(2)
                    atualizarImovel()
                else:
                    try:
                        #ESTADO
                        a = input('\nAlterar Estado?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[2]))
                        if a.lower() == 's':
                            alt_estado = str(input('\n>>> '))
                        elif a.lower() == 'n':
                            alt_estado = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #CIDADE
                        b = input('Alterar Cidade?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[3]))
                        if b.lower() == 's':
                            alt_cidade = str(input('\n>>> '))
                        elif b.lower() == 'n':
                            alt_cidade = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #BAIRRO
                        c = input('Alterar Bairro?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[4]))
                        if c.lower() == 's':
                            alt_bairro = str(input('\n>>> '))
                        elif c.lower() == 'n':
                            alt_bairro = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #RUA
                        d = input('Alterar Rua?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[5]))
                        if d.lower() == 's':
                            alt_rua = str(input('\n>>> '))
                        elif d.lower() == 'n':
                            alt_rua = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #NUMERO
                        e = input('Alterar Numero?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[6]))
                        if e.lower() == 's':
                            alt_numero = str(input('\n>>> '))
                        elif e.lower() == 'n':
                            alt_numero = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #CEP
                        f = input('Alterar CEP?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[7]))
                        if f.lower() == 's':
                            alt_cep = str(input('\n>>> '))
                            if alt_cep == "":
                                print("Saindo...\n")
                                alt_cep = None
                                time.sleep(2)
                                atualizarImovel()
                        elif f.lower() == 'n':
                            alt_cep = None  # Mantém como None para não atualizar
                            print('OK\n')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #VALOR DIARIA
                        g = input('Alterar Valor Diaria?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[8]))
                        if g.lower() == 's':
                            alt_diaria = str(input('\n>>> '))
                            try:
                                #VERIFICA SE ESCREVEU CERTO
                                alt_floatDiaria = float(alt_diaria)
                                if type(alt_floatDiaria) == float:
                                    alt_diaria = alt_floatDiaria
                                #SE ESCREVEU ERRADO MANDA MENSAGEM E VAI PARA O EXCEPT:
                                else:
                                    print("Diária digitada de forma errada...\n")
                                    print("Você digitou:",alt_diaria)
                                    time.sleep(2)
                            except ValueError:
                                # VAMOS FICAR AQUI ATÉ ELA RESOLVER DIGITAR CORRETAMENTE:
                                while type(alt_diaria) != float:
                                    alt_diaria = input('Digite o Valor da Diaria de forma correta.\nEX: {}\n>>>  '.format(resultados[8]))
                                    #VERIFICA SE DIGITOU CERTO
                                    try:
                                        alt_floatDiaria = float(alt_diaria)
                                        if type(alt_floatDiaria) == float:
                                            alt_diaria = alt_floatDiaria
                                            continue
                                    #SE NÃO DIGITOU DA ERRO E VOLTA E DA O EXEMPLO
                                    except ValueError:
                                        print("Vamos tentar novamente🔄️\n>>> ")
                                        time.sleep(1)
                        elif g.lower() == 'n':
                            alt_diaria = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                            time.sleep(3)
                            print("Retornando ao inicio...🔄")
                            time.sleep(1.2)
                            atualizarImovel()
                        #QUANTIDADE COMODOS
                        h = input('Alterar Quantidade de Comodos?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[9]))
                        if h.lower() == 's':
                            alt_comodos = str(input('\n>>> '))
                        elif h.lower() == 'n':
                            alt_comodos = None  # Mantém como None para não atualizar
                            print('OK\n ')
                        else:
                            print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
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
#======================================================================================#
#                                 📃 Função Listar 📃                                 # 
#======================================================================================#
def listarImoveis():    
    print('Lista de Imoveis: \n')
    #Qtd de linhas do select
    cursor.execute("SELECT * FROM tbl_imovel;")
    rows = cursor.fetchall()

    #O '//' na equação significa divisão sem resto; Numero de paginas será arredondando p baixo...e somarei + 1 se houver resto
    #Ex: 23 itens 23/5 = 4pg inteira + 1 pois há resto
    paginaAtual = 1
    Qtd_paginas = math.ceil(len(rows)/5) #Quero dividir: 5 por pagina entao Total de linhas / 5
    #len = Comprimento (Quantidade de linhas/rows)

    cursor.execute("Select * from TBL_imovel LIMIT 5;")
    data = cursor.fetchall()
    for resultado in data:
        print(f"\n>>> ID: {resultado[0]} |\n>>> {resultado[1]} |\n>>> Estado: {resultado[2]} |\n>>> Cidade: {resultado[3]} |\n>>> Bairro: {resultado[4]} |\n>>> Rua: {resultado[5]} |\n>>> Numero: {resultado[6]} |\n>>> Cep: {resultado[7]} |\n>>> Diaria: {resultado[8]} |\n>>> Comodos: {resultado[9]}")
        print("Pagina: |{}| de |{}|\n".format(paginaAtual,Qtd_paginas))

    def listandoImoveis():
        comando = input("🔧Comandos Disponíveis🔧:\n|A| Para atualizar imoveis🏡\n|S| Para sair🏃💨\nDigite o número da pagina📃\n>>> ")
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
                    for resultado in resultados:
                        print(f"\n>>> ID: {resultado[0]} |\n>>> {resultado[1]} |\n>>> Estado: {resultado[2]} |\n>>> Cidade: {resultado[3]} |\n>>> Bairro: {resultado[4]} |\n>>> Rua: {resultado[5]} |\n>>> Numero: {resultado[6]} |\n>>> Cep: {resultado[7]} |\n>>> Diaria: {resultado[8]} |\n>>> Comodos: {resultado[9]}")
                        print("Você está na pagina: ",Qtd_paginas," De", Qtd_paginas)
                        print("Numero da pagina maior que o limite de: {}😅\nExibindo Ultima Página\n".format(Qtd_paginas))
                else:
                    dadosDaPagina = (pagina*5)-5
                    cursor.execute("SELECT * FROM TBL_imovel LIMIT 5 OFFSET %s;", (dadosDaPagina,))
                    resultados = cursor.fetchall()
                    for resultado in resultados:
                        print(f"\n>>> ID: {resultado[0]} |\n>>> {resultado[1]} |\n>>> Estado: {resultado[2]} |\n>>> Cidade: {resultado[3]} |\n>>> Bairro: {resultado[4]} |\n>>> Rua: {resultado[5]} |\n>>> Numero: {resultado[6]} |\n>>> Cep: {resultado[7]} |\n>>> Diaria: {resultado[8]} |\n>>> Comodos: {resultado[9]}")
                        print("Você está na pagina: ",pagina," De", Qtd_paginas)

                listandoImoveis()
            else:
                print("Comando inválido🤔")
        except ValueError:  # Se não conseguir converter para int
            print("ERRO!\nDigite apenas 👉números inteiros👈 para as paginas ou 'S' para sair.🤙\n>>> ")
            listandoImoveis()
    listandoImoveis()
#======================================================================================#
#                             ✍ cadastro de Cliente ✍                               # 
#======================================================================================#
def cadastroClinte():
    cadastroCliente = True
    while cadastroCliente:
        print("Para cancelar❌\nDeixe o campo vazio e aperte 'ENTER'")
        nome = str(input('Digite seu Nome Completo:\n>>> '))
        if nome == "":
            print("Saindo...\n")
            time.sleep(1)
            cadastroCliente = False
            main()
            break
        
        email = str(input('Digite seu Email:\n>>> '))
        if email == "":
            print("Saindo...\n")
            time.sleep(1)
            cadastroCliente = False
            main()
            break
        telefone = str(input('Digite seu Telefone:\n>>> '))
        if telefone == "":
            print("Saindo...\n")
            time.sleep(1)
            cadastroCliente = False
            main()
            break

        # VALIDADOR DE CPF
        cpf = input('Digite Seu CPF\n>>> ')
        d1 = int(cpf[0]) * 10
        d2 = int(cpf[1]) * 9
        d3 = int(cpf[2]) * 8
        d4 = int(cpf[3]) * 7
        d5 = int(cpf[4]) * 6
        d6 = int(cpf[5]) * 5
        d7 = int(cpf[6]) * 4
        d8 = int(cpf[7]) * 3
        d9 = int(cpf[8]) * 2
        d10 = int(cpf[9]) 

        soma = d1+d2+d3+d4+d5+d6+d7+d8+d9
        multiplicacao = soma * 10
        restDivisao = multiplicacao % 11

        if restDivisao == 10:
            restDivisao = 0
        if restDivisao == d10:
            print('Validando seu CPF...')
            time.sleep(1)
            print('Sucesso! Seu CPF é valido!')
            time.sleep(1)
        else:
            print('CPF INVALIDO!!!')
            print('Retornando ao Inicio...')
            time.sleep(1)
            main()
        if cpf == "":    
            print("Saindo...\n")
            time.sleep(1)
            cadastroCliente = False
            main()
            break

        print("===Pronto para registro===\n")
        print(">>> NOME| {}\n>>> EMAIL| {}\n>>> TELEFONE| {}\n>>> CPF| {}\n".format(nome, email, telefone,cpf))
        print("Os dados estão corretos?\n|S| Sim\n|N| Não")
        resposta = input("\n>>> ")
        if resposta.lower() == "s":
            cursor.execute(
                "INSERT INTO TBL_cliente (nome_cliente,email_cliente,telefone_cliente,cpf_cliente)" 
                "VALUES (%s,%s,%s,%s);",(nome,email,telefone,cpf))
            cursor.fetchone()
            db.commit()
            print('Dados Salvos! ✅')
            main()
        else:
            cadastroCliente = False
            print("Saindo...\n")
            time.sleep(1.5)
            break
    main()
#======================================================================================#
#                     🏡➕🏃‍♂️💨 Atribuir Cliente ao Imovel 🏡➕🏃‍♂️💨                  # 
#======================================================================================#
def atribuirCliente():
    print('Tela para Atribuir Cliente ao Imovel🏡🏃💨\n')
    comando = input('Pressione |A| para Atribuir\n Digite |ENTER| para sair\n>>> ')
    if comando == "":
        print('Retornando ao Inicio...')
        time.sleep(1.2)
        main()
    else:
        print('>>>Caso queira sair, pressione o enter duas vezes<<<\n')
        try:
            idCliente = input('Digite o ID do cliente que deseja atribuir ao Imovel:\n>>> ')
            idImovel = input('Digite o ID do Imovel que deseja atribuir ao cliente:\n>>> ')
            cursor.execute(
            "UPDATE TBL_imovel SET fk_TBL_imovel_id_cliente = %s WHERE id_imovel = %s;",(idCliente,idImovel))
            cursor.fetchone()
            cursor.execute("SELECT tbl_cliente.nome_cliente, tbl_imovel.descricao_imovel FROM tbl_imovel INNER JOIN tbl_cliente ON fk_TBL_imovel_id_cliente = id_cliente WHERE id_cliente = %s;",(idCliente,))
            cliente = cursor.fetchall()
            db.commit()
        except ValueError:  # Se não conseguir converter para int
            print("ERRO!\nDigite apenas números inteiros para o ID.")
            main()

        for data in cliente:
            print("O cliente: {} Está na casa: {}".format(data[0], data[1]))
    main()
#======================================================================================#
#                                👨‍💻 Adicionar ADM 👨‍💻                                  # 
#======================================================================================#
def cadastroADM():
    print("===|TELA CADASTRO|===\n")
    nome = str(input('Digite seu nome::\n'))
    email = str(input('Coloque seu email:\n'))
    senha = str(input('Crie sua senha:\n'))
        
    cursor.execute(
        "INSERT INTO TBL_adm (nome_adm,email_adm,senha_adm) " 
        "VALUES (%s,%s,%s);",(nome,email,senha))
    cursor.fetchone()
    db.commit()
    print('Dados Salvos! ✅')
    time.sleep(1.5)
    main()
#======================================================================================#
#                                👨‍💻 Remover ADM 👨‍💻                                    # 
#======================================================================================#
def removerADM():
    id_remover = input('Digite o ID do ADM que deseja remover | Para sair digite: S\n>>>')
    if id_remover.lower() == "s":
        print("Saindo...\n")
        time.sleep(1)
        main()
    else:
        try:
            id_adm = int(id_remover)
            if type(id_adm) == int:  # Verifica se realmente é inteiro
                id_remover = id_adm
                # Remover adm com o input
                cursor.execute("SELECT * FROM TBL_adm WHERE id_adm = %s;", (id_adm,))
                resultados = cursor.fetchone()
            if resultados == None:
                print('Nenhum Resultado Para ', id_remover,'\n')
                removerADM()

        except ValueError:  # Se não conseguir converter para int
            print("ERRO!\nDigite apenas números inteiros para o ID.")
            removerADM()
        if resultados:
            print("\nDados do ADM encontrado:")
            print(f"ID: {resultados[0]}")
            print(f"Nome: {resultados[1]}")
            print(f"Email: {resultados[2]}")
            print(f"Senha: {resultados[3]}")
        confirmacaoADM = input('Deseja remover este adm ?\n=====================\n|S| = Sim\n|N| = Não):\n')
        if confirmacaoADM.lower() == 's':
            cursor.execute("DELETE FROM tbl_adm WHERE id_adm = %s;", (id_adm,))
            db.commit()
            print("\nADM removido com sucesso!")
            removerADM()
        else:
            print("Ação cancelada!")
            removerADM()
    removerADM()
#======================================================================================#
#                        🔧✍🕴 Listar e Editar cliente 🔧✍🕴                      # 
#======================================================================================#
def listarCliente():
    print('Lista de Clientes: \n')
    #Qtd de linhas do select
    cursor.execute("SELECT * FROM TBL_cliente")
    rows = cursor.fetchall()
    db.commit()

    #O '//' na equação significa divisão sem resto; Numero de paginas será arredondando p baixo...e somarei + 1 se houver resto
    #Ex: 23 itens 23/5 = 4pg inteira + 1 pois há resto
    paginaAtual = 1
    Qtd_paginas = math.ceil(len(rows)/5) #Quero dividir: 5 por pagina entao Total de linhas / 5
    #len = Comprimento (Quantidade de linhas/rows)

    cursor.execute("Select * from TBL_cliente LIMIT 5;")
    data = cursor.fetchall()
    db.commit()
    for resultado in data:
        print(f"\n>>> ID: {resultado[0]} |\n>>> Nome: {resultado[1]} |\n>>> Email: {resultado[2]} |\n>>> Telefone: {resultado[3]} |\n>>> CPF: {resultado[4]}")
    print("Pagina: |{}| de |{}|\n".format(paginaAtual,Qtd_paginas))

    def listandoCliente():
        comando = input("🔧Comandos Disponíveis🔧:\n|A| Para atualizar um cliente🏡\n|R| Remover Cliente❌💣\n|S| Para sair🏃💨\nDigite o número da pagina📃\n>>> ")
        #EXECUTA O CODIGO DE ACORDO COM O INPUT
        try:
            if comando.lower() == "s":
                print("Ação cancelada.\n")
                main()
            elif comando.lower() == "a":
                print("Atualizar Cliente...\n")
                time.sleep(1.5)
                atualizarCliente()
            elif comando.lower() == "r":
                print("Remover Cliente...\n")
                time.sleep(1.5)
                removerCliente() 
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
                    cursor.execute("SELECT * FROM TBL_cliente LIMIT 5 OFFSET %s;", (ultimaPg,))
                    resultados = cursor.fetchall()
                    db.commit()
                    for resultado in resultados:
                        print(f"\n>>> ID: {resultado[0]} |\n>>> Nome: {resultado[1]} |\n>>> Email: {resultado[2]} |\n>>> Telefone: {resultado[3]} |\n>>> CPF : {resultado[4]} ")
                    print("Você está na pagina: ",Qtd_paginas," De", Qtd_paginas)
                    print("Numero da pagina maior que o limite de: {}😅\nExibindo Ultima Página\n".format(Qtd_paginas))
                else:
                    dadosDaPagina = (pagina*5)-5
                    cursor.execute("SELECT * FROM TBL_cliente LIMIT 5 OFFSET %s;", (dadosDaPagina,))
                    resultados = cursor.fetchall()
                    db.commit()
                    for resultado in resultados:
                        print(f"\n>>> ID: {resultado[0]} |\n>>> Nome: {resultado[1]} |\n>>> Email: {resultado[2]} |\n>>> Telefone: {resultado[3]} |\n>>> CPF: {resultado[4]}")
                    print("Você está na pagina: ",pagina," De", Qtd_paginas)

                listandoCliente()
            else:
                print("Comando inválido🤔")
        except ValueError:  # Se não conseguir converter para int
            print("ERRO!\nDigite apenas 👉números inteiros👈 para as paginas ou 'S' para sair.🤙\n>>> ")
            listandoCliente()
    listandoCliente()
def atualizarCliente():
        print('Atualizar Dados🛠\n')
        #Pede o ID do imovel a ser atualizado
        comando = input("Comandos Disponiveis: \n|D| Detalhes\n|S| Sair\nID que deseja alterar🔧\n>>> ")
        try:
            if comando.lower() == str("d"):
                print("Indo para Listagem de Clientes🙅...")
                time.sleep(1.2)
                listarCliente()
            elif comando.lower() == "s":
                print("Saindo...🏃💨")
                time.sleep(1.2)
                main()
            else:
                idAtt = int(comando)
                if type(idAtt) == int:
                    cursor.execute("SELECT * FROM TBL_cliente WHERE id_cliente = %s", (idAtt,))
                    resultados = cursor.fetchone()
                    db.commit()
                    print("===Você está editando🔧✍===\n|ID:ㅤ{}\n|NOME:ㅤ{}\n|EMAIL:ㅤ{}\n|TELEFONE:ㅤ{}\n|CPF:ㅤ{}\n".format(resultados[0],resultados[1],resultados[2], resultados[3], resultados[4]))
                    if resultados == None:
                        print('Nenhum Resultado Para esse ID🙄❌❗\n')
                        time.sleep(2)
                        atualizarCliente()
                    else:
                        try:
                            #NOME CLIENTE
                            a = input('Alterar Nome?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[1]))
                            if a.lower() == 's':
                                alt_nome = str(input('\n>>> '))
                            elif a.lower() == 'n':
                                alt_nome = None  # Mantém como None para não atualizar
                                print('OK\n')
                            else:
                                print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                                time.sleep(3)
                                print("Retornando ao inicio...🔄")
                                time.sleep(1.2)
                                atualizarCliente()
                            #EMAIL
                            b = input('Alterar Email?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[2]))
                            if b.lower() == 's':
                                alt_email = str(input('\n>>> '))
                            elif b.lower() == 'n':
                                alt_email = None  # Mantém como None para não atualizar
                                print('OK\n ')
                            else:
                                print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                                time.sleep(3)
                                print("Retornando ao inicio...🔄")
                                time.sleep(1.2)
                                atualizarCliente()
                            #TELEFONE
                            c = input('Alterar Telefone?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[3]))
                            if c.lower() == 's':
                                alt_telefone = str(input('\n>>> '))
                            elif c.lower() == 'n':
                                alt_telefone = None  # Mantém como None para não atualizar
                                print('OK\n ')
                            else:
                                print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                                time.sleep(3)
                                print("Retornando ao inicio...🔄")
                                time.sleep(1.2)
                                atualizarCliente()
                            #CPF
                            d = input('Alterar CPF?\n===|{}|===\n|S| Sim✅\n|N| Não❌\n>>> '.format(resultados[4]))
                            if d.lower() == 's':
                                alt_cpf = input('Digite Seu CPF\n>>> ')
                                d1 = int(alt_cpf[0]) * 10
                                d2 = int(alt_cpf[1]) * 9
                                d3 = int(alt_cpf[2]) * 8
                                d4 = int(alt_cpf[3]) * 7
                                d5 = int(alt_cpf[4]) * 6
                                d6 = int(alt_cpf[5]) * 5
                                d7 = int(alt_cpf[6]) * 4
                                d8 = int(alt_cpf[7]) * 3
                                d9 = int(alt_cpf[8]) * 2
                                d10 = int(alt_cpf[9]) 

                                soma = d1+d2+d3+d4+d5+d6+d7+d8+d9
                                multiplicacao = soma * 10
                                restDivisao = multiplicacao % 11

                                if restDivisao == 10:
                                    restDivisao = 0
                                if restDivisao == d10:
                                    print('Validando seu CPF...')
                                    time.sleep(1)
                                    print('Sucesso! Seu CPF é valido!')
                                    time.sleep(1)
                                else:
                                    print('CPF INVALIDO!!!, Retornando ao Inicio...')
                                    time.sleep(1)
                                    atualizarCliente()
                            elif d.lower() == 'n':
                                alt_cpf = None  # Mantém como None para não atualizar
                                print('OK\n ')
                            else:
                                print("Comando Invalido🙄\nDigite\n|S| Para sim✅\n|N| Para não❌\n>>> ")
                                time.sleep(3)
                                print("Retornando ao inicio...🔄")
                                time.sleep(1.2)
                                atualizarCliente()
                            # Query corrigida - só atualiza campos não nulos
                            query = "UPDATE TBL_cliente SET "
                            params = []
                            updates = []
                            if alt_nome is not None:
                                updates.append("nome_cliente = %s")
                                params.append(alt_nome)
                            if alt_email is not None:
                                updates.append("email_cliente = %s")
                                params.append(alt_email)
                            if alt_telefone is not None:
                                updates.append("telefone_cliente = %s")
                                params.append(alt_telefone)
                            if alt_cpf is not None:
                                updates.append("cpf_cliente = %s")
                                params.append(alt_cpf)

                            if updates:
                                query += ", ".join(updates) + " WHERE id_cliente = %s"
                                params.append(idAtt)

                                cursor.execute(query, params)
                                db.commit()
                                print("Alterando dados...⏳")
                                time.sleep(2)
                                print('Dados Alterados!🔧✅')
                                time.sleep(3)
                                main()
                            else:
                                print('Nenhum campo foi alterado.🔄')
                                time.sleep(3)
                                main()

                        except ValueError:
                            print("Comando invalido❌")
                            time.sleep(2.5)
                            atualizarCliente()
        except ValueError:
            listarCliente()

def removerCliente():
    id_input2 = input('Digite o ID do cliente que deseja remover\nPara sair digite: S\n>>>:')
    try:
        if id_input2.lower() == 's':
            print('Saindo...')
            time.sleep(1)
            main()
        else:
            id_cliente = int(id_input2)
        if type(id_cliente) == int:
            id_cliente = id_input2
            cursor.execute('SELECT * FROM tbl_cliente WHERE id_cliente = %s;', (id_cliente,))
            resultados = cursor.fetchone()
            db.commit()
        if resultados == None:
            print('Nenhum Resultado Para ', id_input2,'\n')
    except ValueError:
        print("ERRO!\nDigite apenas números inteiros para o ID.")
        time.sleep(1)
        removerCliente()

    if resultados:
        print("\nDados do cliente encontrado:")
        print(f"ID: {resultados[0]}")
        print(f"Nome: {resultados[1]}")
        print(f"Email: {resultados[2]}")
        print(f"Telefone: {resultados[3]}")
        print(f"Senha: {resultados[4]}")
        print(f"CPF: {resultados[5]}")
        confirmacaoCliente = input('Deseja remover este cliente ?\n|S|= Sim\n|N|= Não)\n>>>')
        if confirmacaoCliente.lower() == 's':
            cursor.execute("DELETE FROM tbl_cliente WHERE id_cliente = %s;", (id_cliente,))
            db.commit()
            time.sleep(1)
            print("\nCliente removido com sucesso!")
            removerCliente()
        else:
            print("Ação cancelada!")
            time.sleep(1)
            removerCliente()
def adicionarPagamentos():
    print("\nAdicionando pagamento...✅\n")
    time.sleep(1)
    print("Caso queira sair\nDeixe o campo vazio e pressione 'Enter'")

    adicionandoPagamento = True
    while adicionandoPagamento:
        valorPagamento = input('Digite o Valor do pagamento EX: 299.00:\n>>>')
        if valorPagamento == "":
                print("Saindo...\n")
                time.sleep(1)
                # adicionandoPagamento = False
                pagamentos()
        try:
            float_valorPagamento = float(valorPagamento)
            if type(float_valorPagamento) == float:
                valorPagamento = float_valorPagamento
                print("✅\n")
                time.sleep(1)
                break
            elif valorPagamento == "":
                print("Saindo...\n")
                time.sleep(1)
                pagamentos()
            else:
                print("Valor digitado incorretamente...\n")
                print("Você digitou:",valorPagamento)
                time.sleep(2)
        except ValueError:
            print("Voce digitou errado: {}".format(valorPagamento))
            valorPagamento = input('Digite o Valor do pagamento:\n>>>')
    adicionandoPagamento = False

    dataPagamento = True
    while dataPagamento:
        inputDate = str(input("Digite a data de pagamento (formato: dd/mm/aaaa): "))
        if dataPagamento == "":
            print("Saindo...\n")
            time.sleep(1)
            pagamentos()
        try:
            inputDate = datetime.strptime(inputDate, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Tente novamente no formato: dd/mm/aaaa.")
    # Lê a data do usuário
    dbData = inputDate
    # Converte para o formato de banco de dados (aaaa-mm-dd)
    databaseDate = dbData.strftime("%Y-%m-%d")
    print("Data pagamento: {}✅".format(databaseDate))
    dataPagamento = False
    time.sleep(1)
    statusPagamento_ = True #WHILE
    while statusPagamento_:
        statusPagamento = input("Status do pagamento:\n|0| = Pendente🕧\n|1| = Pago✅\n>>>")
        if statusPagamento.lower() == "":
            print("Saindo...\n")
            time.sleep(1)
            pagamentos()
        else:
            if statusPagamento == "1":
                print("Status de definido como: PAGO✅\n")
                statusPagamento = True      #INPUT
                statusPagamento_ = False    #DESLIGAR O WHILE
                break
            elif statusPagamento == "0":
                print("Status definido como: Pendente🕧\n")
                statusPagamento = False     #INPUT
                statusPagamento_ = False    #DESLIGAR O WHILE
                break
            else:
                print("ERRO")
                continue
    formatoPagamento = True
    while formatoPagamento:
        forma_pagamento = input("Descreva a forma de pagamento:\nEx: Pix, Cartão de Credito, Débito, Dinheiro\n>>>")
        if forma_pagamento.lower() == "":
            print("Saindo...")
            time.sleep(1)
            formatoPagamento = False
            break
        else:
            print("Forma de pagamento definido como: {}\n".format(forma_pagamento))
            formatoPagamento = False
            time.sleep(1)
            break
        break

    pagamentoCliente = True
    while pagamentoCliente:
        print("Caso queira sair⬅️\nDeixe o campo vazio e pressione 'Enter'\n")
        id_cliente_pagamento = input("ID do cliente que pagou\n>>>")
        if id_cliente_pagamento == "":
            print("Saindo...")
            time.sleep(1)
            pagamentos()
        try:
            int_id_cliente = int(id_cliente_pagamento)
            if type(int_id_cliente) == int:
                id_cliente_pagamento = int_id_cliente
                print("Id do cliente: {}".format(int_id_cliente))
                # Verificar no banco se existe esse ID e inserir, se não, volta tudo!
                cursor.execute("SELECT * FROM tbl_cliente WHERE id_cliente = %s;",(id_cliente_pagamento,))
                result = cursor.fetchone()
            if result == None:
                print("ID cliente não encontrado❌")
                time.sleep(1.5)
            else:
                print("===============================")
                print("📃Info do Cliente📃\n|ID: {}\n|Nome: {}".format(result[0],result[1]))
                print("===============================")
                time.sleep(1)
        except ValueError:
            print("Comando inválido")
        #SELECT tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_pagamentos.valor_pagamento, tbl_pagamentos.data_pagamento, tbl_pagamentos.status_pagamento FROM Tbl_cliente INNER JOIN tbl_pagamentos ON fk_TBL_cliente_id_cliente = id_cliente where id_cliente = 1
        cursor.execute("SELECT nome_cliente, cpf_cliente FROM TBL_cliente WHERE id_cliente = %s;",(id_cliente_pagamento,))
        pagamentoCliente = False
        resultado = cursor.fetchone()
        print("Cliente: {}\nCPF: {}\nPagamento: R${}\nData do Pagamento: {}\nStatus Pagamento: {}\n|True = Pago✅ | False = Não Pago❌|\nForma de pagamento: {}\n".format(resultado[0],
                                                                                                                                    resultado[1],
                                                                                                                                    valorPagamento,
                                                                                                                                    inputDate.strftime("%d/%m/%Y"),
                                                                                                                                    statusPagamento,
                                                                                                                                    forma_pagamento))
    registeringPayment = True
    while registeringPayment:
        try:
            confirmPayment = input("Deseja registrar o seguinte pagamento?\n|S| Sim\n|N| Não\n>>>")
            if confirmPayment.lower() == "s":
                print("Registrando...")
                time.sleep(1)
                cursor.execute(
                "INSERT INTO tbl_pagamentos (valor_pagamento,data_pagamento,status_pagamento, formato_pagamento,fk_TBL_cliente_id_cliente) "
                "VALUES (%s,%s,%s,%s,%s);",(valorPagamento,inputDate,statusPagamento,forma_pagamento,id_cliente_pagamento))
                db.commit()
                print("Registro concluido!✅")
                
                time.sleep(1)
                registeringPayment = False
                break
            elif confirmPayment.lower() == "n":
                print("ok")
                registeringPayment = False
                time.sleep(1)
                break
        except ValueError:
            print("Comando inválido❌")
            time.sleep(1)
    pagamentos()

def removerPagamento(): 
    id_INPUT = input('Digite o ID do pagamento que deseja remover | Para sair digite: S\n>>>:')
    try:
        if id_INPUT.lower() == 's':
            main()
        int_id_INPUT = int(id_INPUT)
        if type(int_id_INPUT) == int:
            id_INPUT = int_id_INPUT
            cursor.execute('SELECT tbl_pagamentos.id_pagamento, tbl_pagamentos.valor_pagamento, tbl_pagamentos.data_pagamento, tbl_pagamentos.status_pagamento, tbl_pagamentos.formato_pagamento, tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_cliente.cpf_cliente FROM tbl_pagamentos INNER JOIN tbl_cliente ON fk_TBL_cliente_id_cliente = id_cliente WHERE id_pagamento = %s;',(id_INPUT,))
            resultados = cursor.fetchone()     
        if resultados == None:
            print('Nenhum Resultado Para ', id_INPUT,'\n')
            removerPagamento()
    except ValueError:
        print("ERRO!\nDigite apenas números inteiros para o ID.")
        removerPagamento()

    if resultados:
        print("\nDados do pagamento encontrado:\n")
        print(f"ID Pagamento: {resultados[0]}")
        print(f"Valor: {resultados[1]}")
        print(f"Data: {resultados[2]}")
        print(f"Status: {resultados[3]}")
        print(f"Formato: {resultados[4]}")
        print(f"ID Cliente: {resultados[5]}")
        print(f"Nome Cliente: {resultados[6]}")
        print(f"CPF: {resultados[7]}")
        confirmacaoPagamento = input('Deseja remover este pagamento ?\n|S|= Sim\n|N|= Não): \n')
        if confirmacaoPagamento.lower() == 's':
            cursor.execute("DELETE FROM tbl_pagamentos WHERE id_pagamento = %s", (id_INPUT,))
            db.commit()
            print("\nPagamento removido com sucesso!✅💣\n")
            time.sleep(1)
            removerPagamento()
        else:
            print("Ação cancelada!")
            removerPagamento()

def listarPagamentos():
    print("=========💵📃Listar Pagamentos📃💵=========")
    print("Comandos Disponíveis:\n|A| Listar Todos Pagamentos💵\n|B| Listar pagamentos aprovados📃✅\n|C| Listar Pagamentos Pendentes⏳\n")
    
    pgCmd = input(">>>")
    try:
        if pgCmd.lower() == "a":
            print("Listando todos os pagamentos💵")
            time.sleep(1)
            cursor.execute("SELECT * FROM tbl_pagamentos;") #Contar quantas linhas de registro tem
            rows = cursor.fetchall()

            pgPagamentos = 1
            TotalPaginasPg = math.ceil(len(rows)/5)                 #Dividir 5 registros por pagina +1 pq se houver resto add pg


            cursor.execute("SELECT tbl_pagamentos.id_pagamento, tbl_pagamentos.valor_pagamento, tbl_pagamentos.data_pagamento, tbl_pagamentos.status_pagamento, tbl_pagamentos.formato_pagamento, tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_cliente.cpf_cliente, tbl_imovel.id_imovel, tbl_imovel.descricao_imovel FROM tbl_pagamentos INNER JOIN tbl_cliente INNER JOIN tbl_imovel ON fk_TBL_imovel_id_cliente = id_cliente LIMIT 5;")
            data = cursor.fetchall()
            for resultado in data:
                print(f"\n>>> ID: {resultado[0]} |\n>>> Valor Pagamento: {resultado[1]} |\n>>> Data Pagamento: {resultado[2]} |\n>>> Status Pagamento: {resultado[3]} |\n>>> Forma De Pagamento: {resultado[4]} |\n>>> ID Cliente: {resultado[5]} |\n>>> Nome Cliente: {resultado[6]} |\n>>> CPF Cliente: {resultado[7]} |\n>>> ID Imovel: {resultado[8]} |\n>>> Imovel: {resultado[9]}")
                print("Pagina: |{}| de |{}|\n".format(pgPagamentos,TotalPaginasPg))
                print("Você está na pagina: {} de {}\n".format(pgPagamentos,TotalPaginasPg))

            def listandoTodosPg():
                pgPagamentos = True
                while pgPagamentos:
                    noPagina = 0
                    pgPagamentos = input("Digite o número da página\nPara sair Digite: S\n>>>")

                    if pgPagamentos.lower() == "s":
                        print("Saindo...")
                        time.sleep(1)
                        pagamentos()
                    else:
                        try:
                            int_noPagina = int(pgPagamentos)
                            if type(int_noPagina) == int:
                                pgPagamentos = int_noPagina
                                if pgPagamentos > TotalPaginasPg+1:
                                    print("Numero total de páginas é: {}".format(TotalPaginasPg))
                                    listandoTodosPg()
                            else:
                                print("Erro! Digite apenas numeros inteiros para a pagina")
                                listandoTodosPg()
                            
                            noPagina = pgPagamentos
                            pgPagamentos = (pgPagamentos*5)-5
                            cursor.execute("SELECT tbl_pagamentos.id_pagamento, tbl_pagamentos.valor_pagamento, tbl_pagamentos.data_pagamento, tbl_pagamentos.status_pagamento, tbl_pagamentos.formato_pagamento, tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_cliente.cpf_cliente, tbl_imovel.id_imovel, tbl_imovel.descricao_imovel FROM tbl_pagamentos INNER JOIN tbl_cliente INNER JOIN tbl_imovel ON fk_TBL_imovel_id_cliente = id_cliente LIMIT 5 OFFSET %s;",(pgPagamentos,))
                            resultados = cursor.fetchall()
                            for resultado in resultados:
                                print(f"\n>>> ID: {resultado[0]} |\n>>> Valor Pagamento: {resultado[1]} |\n>>> Data Pagamento: {resultado[2]} |\n>>> Status Pagamento: {resultado[3]} |1=Pago✅ 0=Pendente⏳|\n>>> Forma De Pagamento: {resultado[4]} |\n>>> ID Cliente: {resultado[5]} |\n>>> Nome Cliente: {resultado[6]} |\n>>> CPF Cliente: {resultado[7]} |\n>>> ID Imovel: {resultado[8]} |\n>>> Imovel: {resultado[9]}")
                            print("\n=============FIM DA PAGINA=================")
                            time.sleep(0.5)
                            print("\nVocê está na pagina: {} de {}".format(noPagina, TotalPaginasPg))
                            listandoTodosPg()

                        except ValueError:
                            print("Comando inválido")
                            noPagina = 1
                            listandoTodosPg()
            listandoTodosPg()
            
        elif pgCmd.lower() == "b":
            print("Listando Pagamentos Aprovados💵✅")
            time.sleep(2)
            cursor.execute("SELECT * FROM tbl_pagamentos WHERE status_pagamento = True;") #Contar quantas linhas de registro tem
            rows = cursor.fetchall()

            pgPagamentos = 1
            TotalPaginasPg = math.ceil(len(rows)/5) #Dividir 5 registros por pagina +1 pq não começamos na página 0



            cursor.execute("SELECT tbl_pagamentos.id_pagamento, tbl_pagamentos.valor_pagamento, tbl_pagamentos.data_pagamento, tbl_pagamentos.status_pagamento, tbl_pagamentos.formato_pagamento, tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_cliente.cpf_cliente, tbl_imovel.id_imovel, tbl_imovel.descricao_imovel FROM tbl_pagamentos INNER JOIN tbl_cliente INNER JOIN tbl_imovel ON fk_TBL_imovel_id_cliente = id_cliente WHERE status_pagamento = True LIMIT 5;")
            data = cursor.fetchall()
            for resultado in data:
                print(f"\n>>> ID: {resultado[0]} |\n>>> Valor Pagamento: {resultado[1]} |\n>>> Data Pagamento: {resultado[2]} |\n>>> Status Pagamento: {resultado[3]}✅|\n>>> Forma De Pagamento: {resultado[4]} |\n>>> ID Cliente: {resultado[5]} |\n>>> Nome Cliente: {resultado[6]} |\n>>> CPF Cliente: {resultado[7]} |\n>>> ID Imovel: {resultado[8]} |\n>>> Imovel: {resultado[9]}")
                print("Pagina: |{}| de |{}|\n".format(pgPagamentos,TotalPaginasPg))
                print("Você está na pagina: {} de {}\n".format(pgPagamentos,TotalPaginasPg))
            
            def listandoPgPagos():
                pgPagamentos = True
                while pgPagamentos:
                    noPagina = 0
                    pgPagamentos = input("Digite o número da página\nPara sair Digite: S\n>>>")

                    if pgPagamentos.lower() == "s":
                        print("Saindo...")
                        time.sleep(1)
                        pagamentos()
                    else:
                        try:
                            int_noPagina = int(pgPagamentos)
                            if type(int_noPagina) == int:
                                pgPagamentos = int_noPagina
                                if pgPagamentos == int(0):
                                    pgPagamentos = 1
                                if pgPagamentos > TotalPaginasPg:
                                    print("Numero total de páginas é: {}".format(TotalPaginasPg))
                                    listandoPgPagos()
                            else:
                                print("Erro! Digite apenas numeros inteiros para a pagina")
                                listandoPgPagos()
                            
                            noPagina = pgPagamentos
                            pgPagamentos = (pgPagamentos*5)-5
                            cursor.execute("SELECT tbl_pagamentos.id_pagamento, tbl_pagamentos.valor_pagamento, tbl_pagamentos.data_pagamento, tbl_pagamentos.status_pagamento, tbl_pagamentos.formato_pagamento, tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_cliente.cpf_cliente, tbl_imovel.id_imovel, tbl_imovel.descricao_imovel FROM tbl_pagamentos INNER JOIN tbl_cliente INNER JOIN tbl_imovel ON fk_TBL_imovel_id_cliente = id_cliente WHERE status_pagamento = True LIMIT 5 OFFSET %s;",(pgPagamentos,))
                            resultados = cursor.fetchall()
                            for resultado in resultados:
                                print(f"\n>>> ID: {resultado[0]} |\n>>> Valor Pagamento: {resultado[1]} |\n>>> Data Pagamento: {resultado[2]} |\n>>> Status Pagamento: {resultado[3]} |Pago✅\n>>> Forma De Pagamento: {resultado[4]} |\n>>> ID Cliente: {resultado[5]} |\n>>> Nome Cliente: {resultado[6]} |\n>>> CPF Cliente: {resultado[7]} |\n>>> ID Imovel: {resultado[8]} |\n>>> Imovel: {resultado[9]}")
                            print("\n=============FIM DA PAGINA=================")
                            time.sleep(0.5)
                            print("\nVocê está na pagina: {} de {}".format(noPagina, TotalPaginasPg))
                            listandoPgPagos()

                        except ValueError:
                            print("Comando inválido❌")
                            noPagina = 1
                            listandoPgPagos()
                pgPagamentos = False
            listandoPgPagos()


        elif pgCmd.lower() == "c":
            print("Listando pagamentos pendentes⏳")
            time.sleep(2)
            cursor.execute("SELECT * FROM tbl_pagamentos WHERE status_pagamento = False;") #Contar quantas linhas de registro tem
            rows = cursor.fetchall()

            pgPagamentos = 1
            TotalPaginasPg = math.ceil(len(rows)/5) #Dividir 5 registros por pagina +1 pq não começamos na página 0



            cursor.execute("SELECT tbl_pagamentos.id_pagamento, tbl_pagamentos.valor_pagamento, tbl_pagamentos.data_pagamento, tbl_pagamentos.status_pagamento, tbl_pagamentos.formato_pagamento, tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_cliente.cpf_cliente, tbl_imovel.id_imovel, tbl_imovel.descricao_imovel FROM tbl_pagamentos INNER JOIN tbl_cliente INNER JOIN tbl_imovel ON fk_TBL_imovel_id_cliente = id_cliente WHERE status_pagamento = False LIMIT 5;")
            data = cursor.fetchall()
            for resultado in data:
                print(f"\n>>> ID: {resultado[0]} |\n>>> Valor Pagamento: {resultado[1]} |\n>>> Data Pagamento: {resultado[2]} |\n>>> Status Pagamento: {resultado[3]}❌⏳|\n>>> Forma De Pagamento: {resultado[4]} |\n>>> ID Cliente: {resultado[5]} |\n>>> Nome Cliente: {resultado[6]} |\n>>> CPF Cliente: {resultado[7]} |\n>>> ID Imovel: {resultado[8]} |\n>>> Imovel: {resultado[9]}")
                print("Pagina: |{}| de |{}|\n".format(pgPagamentos,TotalPaginasPg))
                print("Você está na pagina: {} de {}\n".format(pgPagamentos,TotalPaginasPg))
            
            def listandoPgPendente():
                pgPagamentos = True
                while pgPagamentos:
                    noPagina = 0
                    pgPagamentos = input("Digite o número da página\nPara sair Digite: S\n>>>")

                    if pgPagamentos.lower() == "s":
                        print("Saindo...")
                        time.sleep(1)
                        pagamentos()
                    else:
                        try:
                            int_noPagina = int(pgPagamentos)
                            if type(int_noPagina) == int:
                                pgPagamentos = int_noPagina
                                if pgPagamentos == int(0):
                                    pgPagamentos = 1
                                if pgPagamentos > TotalPaginasPg:
                                    print("Numero total de páginas é: {}".format(TotalPaginasPg))
                                    listandoPgPendente()
                            else:
                                print("Erro! Digite apenas numeros inteiros para a pagina")
                                listandoPgPendente()
                            
                            noPagina = pgPagamentos
                            pgPagamentos = (pgPagamentos*5)-5
                            cursor.execute("SELECT tbl_pagamentos.id_pagamento, tbl_pagamentos.valor_pagamento, tbl_pagamentos.data_pagamento, tbl_pagamentos.status_pagamento, tbl_pagamentos.formato_pagamento, tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_cliente.cpf_cliente, tbl_imovel.id_imovel, tbl_imovel.descricao_imovel FROM tbl_pagamentos INNER JOIN tbl_cliente INNER JOIN tbl_imovel ON fk_TBL_imovel_id_cliente = id_cliente WHERE status_pagamento = False LIMIT 5 OFFSET %s;",(pgPagamentos,))
                            resultados = cursor.fetchall()
                            for resultado in resultados:
                                print(f"\n>>> ID: {resultado[0]} |\n>>> Valor Pagamento: {resultado[1]} |\n>>> Data Pagamento: {resultado[2]} |\n>>> Status Pagamento: {resultado[3]} |Pendente⏳\n>>> Forma De Pagamento: {resultado[4]} |\n>>> ID Cliente: {resultado[5]} |\n>>> Nome Cliente: {resultado[6]} |\n>>> CPF Cliente: {resultado[7]} |\n>>> ID Imovel: {resultado[8]} |\n>>> Imovel: {resultado[9]}")
                            print("\n=============FIM DA PAGINA=================")
                            time.sleep(0.5)
                            print("\nVocê está na pagina: {} de {}".format(noPagina, TotalPaginasPg))
                            listandoPgPendente()

                        except ValueError:
                            print("Comando inválido❌")
                            noPagina = 1
                            listandoPgPendente()
                pgPagamentos = False
            listandoPgPendente()

        else:
            print("Comando inválido❌")
            time.sleep(1)
            listarPagamentos()

    except ValueError:
        print("Comando Inválido❌")
        time.sleep(1)
        pagamentos()

def pagamentos():
    print("=========💵Pagamentos💵=========")
    print("Comandos Disponíveis:\n|A| Adicionar um pagamento💵✅\n|L| Listar pagamentos📃\n|R| Remover registro de pagamento❌💣\n")
    print("|S| Sair⬅️\n")
    comando = str(input(">>>"))

    if comando.lower() == str("s"):
        print("Saindo...⬅️")
        time.sleep(1)
        main()
    elif comando.lower() == str("a"):
        print("Adicionar Pagamento✅")
        time.sleep(1)
        adicionarPagamentos()
    elif comando.lower() == str("l"):
        print("Listar pagamentos📃")
        time.sleep(1)
        listarPagamentos()
    elif comando.lower() == str("r"):
        print("Remover registro de pagamento💣💵")
        time.sleep(1)
        removerPagamento()