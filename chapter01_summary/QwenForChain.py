import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from pydantic import BaseModel, Field

"""
   通过LangChain框架 来问千问模型问题-样例代码3
   使用LangChain链进行处理 + JSON结构化输出
"""
load_dotenv(override=True)

# 1. 初始化通义千问模型
model = ChatOpenAI(
    model=os.getenv("QWEN_MODEL", "qwen-max"),
    openai_api_key=os.getenv("DASHSCOPE_API_KEY"),
    openai_api_base=os.getenv("DASHSCOPE_BASE_URL"),
    temperature=0.7
)

# 2. 定义输出结构
class EmotionResponse(BaseModel):
    """情感问题的结构化回答"""
    summary: str = Field(description="一句话总结回答")
    key_points: list[str] = Field(description="关键建议，每条一个要点")
    detailed_advice: str = Field(description="详细的建议说明")

# 3. 创建提示词模板（明确告知 JSON 字段名）
system_template = """你是一个情感专家，请以JSON格式结构化地回答问题。
请严格按照以下JSON字段返回：
- summary: 一句话总结回答
- key_points: 关键建议列表，每条为一个字符串
- detailed_advice: 详细的建议说明"""
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{question}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# 4. 使用 json_mode 让模型返回 JSON
structured_model = model.with_structured_output(EmotionResponse, method="json_mode")

# 5. 组合链并执行
chain = chat_prompt | structured_model
input_question = "异性之间如何才能相处的融洽"
response = chain.invoke({"question": input_question})

# 6. 输出结果
print(response)
print("---")
print(response.summary)
print(response.key_points)
print(response.detailed_advice)
print("---")
print(response.model_dump_json(indent=2))