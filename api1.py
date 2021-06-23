from flask import Flask, jsonify, request
import requests, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def gather():
    data = request.get_json()
    name = data['name']
    age = data['age']
    ra_no = data['random_number']
    output = int(age) + int(ra_no)
    return(jsonify({"output": output}))

if __name__ == '__main__':
    app.run(port=5000,debug=True)