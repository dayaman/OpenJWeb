from flask import Flask, request
from jtalk import jtalk

app = Flask(__name__)

@app.route('/', methods=['POST'])
def say():
    read = request.body['text']
    rawbin = jtalk(read.encode())
    return {'voice':rawbin}

if __name__ == '__main__':
    app.run(debug=True)