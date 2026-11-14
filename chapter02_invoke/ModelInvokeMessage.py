import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

"""
   Invoke的用法 - 入参是-Message
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
    SystemMessage(content="你是一个专业的数学老师"),
    HumanMessage(content="帮我解释一下什么是斐波那契数列"),
]
# 第1次对话
response1 = model.invoke(messages)
print(f"AI的回复1: {response1.content}")

#添加记忆
messages.append(AIMessage(content=response1.content))
messages.append(HumanMessage(content="我刚才问了什么问题？"))

# 第2次对话
response2 = model.invoke(messages)
print(f"AI的回复2: {response2.content}")



