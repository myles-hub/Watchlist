# 第4章：静态文件

## 4.1 静态文件（）

### 4.1.1 什么是静态文件（static files)

静态文件（static file）和我们的动态模板概念相反，指的是内容不需要动态生成的文件，比如图片、JavaScript脚本、CSS文件。

- images 图片
- JS 脚本
- CSS 文件



### 4.1.2 静态文件目录 `static`

在 Flask 框架中， 默认所有的静态文件都保存在static 静态文件夹中，所以我们需要在项目根目录下手动创建一个static目录。

```
$ mkdir static
```



## 4.2  静态文件URL

### 4.2.1 什么是静态文件URL

在 html 动态模板中，静态文件引入需要给出资源所在的**<u>URL地址</u>**。为了更加灵活的配置，这些静态文件URL可以通过Flask提供的 **<u>url_for() 函数</u>** 来生成。



### 4.2.2 url_for() 函数

**<u>url_for()函数</u>** 是 flask 框架中用来动态生成 `url`内置方法，其使用场景有一下 2种（python环境，html模块环境）。

- **（1）python 环境**：其使用需要我们手动从flask包中引入，才可以使用；

```python
from flask import url_for
```



- **（2）html 模块环境**：我们可以直接使用，因为 Flask 把一些常用的函数和对象添加到了模板上下文（环境）里。

假如我们在 static 文件夹的根目录下面放了一个 foo.jpg 文件，下面的调用可以获取它的 URL

```html
<img src="{{ url_for('static', filename='foo.jpg') }}">

# 端点值：'static'
# filename参数：静态文件相对路径
```



## 4.3  URL 生成实例

### 4.3.1 添加 Favicon



### 4.3.2 添加图片



### 4.3.3 添加 CSS