from flask import Flask, render_template

app = Flask(__name__)
'''
@app.route('/in')
def index():
    return '<h1>Hello World!Sangre</h1>'
'''


@app.route('/')
def index():
    return '<h1> Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, ' + name + '!</h1>'


# 주소 뒤에 /~~로 붙는 내용이 일종의 변수로 받아지는 것
# 뒤에만 조금씩 수정해서 새로운 페이지를 만들 수 있음
# 서버=컴퓨터
# 내가 포트, url을 열면 이 화면을 보여줄게

@app.route('/mine')
def mine():
    return render_template('mypage.html')


@app.route('/mine/<n>')
def mine2(n):
    return render_template('mypage2.html', name=n)
# '<>'안의 값을 변수화 시킨것

@app.route('/free_diving')
def dive():
    return render_template('freediving.html')


app.run(host='0.0.0.0', debug=True)
