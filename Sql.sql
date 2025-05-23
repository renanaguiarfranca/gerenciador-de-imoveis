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
    senha_adm VARCHAR(255)
);
 
 ALTER TABLE TBL_Pagamentos ADD CONSTRAINT FK_TBL_Pagamentos
    FOREIGN KEY (fk_TBL_cliente_id_cliente)
    REFERENCES TBL_cliente (id_cliente)
    ON DELETE RESTRICT;
 
 ALTER TABLE TBL_imovel ADD CONSTRAINT FK_TBL_imovel
    FOREIGN KEY (fk_TBL_imovel_id_cliente)
    REFERENCES TBL_cliente (id_cliente)
    ON DELETE SET NULL;
    
    INSERT INTO TBL_imovel (
    descricao_imovel, estado_imovel, cidade_imovel, bairro_imovel, 
    rua_imovel, numero_imovel, cep_imovel, diaria_imovel, comodos_imovel
) VALUES
-- Registro 1 (SP)
('Casa do Tal...O Taldo_Renan','São Paulo','Taboão da Serra','Jardim Salete','José Micheloni Filho','64-A','06787-380','499.99','5'),

-- Registro 2 (SP)
('Casa moderna com piscina e vista para o jardim', 'São Paulo', 'São Paulo', 'Morumbi', 'Avenida Giovanni Gronchi', '1500', '05651-000', 600.00, 5),

-- Registro 3 (RJ)
('Casa de praia com varanda e rede', 'Rio de Janeiro', 'Rio de Janeiro', 'Barra da Tijuca', 'Rua das Conchas', '23', '22631-200', 450.00, 3),

-- Registro 4 (MG)
('Sobrado clássico com quintal amplo', 'Minas Gerais', 'Belo Horizonte', 'Sion', 'Rua dos Inconfidentes', '45', '30310-420', 380.00, 4),

-- Registro 5 (RS)
('Casa rústica com lareira e acabamento em madeira', 'Rio Grande do Sul', 'Gramado', 'Centro', 'Rua das Hortênsias', '789', '95670-000', 550.00, 3),

-- Registro 6 (SC)
('Casa alpina com influência alemã', 'Santa Catarina', 'Blumenau', 'Vorstadt', 'Rua XV de Novembro', '1234', '89010-001', 420.00, 4),

-- Registro 7 (PR)
('Casa térrea com garagem coberta', 'Paraná', 'Curitiba', 'Batel', 'Avenida do Batel', '500', '80420-000', 490.00, 3),

-- Registro 8 (BA)
('Casa colonial com azulejos históricos', 'Bahia', 'Salvador', 'Pelourinho', 'Rua do Carmo', '15', '40026-010', 530.00, 4),

-- Registro 9 (PE)
('Casa colorida com varanda gourmet', 'Pernambuco', 'Recife', 'Boa Viagem', 'Avenida Conselheiro Aguiar', '2030', '51021-020', 480.00, 3),

-- Registro 10 (CE)
('Casa com pátio interno e ventilação natural', 'Ceará', 'Fortaleza', 'Meireles', 'Rua dos Pacajus', '78', '60160-160', 400.00, 3),

-- Registro 11 (DF)
('Casa contemporânea com painéis solares', 'Distrito Federal', 'Brasília', 'Asa Sul', 'Quadra 306', 'Bloco B', '70236-060', 580.00, 4),

-- Registro 12 (GO)
('Casa com piscina de borda infinita', 'Goiás', 'Goiânia', 'Setor Marista', 'Rua 9', '1023', '74150-090', 520.00, 5),

-- Registro 13 (AM)
('Casa palafita adaptada ao clima amazônico', 'Amazonas', 'Manaus', 'Parque 10', 'Rua Rio Juruá', '12', '69055-090', 350.00, 3),

-- Registro 14 (PA)
('Casa com estrutura elevada contra enchentes', 'Pará', 'Belém', 'Nazaré', 'Avenida Nazaré', '1001', '66035-170', 390.00, 3),

-- Registro 15 (RN)
('Casa branca com telhado vermelho típico', 'Rio Grande do Norte', 'Natal', 'Ponta Negra', 'Rua Praia de Genipabu', 'S/N', '59090-210', 470.00, 4),

-- Registro 16 (ES)
('Casa com vista para o mar e suíte master', 'Espírito Santo', 'Vitória', 'Praia do Canto', 'Rua da Praia', '77', '29055-290', 620.00, 4),

-- Registro 17 (MS)
('Casa de campo com varanda ampla', 'Mato Grosso do Sul', 'Bonito', 'Centro', 'Rua 21 de Abril', '321', '79290-000', 430.00, 3),

-- Registro 18 (MT)
('Casa com inspiração pantaneira e varanda', 'Mato Grosso', 'Cuiabá', 'Jardim Itália', 'Rua das Palmeiras', '55', '78060-800', 410.00, 4),

-- Registro 19 (PI)
('Casa térrea com paredes grossas para clima quente', 'Piauí', 'Teresina', 'Jóquei', 'Avenida Nossa Senhora de Fátima', '2233', '64049-550', 370.00, 3),

-- Registro 20 (SE)
('Casa com azulejos azuis e pátio fresco', 'Sergipe', 'Aracaju', 'Atalaia', 'Avenida Santos Dumont', '1500', '49037-470', 440.00, 3),

-- Registro 21 (RO)
('Casa de madeira rústica com varanda', 'Rondônia', 'Porto Velho', 'Nova Floresta', 'Rua das Castanheiras', '30', '76803-420', 360.00, 3);
    
   SELECT tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_imovel.descricao_imovel, tbl_pagamentos.id_pagamento, tbl_pagamentos.valor_pagamento, tbl_pagamentos.data_pagamento, tbl_pagamentos.status_pagamento 
   FROM tbl_imovel,tbl_pagamentos INNER JOIN tbl_cliente ON 
   fk_TBL_cliente_id_cliente = tbl_cliente.id_cliente = tbl_pagamentos.fk_TBL_cliente_id_cliente;
   
   INSERT INTO tbl_cliente (nome_cliente, email_cliente, telefone_cliente, senha_cliente, cpf_cliente) 
   VALUES ('Taldo_Renan','taldorenan@gmail.com',11984842999,'1234',12345678910);
   UPDATE TBL_imovel SET fk_TBL_imovel_id_cliente = 1 WHERE id_imovel = 1;
   SELECT * FROM TBL_cliente;

   SELECT tbl_cliente.id_cliente, tbl_cliente.nome_cliente, tbl_imovel.id_imovel, tbl_imovel.descricao_imovel
   FROM tbl_imovel INNER JOIN tbl_cliente ON fk_TBL_imovel_id_cliente = id_cliente;
   
   SELECT * FROM tbl_adm;
   SELECT * FROM tbl_imovel;
   SELECT * FROM tbl_cliente;
   SELECT * FROM tbl_pagamentos;
   INSERT INTO tbl_adm (nome_adm,email_adm,senha_adm)
   VALUES ('Taldo_Renan','taldorenan@gmail.com','123'),
          ('Maboni','mabonigames@bol.com','123');
          
SELECT email_adm, senha_adm FROM tbl_adm WHERE email_adm = 'taldorenan@gmail.com' and senha_adm = '123';
