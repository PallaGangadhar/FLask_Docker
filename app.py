from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello DAMAN"

@app.route('/name', methods=['GET'])
def name():
    return "Hello GANGDADHAR PALLA"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")

