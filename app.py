from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

if __name__ == '__main__':
    # running on 0.0.0.0 allows access from external machines if needed
    # debug=True allows you to see errors in the browser
    app.run(host='0.0.0.0', port=5000, debug=True)
