import os
import json
from flask import Flask, request, send_file
from jtalk import jtalk

app = Flask(__name__)

@app.route('/', methods=['POST'])
def say():
    data = request.data.decode('utf-8')
    jdata = json.loads(data)
    read = jdata['text']
    fname = jtalk(read)
    fpath = './'+fname
    return send_file(
            fpath,
            mimetype='audio/wav',
            as_attachment=True,
            attachment_filename='{}'.format(fname))

@app.after_request
def after_request(responce):
    if responce.status_code == 200:
        os.remove(responce.headers['Content-Disposition'][21:])
    return responce


if __name__ == '__main__':
    app.run(debug=True)