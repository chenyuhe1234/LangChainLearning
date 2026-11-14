    import os
    import sys

    from dotenv import load_dotenv
    from langchain_core.messages import HumanMessage, SystemMessage
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI

    # 通过 LangChain API 从 .env 读取配置，访问大模型
    load_dotenv()

    api_key = os.getenv("DASHSCOPE_API_KEY")
    base_url = os.getenv("DASHSCOPE_BASE_URL")
    if not api_key or not base_url:
        sys.exit("请在 .env 或环境变量中配置 DASHSCOPE_API_KEY / DASHSCOPE_BASE_URL")

    # 初始化通义千问模型
    model = ChatOpenAI(
        model=os.getenv("QWEN_MODEL", "qwen-max"),
        api_key=api_key,
        base_url=base_url,
        temperature=0.7,
    )

    # 构造角色化对话消息
    messages = [
        SystemMessage(content="你是一个情感专家"),
        HumanMessage(content="异性之间如何才能相处的融洽"),
    ]

    # 定义提示词模板，format 后得到 PromptValue 实例
    prompt_template = ChatPromptTemplate.from_template("请介绍一下 {topic} 的最新发展。")
    prompt_value = prompt_template.format(topic="人工智能")

    # 三种入参形式调用
    print("---------- 第1轮调用 · 入参是字符串 ----------")
    response1 = model.invoke("帮忙分析一下如今的就业形势")
    print(response1.content)

    print("---------- 第2轮调用 · 入参是 PromptValue ----------")
    response2 = model.invoke(prompt_value)
    print(response2.content)

    print("---------- 第3轮调用 · 入参是消息列表 ----------")
    response3 = model.invoke(messages)
    print(response3.content)

