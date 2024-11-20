from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello"

@app.route('/name', methods=['GET'])
def name():
    return "Hello GANGDADHAR PALLA How R u"

@app.route('/about', methods=['GET'])
def about():
    print("Hii fgdf")
    print("Hii fgdf")
    print("Hii fgdf dfdsfdfdf")
    print("Hii dfdsfd fgfdg")
    print("Hii hlloooo fgfdgfdgdfg")
    print(" sdfkdk  kfjgk dfkjfdk gkdf gkdfj kgjdfkgjdfk")
    print("Hii fgdf")
    print("Hii fgdf")
    print("Hii fgdf dfdsfdfdf")
    print("Hii fgfdg")
    print("Hii hlloooo sddfdsf fgfdgfdgdfg")
    print(" sdfkdk  kfjgk dfkjfdk gkdf gkdfj kgjdfkgjdfk")
    print("Hii fgdf")
    print("Hii fgdf")
    print("Hii fgdf dfdsfdfdf")
    print("Hii fgfdg")
    print("Hii hlloooo fgfdgfdgdfg")
    print(" sdfkdk  kfjgk dfkjfdk gkdf gkdfj kgjdfkgjdfk")
    return "Hello GANGDADHAR Palla"

@app.route('/login', methods=['GET'])
def login():
    print("Hii fgdf")
    print("Hii fgdf")
    print("Hii fgdf dfdsfdfdf")
    print("Hii fgfdg")
    print("Hii hlloooo fgfdgfdgdfg")
    print(" sdfkdk  kfjgk dfkjfdk gkdf gkdfj kgjdfkgjdfk")
    return "Hello GANGDADHAR Palla"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")

