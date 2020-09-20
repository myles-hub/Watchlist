from flask import Flask

# 创建一个应用实例
app = Flask(__name__)

# 创建一个静态路由,将根目录访问映射到视图函数hello()
@app.route('/')
def hello():
    # return "Welcome to my watchlist."
    return """<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">"""

@app.route("/home")
def hi():
    return "欢迎来到我的 Wathclist."