from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def homepage():
    return "This is Homepage, edit url and add '/api' to get response"

@app.route("/api", methods=['GET'])
def api():
    with open('data.json','r') as file:
        data = json.load(file)
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)