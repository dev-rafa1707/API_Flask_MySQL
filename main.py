from flask import Flask, make_response, jsonify, request
from bd import Cars


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#GetAll
@app.route('/cars', methods=['GET'])
def get_cars():
    return make_response(
        jsonify(message='Cars List',
                data=Cars)
    )



#Get by id
@app.route('/cars/<int:id>', methods=['GET'])
def get_car(id):
    for car in Cars:
        if car['id'] == id:
            return make_response(
                jsonify(message='Car',
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

 






app.run()