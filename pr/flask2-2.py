from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
@app.route('/training/<prof>')
def training(prof):
    
    return render_template('train.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

# http://127.0.0.1:8080/training/врач