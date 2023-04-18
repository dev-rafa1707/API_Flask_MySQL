from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Required
app.config["MYSQL_HOST"] = os.environ.get('DB_HOST')
app.config["MYSQL_USER"] = os.environ.get('DB_USER')
app.config["MYSQL_PASSWORD"] = os.environ.get('DB_PASSWORD')
app.config["MYSQL_DB"] = os.environ.get('DB_NAME')


mysql = MySQL(app)



#GetAll
@app.route('/cars', methods=['GET'])
def getAll():
    cur = mysql.connection.cursor()
    comando = f'SELECT * FROM cars'
    cur.execute(comando)
    myCars = cur.fetchall()

    cars = list()
    for car in myCars:
        cars.append(
            {
                'idCar':car[0],
                'brand':car[1],
                'model':car[2],
                'yearProd':car[3]
            }
        )

    return make_response(
        jsonify(message='List',
                data=cars)
    )



#Get by id
@app.route('/cars/<int:idCar>', methods=['GET'])
def getById(idCar):
    cur = mysql.connection.cursor()
    comando = f'SELECT * FROM cars WHERE idCar = {idCar}'
    cur.execute(comando)
    myCar = cur.fetchall()

    car = [
        {
            'idCar':myCar[0][0],
            'brand':myCar[0][1],
            'model':myCar[0][2],
            'yearProd':myCar[0][3]
        }
    ]

    return make_response(
        jsonify(message="Car by Id",
                data=car)
    )



#Create
@app.route('/cars', methods=['POST'])
def createCar():
    car = request.json
    cur = mysql.connection.cursor()
    comando = f"""INSERT INTO cars (band, model, yearProd) VALUES ("{car['band']}","{car['model']}",{car['yearProd']})"""
    cur.execute(comando)
    mysql.connection.commit()

    return make_response(
        jsonify(message='Successful registration',
                data=car
        )
    ) 


#Update
@app.route('/cars/<int:idCar>', methods=['PUT'])
def updateCar(idCar):
    updatedCar = request.json
    cur = mysql.connection.cursor()
    comando = f"""UPDATE cars SET band = "{updatedCar['band']}", model = "{updatedCar['model']}", yearProd = {updatedCar['yearProd']} WHERE idCar = {idCar}"""
    cur.execute(comando)
    mysql.connection.commit()

    return make_response(
        jsonify(message='Successful update',
                data=updatedCar
        )
    )





#Delete
@app.route('/cars/<int:idCar>', methods=['DELETE'])
def deleteCar(idCar):
    cur = mysql.connection.cursor()
    comando = f"DELETE FROM cars WHERE idCar = {idCar}"
    cur.execute(comando)
    mysql.connection.commit()
    return  make_response(
                jsonify(message='Deleted Succesfull',
                data=''
                )
            )



app.run()