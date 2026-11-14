import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

"""
   Invoke的用法 - 入参是-字典列表
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

messages = [
    {"role":"system","content":"你是一个专业的数学老师"},
    {"role":"user","content":"帮我解释一下什么是斐波那契数列"}
]


# 调用并输出结果
response = model.invoke(messages)
print(response.content)
