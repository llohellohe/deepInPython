import os
from http import HTTPStatus
from dashscope import Application

biz_params = {
    # 智能体应用的自定义插件输入参数传递，自定义的插件ID替换your_plugin_code
    "user_defined_params": {
        "Start_bYxoRU": {
            "city": "宁波"}}}
biz_params2 = {"city": "杭州"}

response = Application.call(
    # 若没有配置环境变量，可用百炼API Key将下行替换为：api_key="sk-xxx"。但不建议在生产环境中直接将API Key硬编码到代码中，以减少API Key泄露风险。
    api_key="",
    app_id='',# 替换为实际的应用 ID
    prompt="hello",
    biz_params=biz_params2)

if response.status_code != HTTPStatus.OK:
    print(f'request_id={response.request_id}')
    print(f'code={response.status_code}')
    print(f'message={response.message}')
    print(f'请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code')
else:
    print(response.output.text)