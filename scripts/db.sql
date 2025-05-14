#Derrubar Banco caso necessario
drop database if exists bd_projeto;

create database if not EXISTS bd_projeto;
use bd_projeto;

/* Lógico_4: */
CREATE TABLE TBL_cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(50),
    email_cliente VARCHAR(50),
    telefone_cliente VARCHAR(50),
    senha_cliente VARCHAR(255),
    cpf_cliente VARCHAR(15),
    fk_tbl_pagamentos_id_pagamento INT
);

CREATE TABLE TBL_Pagamentos (
    id_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    valor_pagamento DECIMAL(10,2),
    data_pagamento DATE,
    vencimento_pagamento DATE,
    status_pagamento BOOLEAN,
    formato_pagamento VARCHAR(20),
    fk_TBL_cliente_id_cliente INT
);

CREATE TABLE TBL_imovel (
    id_imovel INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    descricao_imovel VARCHAR(255),
    estado_imovel VARCHAR(100),
    cidade_imovel VARCHAR(100),
    bairro_imovel VARCHAR(100),
    rua_imovel VARCHAR(100),
    numero_imovel VARCHAR(100),
    cep_imovel VARCHAR(100),
    diaria_imovel FLOAT(10,2),
    comodos_imovel INT,
    fk_TBL_imovel_id_cliente INT
);
CREATE TABLE TBL_adm (
    id_adm INT PRIMARY KEY AUTO_INCREMENT,
    nome_adm VARCHAR(50),
    email_adm VARCHAR(50),
    senha_adm VARCHAR(255),
    super_adm bool
);
 
 ALTER TABLE TBL_Pagamentos ADD CONSTRAINT FK_TBL_Pagamentos
    FOREIGN KEY (fk_TBL_cliente_id_cliente)
    REFERENCES TBL_cliente (id_cliente)
    ON DELETE RESTRICT;
 
 ALTER TABLE TBL_imovel ADD CONSTRAINT FK_TBL_imovel
    FOREIGN KEY (fk_TBL_imovel_id_cliente)
    REFERENCES TBL_cliente (id_cliente)
    ON DELETE SET NULL;