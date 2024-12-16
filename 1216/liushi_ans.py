import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁？'}
        ],
    stream=True
    )
full_content = ""
print("流式输出内容为：")
for chunk in completion:
    full_content += chunk.choices[0].delta.content
    print(chunk.choices[0].delta.content)
print(f"完整内容为：{full_content}")