from flask import Flask, jsonify, request
import requests

app_happy = Flask(__name__)

@app_happy.route('/')
def happy():
    return 'Happy World! This is the Happy microservice. Check my fully dev-prod env. This final version is fetched from private repo. We love automation.'

# endpoint for fetching Hello World json
@app_happy.route('/api/hello', methods=['GET'])
def get_happy():
    # Communicate with the "Hello, World!" service using the api endpoint
    hello_response = requests.get('http://hello-world-service/api/hello')
    hello_message = hello_response.json().get('message', 'Error getting hello message')

    return jsonify(message=f"{hello_message} And Happy Final from the Happy microservice! Edition 4.0 Finale")

if __name__ == '__main__':
    app_happy.run(debug=True, host='0.0.0.0', port=5001)
