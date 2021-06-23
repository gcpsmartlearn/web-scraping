from flask import Flask, jsonify, request
import requests, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def gather():
    data = request.get_json()
    name = data['name']
    age = data['age']
    ra_no = data['random_number']
    url = "http://0.0.0.0:"
    port1 = 5000
    port2 = 5001
    payload = json.dumps({
        "name": str(name),
        "age": int(age),
        "random_number": int(ra_no)
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url+str(port1)+"/", headers=headers, data=payload)
    next_input = json.loads(response.text)
    num = next_input['output']
    payload2 = json.dumps({
        "num": int(num)
    })
    response2 = requests.request("POST", url+str(port2)+"/", headers=headers, data=payload2)
    f_output = json.loads(response2.text)
    return(jsonify({"final_output":f_output['output']}))

if __name__ == '__main__':
    app.run(port=5003,debug= True)

