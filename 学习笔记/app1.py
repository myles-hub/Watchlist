from flask import Flask, url_for, escape

# 创建一个应用实例
app = Flask(__name__)


# 1. 静态路由
# 创建一个静态路由,将根目录访问映射到视图函数hello()
@app.route('/home')
def hello():
    # return "Welcome to my watchlist."
    return """<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">"""

# @app.route("/home")
@app.route("/index")
def hi():
    return "欢迎来到我的 Wathclist Home Page."

# 2. 动态路由

@app.route('/user/<name>')
def user_page(name):
    return "User Page >>> <br> <br> Welcom {} to my watchlist".format(escape(name))


# 3. url_for


@app.route('/test')
def test_url_for():
    return "url_for(user_page) >>> {}".format(url_for('user_page', name='myles'))