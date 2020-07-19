# coding=gbk
from flask import Flask

app = Flask(__name__)


@app.route('/')  # 路由
def hello_world():
    return '1234546'


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1943,debug=True)
