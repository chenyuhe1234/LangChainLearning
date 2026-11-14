import os
import json
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser  # 引入 JsonOutputParser

# 加载 .env 文件中的环境变量
load_dotenv()

# 调用对话模型
chat_model = ChatOpenAI(
    model_name=os.getenv("MODEL_NAME"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    request_timeout=60.0
)

# 1. 定义 JsonOutputParser
# 如果定义了 schema，LangChain 会自动在 prompt 中追加格式要求（部分模型支持）
# 此处仅做基础解析演示
parser = JsonOutputParser()

# 2. 定义提示词模板
# 关键：必须明确要求模型输出 JSON 格式
# 关键修改：将 JSON 示例中的 {和 } 替换为 {{ 和 }} 以转义
prompt_template = ChatPromptTemplate.from_template(
    """
     你是一个专业的AI助手。
     请回答关于 {topic} 的最新发展。要求：
     1. 仅输出一个合法的 JSON 对象。
     2. JSON 结构如下：
     {{
         "summary": "简短总结",
         "key_points": ["要点1", "要点2"]
     }}
     3. 不要输出任何 markdown 标记（如 ```json），只输出纯 JSON 字符串。
     """
)

# 3. 构建 LCEL 链
# prompt -> model -> parser
chain = prompt_template | chat_model | parser

# 4. 执行调用
try:
    # invoke 返回的是解析后的 Python 字典对象
    result_dict = chain.invoke({"topic": "人工智能"})

    # 输出结果（此时 result_dict 已经是 dict类型，无需手动 json.loads）
    print("=== 使用 JsonOutputParser 的结果 ===")
    print(json.dumps(result_dict, ensure_ascii=False, indent=2))

except Exception as e:
    print(f"解析失败或请求错误: {e}")
