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
    resposta = cur.fetchall()
    return make_response(
        jsonify(message='List',
                data=resposta)
    )


#READ ALL
# def getAll():
#     comando = f'SELECT * FROM vendas'
#     cursor.execute(comando)
#     resultado = cursor.fetchall()
#     return resultado


# @app.route("/")
# def users():
#     cur = mysql.connection.cursor()
#     cur.execute("""SELECT user, host FROM mysql.user""")
#     rv = cur.fetchall()
#     return str(rv)



#Get by id
# @app.route('/cars/<int:id>', methods=['GET'])
# def get_car(id):
#     for car in Cars:
#         if car['id'] == id:
#             return make_response(
#                 jsonify(message='Car',
#                         data=car)
#             )

#Get by id
@app.route('/cars/<int:idCar>', methods=['GET'])
def getById(idCar):
    cur = mysql.connection.cursor()
    comando = f'SELECT * FROM cars WHERE idCar = {idCar}'
    cur.execute(comando)
    resposta = cur.fetchall()
    return make_response(
        jsonify(message="Car by Id",
                data=resposta)
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