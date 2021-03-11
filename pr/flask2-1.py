from flask import Flask, render_template
from flask import url_for



@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница', 
                           username=user)