CREATE DATABASE gamesreview;

USE gamesreview;

CREATE TABLE desenvolvedora (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(150) NOT NULL,
    Pais_de_origem VARCHAR(45) NOT NULL,
    Especialidade VARCHAR(45) NOT NULL
);

CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(150) NOT NULL,
    Email VARCHAR(150) NOT NULL,
    Senha VARCHAR(150) NOT NULL
);

CREATE TABLE empresa_proprietaria (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(45) NOT NULL,
    Descricao VARCHAR(150) NOT NULL,
    Desenvolvedora_id INTEGER NOT NULL,
    FOREIGN KEY (Desenvolvedora_id) REFERENCES desenvolvedora(id)
);

CREATE TABLE jogo (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Titulo VARCHAR(150) NOT NULL,
    Descricao VARCHAR(200) NOT NULL,
    Genero VARCHAR(45) NOT NULL,
    Data_de_lancamento DATE NOT NULL,
    Empresa_Proprietaria_id INTEGER NOT NULL,
    FOREIGN KEY (Empresa_Proprietaria_id) REFERENCES empresa_proprietaria(id)
);

CREATE TABLE avaliacao (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Pontuacao FLOAT NOT NULL,
    Comentario VARCHAR(200) NOT NULL,
    jogo_id INTEGER,
    Usuario_id INTEGER,
    FOREIGN KEY (jogo_id) REFERENCES jogo(id),
    FOREIGN KEY (Usuario_id) REFERENCES usuario(id)
);