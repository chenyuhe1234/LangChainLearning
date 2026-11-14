import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model

"""
   通过LangChain框架 来问千问模型问题-样例代码1
   使用 init_chat_model 统一初始化
   
   init_chat_model初始化模型有什么优势
   【以前】
   > 不同模型提供商的类名、参数名各不相同：
   # 以前：每个提供商有自己的类和参数
    ChatOpenAI(openai_api_key=..., openai_api_base=...)
    ChatDeepSeek(api_key=..., api_base=...)
    ChatAnthropic(anthropic_api_key=...)
    ChatTongyi(dashscope_api_key=...)
   【现在】
   # 现在：统一参数名
    init_chat_model("openai:gpt-4", api_key=..., base_url=...)
    init_chat_model("deepseek:deepseek-chat", api_key=..., base_url=...)
    init_chat_model("anthropic:claude-sonnet-4-20250514", api_key=...)
"""

# 读取 .env 配置文件
load_dotenv(override=True)

# 初始化通义千问模型
# init_chat_model 会自动从环境变量中读取 OPENAI_API_KEY 和 OPENAI_BASE_URL
# 但通义千问用的是 DASHSCOPE_API_KEY / DASHSCOPE_BASE_URL，需要显式传入
model = init_chat_model(
    "openai:qwen-max",  # 格式: provider:model_name
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
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