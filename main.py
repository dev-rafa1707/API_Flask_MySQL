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





app.run()