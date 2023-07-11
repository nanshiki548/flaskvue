from flask import Flask, render_template, url_for, request

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Form Sample", message="お名前は？")


@app.route('/', methods=['POST'])
def form():
    ck = request.form.get('check')
    rd = request.form.get('radio')
    sel = request.form.getlist('sel')
    return render_template('insex.html', title="Form sample", message=[ck, rd, sel])