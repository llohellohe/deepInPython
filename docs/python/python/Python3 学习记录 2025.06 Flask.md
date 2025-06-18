文档：https://tutorial.helloflask.com/template/


@app.route('/') 可以配置多个路由

# template
```

- `{{ ... }}` 用来标记变量。
- `{% ... %}` 用来标记语句，比如 if 语句，for 语句等。
- `{# ... #}` 用来写注释。


```


渲染模板：

return render_template('index.html', name=name, movies=movies)

其中 name 和movies 变量是传给模板的变量


# 静态资源
使用url_for参数
```
<head> ... <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" type="text/css"> </head>
```


# 错误码处理
```
@app.errorhandler(404) # 传入要处理的错误代码 
def page_not_found(e): # 接受异常对象作为参数 
	user = User.query.first() 
	return render_template('404.html', user=user), 404 # 返回模板和状态码
```