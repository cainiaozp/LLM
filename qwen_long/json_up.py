import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
file_info_1 = {
    'content': '百炼X1————畅享极致视界：搭载6.7英寸1440 x 3200像素超清屏幕，搭配120Hz刷新率...',
    'file_type': 'pdf',
    'filename': 'test_case_1',
    'title': 'test_case_1'
}

file_info_2 = {
    'content': '星尘S9 Pro —— 创新视觉盛宴：突破性6.9英寸1440 x 3088像素屏下摄像头设计:...',
    'file_type': 'pdf',
    'filename': 'test_case_2',
    'title': 'test_case_2'
}

# 首次对话会等待文档解析完成，首轮响应时间可能较长
completion = client.chat.completions.create(
    model="qwen-long",
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'system', 'content': json.dumps(file_info_1, ensure_ascii=False)},
        {'role': 'system', 'content': json.dumps(file_info_2, ensure_ascii=False)},
        {'role': 'user', 'content': '这两篇文章讨论的产品有什么异同点？'},
    ],
    stream=True,
    stream_options={"include_usage": True}
)

full_content = ""
for chunk in completion:
    if chunk.choices and chunk.choices[0].delta.content:
        full_content += chunk.choices[0].delta.content
        print(chunk.model_dump())

print({full_content})