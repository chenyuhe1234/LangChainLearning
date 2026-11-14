import os

from dotenv import load_dotenv
from openai import OpenAI
"""
  将配置文件.env的配置 加载到环境变量中
"""
# 加载项目根目录下的 .env 文件到环境变量（不覆盖已存在的系统变量）
load_dotenv()

print("DASHSCOPE_API_KEY =", os.getenv("DASHSCOPE_API_KEY"))
print("DASHSCOPE_BASE_URL =", os.getenv("DASHSCOPE_BASE_URL"))

client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url=os.environ["DASHSCOPE_BASE_URL"],
)
completion = client.chat.completions.create(
    model=os.getenv("QWEN_MODEL", "qwen-plus"),
    messages=[
        {"role": "system", "content": "你是一个专业、简洁的中文助手。"},
        {"role": "user", "content": "用三句话介绍一下你自己。"},
    ],
    temperature=0.7,
    max_tokens=2048,
)
print(completion.choices[0].message.content)
