from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
@app.route('/list_prof/<list>')
def list_prof(list):
    jobs_list = ['Капитан', 'Штурман', 'Врач', 'Солдат', 'Гей']
    
    return render_template('list_prof.html', list=list, jobs=jobs_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

# http://127.0.0.1:8080/list_prof/ol