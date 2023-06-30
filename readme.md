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
(Link) [https://pypi.org/project/Flask-MySQLdb/]


8. Copy .env.example to .env and input the variables as usend in you database
(Copiar o arquivo .env.example para .env e inserir as variáveis conforme o seu banco de dados)
<p>DB_HOST=</p>
<p>DB_USER=</p>
<p>DB_PASSWORD=</p>
<p>DB_NAME=</p>


9. Create the table "cars" in MySQL
(Criar a tabela "cars" no MySQL)

create table cars (  
	idCar int auto_increment,  
    brand varchar(45) not null,  
    model varchar(45) not null,
    yearModel int not null,
    constraint pk_idCar primary key (idCar)  
);


10. Use main.py to run the server
Server will listen on localhost PORT 5000
http://127.0.0.1:5000/



### Main commands / Principais comandos

* Cursor
cur = mysql.connection.cursor()

* comando = "SQLquery"
cur.execute(comando)

* Update in database / Editar o banco de dados
mysql.connection.commit()

* Read from database / Ler o banco de dados
myCars = cur.fetchall()



### How to test the application / Como testar a aplicação
We are using request.rest the VS Code extension but you can use Postman ou any other tool to make the requests. 



### Endpoints
// Get All Cars
GET http://localhost:5000/cars
 
###

// Get Car by Id
GET http://localhost:5000/cars/2


###
// Create Car
POST http://localhost:5000/cars
Content-Type: application/json

  {
    "band":"KIA",
    "model":"Sportage",
    "yearProd":2010
  }

###

// Update car
PUT http://localhost:5000/cars/1
Content-Type: application/json

  {
    "idCar":1,
    "band":"Jeep",
    "model":"Compass",
    "yearProd":2020
  }

###
// Delete car
DELETE http://localhost:5000/cars/2




### Flask tools
* make_response,

* jsonify

* request

* flask_mysqldb (MySQL)





### Author
Any question or issue, please contact me
dev-rafa1707
<rafa1707@gmail.com>



### License
No License required. 