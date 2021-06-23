from flask import Flask, jsonify, request
import requests, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def gather():
    data = request.get_json()
    num = data['num']
    output2 = int(num)/2
    return(jsonify({"output":output2}))

if __name__ == '__main__':
    app.run(port=5001,debug=True)