from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Welcome Faker Server"})

@app.route('/add', methods=['POST']) 
def add():
    data = request.get_json()
    result = data['num1'] + data['num2']
    return jsonify({"result Of your Addition": result})

@app.route('/add3', methods=['POST'])  
def add3():
    data = request.get_json()
    result = data['num1'] + data['num2']+data['num3']
    return jsonify({"result Of your Addition": result})

@app.route('/sub', methods=['POST'])  
def sub():
    data = request.get_json()
    result = data['num1'] - data['num2'] -data['num3']
    return jsonify({"result Of your Subtraction": result})

if __name__ == '__main__':
    app.run(debug=True)
