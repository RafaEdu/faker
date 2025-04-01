CREATE TABLE estado (
    idestado INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sigla VARCHAR(10) NOT NULL
);

CREATE TABLE cidade (
    idcidade INT PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    estado_idestado INT NOT NULL,
    CONSTRAINT fk_estado FOREIGN KEY (estado_idestado) REFERENCES estado(idestado)
);

CREATE TABLE fabricante (
    idfabricante INT PRIMARY KEY,
    nome VARCHAR(200) NOT NULL
);

CREATE TABLE modelo (
    idmodelo INT PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL,
    fabricante_idfabricante INT NOT NULL,
    CONSTRAINT fk_fabricante FOREIGN KEY (fabricante_idfabricante) REFERENCES fabricante(idfabricante)
);

CREATE TABLE veiculos (
    idveiculos INT PRIMARY KEY,
    placa VARCHAR(45) NOT NULL UNIQUE,
    modelo_idmodelo INT NOT NULL,
    cidade_idcidade INT NOT NULL,
    tipo_veiculo_idtipo_veiculo INT NOT NULL,
    CONSTRAINT fk_modelo FOREIGN KEY (modelo_idmodelo) REFERENCES modelo(idmodelo),
    CONSTRAINT fk_cidade FOREIGN KEY (cidade_idcidade) REFERENCES cidade(idcidade),
    CONSTRAINT fk_tipo_veiculo FOREIGN KEY (tipo_veiculo_idtipo_veiculo) REFERENCES tipo_veiculo(idtipo_veiculo),
);

CREATE TABLE tipo_veiculo (
    idtipo_veiculo INT PRIMARY KEY,
    descricao VARCHAR(150) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
);

CREATE TABLE praca (
    idpraca INT PRIMARY KEY,
    descricao VARCHAR(200) NOT NULL,
    cidade_idcidade INT NOT NULL,
    CONSTRAINT fk_cidade_praca FOREIGN KEY (cidade_idcidade) REFERENCES cidade(idcidade)
);

CREATE TABLE ticket (
    idticket INT PRIMARY KEY,
    data_hora TIMESTAMP NOT NULL,
    praca_idpraca INT NOT NULL,
    veiculos_idveiculos INT NOT NULL,
    CONSTRAINT fk_veiculos FOREIGN KEY (veiculos_idveiculos) REFERENCES veiculos(idveiculos),
    CONSTRAINT fk_praca FOREIGN KEY (praca_idpraca) REFERENCES praca(idpraca)
);