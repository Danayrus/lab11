# A very simple Flask Hello World app for you to get started with...

import math
from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    s = 'Доступные действия: <br>1. Сложение - /add/a/b <br>2. Вычитание - /sub/a/b <br>3. Умножение - /mult/a/b <br>4. Деление -/div/a/b <br>5. Возведение в степень - /pow/a/b '
    ss='<br>6. Квадратный корень - /sqrt/a <br>7. Синус - /sin/a 8. Косинус - /cos/a <br>9. Тангенс - /tan/a'
    return s+ss

@app.route('/add/<a>/<b>')                         #Сложение
def add(a,b):
    return str(float(a)+ float(b))

@app.route('/sub/<a>/<b>')                         #Вычитание
def sub(a,b):
    return str(float(a)- float(b))

@app.route('/mult/<a>/<b>')                         #Умножение
def mult(a,b):
    return str(float(a)* float(b))

@app.route('/div/<a>/<b>')                         #Деление
def div(a,b):
    a=float(a)
    b=float(b)
    if (b==0):
        return 'error'
    else:
        return str(a/b)

@app.route('/pow/<a>/<b>')                         #Степень
def pow(a,b):
    return str((float(a)**float(b)))

@app.route('/sqrt/<a>')                         #Корень
def sqrt(a):
    a = float(a)
    if (a<0):
        return 'error'
    else:
        return str(math.sqrt(float(a)))

@app.route('/sin/<a>')                         #Синус
def sin(a):
    return str(math.sin(float(a)))

@app.route('/cos/<a>')                         #Косинус
def cos(a):
    return str(math.cos(float(a)))

@app.route('/tan/<a>')                         #Тангенс
def tan(a):
    return str(math.tan(float(a)))
