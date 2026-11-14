import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

"""
   通过LangChain框架 来问千问模型问题-样例代码1- 将配置放到.env配置文件中
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

# 构造角色化对话消息
messages = [
    SystemMessage(content="你是一个情感专家"),
    HumanMessage(content="异性之间如何才能相处的融洽")
]

# 调用并输出结果
response = model.invoke(messages)
print(response.content)