from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/hello')
def hello_world():
        message = "Hola Mundo, soy Python! Ahora con CloudBuild y hablando JSON"
        response = {
                "message": message,
                "length": len(message)
        }
        return jsonify(response)

@app.route('/bye')
def bye_workd():
        return ("Adios mundo cruel")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
