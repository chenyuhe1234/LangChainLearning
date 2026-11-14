import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

"""
   通过LangChain api 配置文件 访问大模型
"""
# 加载项目根目录下的 .env 文件到环境变量（不覆盖已存在的系统变量）
load_dotenv()
# 初始化通义千问模型
model = ChatOpenAI(
    model="qwen-max",  # 可替换为 qwen-turbo, qwen-max 等
    openai_api_key=os.environ.get("DASHSCOPE_API_KEY"),
    openai_api_base=os.environ.get("DASHSCOPE_BASE_URL"),
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
