import io
import os
import json
from flask import Flask, render_template, request, send_file
from flask.helpers import make_response
from jtalk import convert_to_wav

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def say():
    if request.method == 'GET':
        return render_template('index.html')
    data = request.data.decode('utf-8')
    jdata = json.loads(data)
    read = jdata.get('text')
    if read == '':
        return ('', 400)
    out = convert_to_wav(read)
    if out is None:
        return ('', 400)
    response = make_response(out)
    response.headers.set('Content-Type', 'audio/wav')
    return response


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
