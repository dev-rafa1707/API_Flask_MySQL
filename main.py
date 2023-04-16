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





# Create
@app.route('/cars', methods=['POST'])
def create_car():
    car = request.json
    Cars.append(car)
    return make_response(
        jsonify(message='Successful registration',
                data=car
        )
    ) 

 
# @app.route('/cars', methods=['POST'])
# def createCar():





#Update
@app.route('/cars/<int:id>', methods=['PUT'])
def update_car(id):
    new_car = request.json
    for car in Cars:
        print(car['id'])
        if car['id'] == id:
            # car = new_car
            car['id'] = new_car['id']
            car['brand'] = new_car['brand']
            car['model'] = new_car['model']
            car['year'] = new_car['year']
            return make_response(
                jsonify(message='Successful updated',
                        data=car   
                )
            )
        

#Delete
@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    for car in Cars:
        if car['id']== id:
            # del(car)
            del car['id']
            del car['brand']
            del car['model']
            del car['year']
            return  make_response(
                jsonify(message='OK',
                data=''
                )
            )





app.run()