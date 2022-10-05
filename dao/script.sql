CREATE DATABASE WarehouseInventory;

CREATE TABLE usuario(
	id bigint unsigned auto_increment PRIMARY KEY,
    usuario VARCHAR(65) NOT NULL,
    email VARCHAR(65) NOT NULL,
    passw VARCHAR(150) NOT NULL
);

CREATE TABLE producto(
	id bigint unsigned auto_increment primary KEY,
    descripcion varchar(150) NOT NULL,
    stock int not null
);