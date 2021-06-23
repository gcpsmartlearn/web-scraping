from flask import Flask, jsonify, request
#import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def bmi():
    data = request.get_json()
    height = data['height']
    weight = data['weight']
    bmi = weight/(height**2)
    return(jsonify({"Body mass Index" : bmi}))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)#int(os.environ.get('PORT', 8080)))


