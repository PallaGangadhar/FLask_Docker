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
    print("dfjhdsjfhdsjhfj")
    print("dfjhdsjfhdsjhfjfgf")
    print("dfjhdsjfhdsjhfjfg")
    print("dfjhdsjfhdsjhfjdfgfd")
    print("dfjhdsjfhdsjhfj ffdgfd")
    print("dfjhdsjfhddvfdgf gfgfsjhfj ffdgfd")
    return "Hello GANGDADHAR Palla"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")

