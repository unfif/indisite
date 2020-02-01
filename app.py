from flask import Flask, render_template, request
import requests as rq
import argparse as argp
import uvicorn

parser = argp.ArgumentParser()
parser.add_argument('-n', '--host', type=str, default='0.0.0.0')
parser.add_argument('-p', '--port', type=int, default=5000)
parser.add_argument('-l', '--log-level', type=str, default='info')
args = parser.parse_args()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = {'encode': 'UTC-8'}
    if request.method == 'POST':
        url = request.form['url']
        res = rq.get(url)
        res.encoding = res.apparent_encoding 
        data['html'] = res.text
        data['encode'] = request.form['encode']
        print(url)

    return render_template('index.html', **data)

if __name__ == '__main__':
    uvicorn.run(app, host=args.host, port=args.port, log_level=args.log_level, interface='wsgi', lifespan='off')
