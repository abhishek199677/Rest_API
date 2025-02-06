from flask import Flask, request, Response, jsonify


app = Flask(__name__)

@app.route('/', methods=['POST', "GET"])
def home():
    return "welcome to Flask Home"

@app.route('/calculator', methods=['POST', "GET"])
def calculator():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    if operation == 'add':
        return str(num1 + num2)
    elif operation == 'subtract':
        return str(num1 - num2)
    elif operation == 'multiply':
        return str(num1 * num2)
    elif operation == 'divide':
        return str(num1 / num2)
    else:
        return jsonify({'error': 'Invalid operation'}), 400






if __name__ == '__main__':
    app.run(debug=True, port=5005)
