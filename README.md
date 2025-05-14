# Pharma Management System
Este projeto permite gerenciar seus imoveis, com interface em terminal e integração com banco de dados MySQL.

## Pré-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:
- Python 3.x
- SQL e MySQL Workbench

**Configuração do Ambiente**

## Criando e ativando ambiente virtual Python

Criar Ambiente/Enviroment

No Windows:
   python -m venv env

Ativar Ambiente/Enviroment

No Windows:
   env\Scripts\activate

No Linux/MacOS:
   source env/bin/activate

## Dependências

Esse comando vai instalar um arquivo com todas as dependências usadas:
    pip install -r requirements.txt

## Criando o Banco de Dados

Configuração do Banco de Dados

    Criar o banco de dados executando script db.sql no seu MySQL Workbench ou cliente MySQL preferido.

Inserindo dados no Banco de Dados
    execute o script insert_produtos.sql no seu MySQL Workbench ou cliente MySQL preferido.

    
Configurar as credenciais de acesso ao banco de dados no arquivo settings.py:

    DB_CONFIG = {
        'host': 'localhost',
        'user': 'seu_usuario',  # Alterar para seu usuário MySQL
        'password': 'sua_senha',  # Alterar para sua senha MySQL
        'database': 'nome_do_banco'  # Nome do banco criado
    }

## Executando a Aplicação

Após configurar o ambiente e o banco de dados, execute:
  python main.py


## Estrutura do Projeto

    pharmacy-app/
    │
    ├── backend.py                 # Funções de backend (ex: lógica do sistema, manipulação do banco)
    ├── interface.py               # Interface do usuário (ex: terminal, GUI ou integração futura)
    ├── main.py                    # Ponto de entrada da aplicação
    ├── settings.py                # Configurações, como conexão com banco de dados
    ├── requirements.txt           # Dependências da aplicação
    ├── README.md                  # Documentação do projeto
    │
    └── scripts/                   # Scripts SQL
       └── db.sql                  # Script para criação de tabelas
        