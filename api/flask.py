from flask import Flask

app = Flask(__name__)

@app.route('/api/flask')
def hello_world():
    return 'This is from Flask Serverless Function'

if __name__ == '__main__':
    app.run()