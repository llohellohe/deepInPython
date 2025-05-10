---
tags:
  - mcp
  - 字符串
---
#字符串
# 注释：

"""  
This is a MCP Server for Claude Desktop  
It has 2 tools  
"""

#字符串 
# 格式化
使用如下两种方式

url = f"{NWS_API_BASE}/alerts/active/area/{USER_AGENT}"

#字符串 
prompt=f"""  
You are good at http protocol  
You can format url like :  
API:{NWS_API_BASE}  
USER_AGENT: {USER_AGENT}  
"""


# dict
定义
{
"key":"value",
}

遍历
for k,v in req.items():  
    print(f"key is {k},value is {v}")


转成list
keys=[k for k in req.keys()]

转成字符串
return "\n---\n".join(keys)

# __NAME__
![[Pasted image 20250409175410.png]]
```if __name__ == "__main__":  
    # 这里的代码只有在该脚本直接运行时才会执行  
    print("This script is run directly.")

