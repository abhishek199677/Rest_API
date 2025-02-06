from flask import Flask



app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])    
def hello_world():
    print("Hello World")
    return 'Welcome to API'


if __name__ == '__main__':
    app.run(debug=True)




#http://127.0.0.1:5000/hello   ------->  this is basically API for my particular function i.e hello_world