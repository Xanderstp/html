from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index/<title_web>')
def index(title_web):
    
    return render_template('index.html', title=title_web)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

# http://127.0.0.1:8080/index