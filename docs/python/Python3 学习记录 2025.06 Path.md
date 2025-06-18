
导入：from pathlib import Path

```
cwd = Path.cwd()  
print(cwd)  
  
home = Path.home()  
print(home)  
  
log_dir = home.joinpath('logs_test')  
print(log_dir)  
  
if not log_dir.exists():  
    log_dir.mkdir()  
else:  
    print(log_dir.exists())
```

* 获得当前工作目录 Path.cwd
* 获得当前的home目录 Path.home
* 判断目录是否存在 xx.exits()
* 创建目录 xx.mkdir()

递归创建不存在的目录，parents为True
```
new_dir=home.joinpath('x1/x2/new_logs')  
new_dir.mkdir(parents=True)
```

参考资料：
1. https://docs.python.org/zh-cn/3.12/library/pathlib.html
