import random
import requests
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args['name']
    # random
    # choice.( -- ) = ['신중함', '경건함', '장난기', '재미', '노잼']

    saa = random.sample(['잘남', '신중함', '경건함', '장난기', '재미', '노잼', '멍청함'],3)
    result = random.choice(['03_main.jpg', '03_main.jpg', '03_main.jpg'])
    return render_template('pong.html', name_in_html=name, result=result, saa=saa)

@app.route('/lotto/<int:num>')
def lotto(num):
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    response = requests.get(url)
    lotto = response.json()
    
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])

    bonus = lotto['bnusNo']

    return render_template('lotto.html', w=winner, b=bonus, n=num)
