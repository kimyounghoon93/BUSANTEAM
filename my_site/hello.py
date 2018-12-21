import os
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

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    token = os.getenv('TELEGRAM_BOT_TOKEN') #=> os.getenv를 통해 저장해놨던 값이 나옴
    chat_id = os.getenv('CHAT_ID')          #=> 해서 미리 저장해놓고 암호화 하고난 뒤 os.getenv()를 넣어야함
    # 하고싶은 것들

    text = request.args['message']
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')