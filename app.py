# 导入模块
from flask import Flask

# 创建应用程序实例
app = Flask(__name__)

# 创建静态路由映射
# @app.route('/')
# def hello():
#     return "Welcome to Myles's Watchlist."

# 修改返回值1
@app.route('/')
def hello():
    return "欢迎来到 Myles 的 Watchlist."

# # 修改返回值2
# @app.route('/')
# def hello():
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

#
# # 修改URL规则1
# @app.route('/home')
# def hello():
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# 一个视图函数对应多个 url 规则
@app.route('/')
@app.route('/home')
@app.route('/hello')
def hello():
    return "欢迎来到 Myles 的 Watchlist."