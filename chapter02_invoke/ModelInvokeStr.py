import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from rich import print as rprint

"""
   Invoke的用法 - 入参是-字符串
"""

# 读取 .env 配置文件
load_dotenv(override=True)

# 初始化通义千问模型（配置从 .env 文件中读取）
model = ChatOpenAI(
    model=os.getenv("QWEN_MODEL", "qwen-max"),
    openai_api_key=os.getenv("DASHSCOPE_API_KEY"),
    openai_api_base=os.getenv("DASHSCOPE_BASE_URL"),
    temperature=0.7
)

# 调用并输出结果
response = model.invoke("你好嘛")
print(type(response))
rprint(response)
