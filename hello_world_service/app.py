from flask import Flask, jsonify

app_hello = Flask(__name__)

@app_hello.route('/')
def hello():
    return 'Hello, World! This is the Hello microservice. This is the final version for CI/CD and GitOps!'

# endpoint for api communication
@app_hello.route('/api/hello', methods=['GET'])
def get_hello():
    return jsonify(message="Hello from the Hello microservice 2.0!")

if __name__ == '__main__':
    app_hello.run(debug=True, host='0.0.0.0', port=5000)
