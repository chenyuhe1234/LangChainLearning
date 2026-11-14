import os
"""
 通过【环境变量】来获取配置
 思考:api_key=os.environ["DASHSCOPE_API_KEY"], 与 os.getenv("DASHSCOPE_API_KEY")的区别
"""
from openai import OpenAI


print("DASHSCOPE_API_KEY =", os.environ.get("DASHSCOPE_API_KEY"))
print("DASHSCOPE_BASE_URL =", os.environ.get("DASHSCOPE_BASE_URL"))
print("OPENAI_API_KEY =", os.getenv("DASHSCOPE_API_KEY"))
client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url=os.environ["DASHSCOPE_BASE_URL"],
)


completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": "你是一个专业、简洁的中文助手。"},
        {"role": "user", "content": "用三句话介绍一下你自己。"},
    ],
    temperature=0.7,
    max_tokens=2048,
)
print(completion.choices[0].message.content)
