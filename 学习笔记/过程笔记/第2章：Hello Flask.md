# Hello Flask

## 2.1 最简单的主页

### 2.1.1 代码编写

创建一个app.py 文件，开始进行主页代码的编写。

```python
# 导入 Flask 类
from flask import Flask

# 创建应用实例
app = Flask(__name__)

# 添加路由映射（映射 URL 与 View Function）
@app.route('/')
def hello():
    return "Welcome to My WatchList."
```



### 2.1.2 程序运行

在项目目录下打开 `Git Bash`命令行，运行命令 `flask run `, flask 程序会通过环境变量自动去查找 `app.py`的程序文件，并运行它。

```cmd
$ flask run
 * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```



## 2.2 环境变量管理

### 2.2.1 2个环境变量

在启动 Flask 程序的时候，我们通常要和下面两个环境变量打交道：**<u>"FLASK_APP"</u>** 和 <u>**”FLASK_ENV“**</u>

- FLASK_APP 变量
  - FLASK_APP 变量主要与 **<u>"app.py"</u>** 相关联
- FLASK_ENV
  - **<u>“FLASK_ENV 变量”</u>** 主要与应用程序的 **<u>“debug mode”</u>** 相关联；
  - 关闭 “debug mode" ：FLASK_ENV = production （默认状态）；
  - 开启 “debug mode” ：FLAKS_ENV = development (需要手动配置)



### 2.2.2 python-dotenv

为了不用每次打开新的终端会话都要 **<u>“手动去设置环境变量”</u>**，我们可以安装 `python-dotenv` 这个工具来管理系统环境变量。

#### (1) python-dotenv 安装

```cmd
$ pip install python-dotenv
```



#### (2) 创建2个配置文件

当 python-dotenv 安装后，Flask 会从项目根目录的 .flaskenv 和 .env 文件读取环境变量并设置。因此我们可以直接手动创建2个环境文件，然后分别去配置你想要配置的环境变量值。

```cmd
$ mkdir .flaskenv .env
```



#### (3) 开启 app.py 调试模式

前面我们讲到了2个环境变量，其中变量“FLASK_ENV” 就是用来控制 “debug mode”的。

```cmd
# 编辑环境配置文件：.flaskenv，指定变量 FLASK_ENV的值 development 开启调试模式
$ vim .flaskenv
FLASK_ENV = development	# 开启调试模式
```



#### (4) .env 安全配置

由于 **<u>".env配置文件"</u>** 经常会存储敏感安全数据，因此我们不应将其同步到github远程仓库。

```cmd
# 编辑 Git 同步上传忽略规则文件 .gitignore, 添加被忽略文件名即可
# viem .gitignore

*.pyc
*~
__pychache__
.DS_Store
.env
~
# 最后保存退出。（:wq!）
```

