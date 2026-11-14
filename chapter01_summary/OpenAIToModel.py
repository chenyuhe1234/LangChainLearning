from openai import OpenAI

client = OpenAI(
    api_key="sk-2db88a2dc4564fcdbf47bc2f1b3e6355",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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