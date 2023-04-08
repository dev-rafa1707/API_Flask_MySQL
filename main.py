from flask import Flask, make_response, jsonify, request
from bd import Cars


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/cars', methods=['GET'])
def get_cars():
    return make_response(
        jsonify(message='Cars List',
                data=Cars)
    )

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