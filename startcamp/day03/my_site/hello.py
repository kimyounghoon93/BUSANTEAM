from flask import Flask, render_template
import random
# from bs4 import BeautifulSoup
# BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ssafy")
def ssafy():
    return "This is SSAFY"

@app.route("/greeting/<string:name>")
def greeting(name): #변수 이름을 가져와야함
    return f'반갑습니다! {name}님'

@app.route("/cube/<int:num>")
def cube(num): #변수 이름을 가져와야함
    cube = num ** 3 # == num * num * num
    return f'{num}의 세제곱은 {cube}입니다.'

@app.route("/lunch/<int:person>")
def lunch(person):
    menu = ['짜장면','군만두','탕수육','팔보채','짬뽕','중화비빔밥','중화볶음밥','칠리새우']
    order = random.sample(menu, person)

    return str(order)

@app.route("/html")
def html():
    multiline_string = '''
        <h1>이것은 h1입니다!</h1>
        <p>여기는 p입니다.</p>
        123
    '''
    return multiline_string

@app.route("/html_file")
def html_file():
    return render_template('html_file.html')

@app.route("/hi/<string:name>")
def hi(name):
    return render_template('hi.html', name_in_html=name)


@app.route("/fake_naver")
def fake_naver():
    return render_template('fake_naver.html')