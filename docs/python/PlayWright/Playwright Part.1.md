# 获取内容
https://playwright.dev/python/docs/locators
## 根据名字获得 get_by_label

page.get_by_label("User Name").fill("John")  

page.get_by_label("Password").fill("secret-password")  

## 根据类型获得 get_by_role
page.get_by_role("button", name="Sign in").click()

获得button类型，名字为'Sign in'的。

# CSS or XPath
```
page.locator("css=button").click()  
page.locator("xpath=//button").click()  
  
page.locator("button").click()  
page.locator("//button").click()
```


```
page.fill('//input[@id="kw"]', '周杰伦')  
page.click('//input[@id="su"]')
```

## filter
![[Pasted image 20250514203144.png]]