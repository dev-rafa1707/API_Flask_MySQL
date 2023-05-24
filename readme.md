# API Python Flask using MySQL database
API Rest Backend server using Python Flask and MySQL database


### Status:
Finished


### Features
CRUD

* CREATE new record database
(Criar novo registro de veículo)

* READ ALL  the records in database
(Consultar todos os veículos cadastrados)

* READ by id
(Consulta veículo por codigo)

* UPDATE by id  Update a record in database using the id
(Edita veículo cadastrado)

* DELETE a record in database using the id
(Exclui veículo cadastrado)


### Requirements / Pré-requisitos
* Python already installed

* MySQL already installed


### How to run the application / Como rodar a aplicação

1. Download this project from
(Fazer o download do projeto a partir de)

(Link)[https://github.com/dev-rafa1707/API_Flask_MySQL.git]

2. Move the terminal to the project folder directory

3. Run the script below to create the virtual environment
python -m venv venv

4. Run the script below to activate the virutal environment
venv/Scripts/activate.bat (windows)

5. Run the script below to install Flask
pip install flask

6. Run the script below to install dotenv
pip install python-dotenv

7. Run the script below to Install Flask-MySQLdb
pip install flask-mysqldb


8. Copy .env.example to .env and input the variables as usend in you database
(Copiar o arquivo .env.example para .env e inserir as variáveis conforme o seu banco de dados)
<p>DB_HOST=</p>
<p>DB_USER=</p>
<p>DB_PASSWORD=</p>
<p>DB_NAME=</p>

* Create the table "cars" in MySQL
(Criar a tabela "cars" no MySQL)

create table cars (  
	idCar int auto_increment,  
    brand varchar(45) not null,  
    model varchar(45) not null,
    yearModel int not null,
    constraint pk_idCar primary key (idCar)  
);








From Flask
make_response,

jsonify

request
from flask_mysqldb import MySQL

// ajustes readme