import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如果您没有配置环境变量，请在此处替换您的API-KEY
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务base_url
)
# 初始化messages列表
messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    # 请将 'file-fe-xxx1' 替换为您实际对话场景所使用的 file-id。
    {'role': 'system', 'content': f'file-fe-b1SLBScqnrwnc3oT44lGmbHA'},
    {'role': 'user', 'content': '这篇文章讲了什么？'}
]

# 第一轮响应
completion_1 = client.chat.completions.create(
    model="qwen-long",
    messages=messages,
    stream=False
)

# 打印出第一轮响应
# 如果需要流式输出第一轮的响应，需要将stream设置为True，并拼接每一段输出内容，在构造assistant_message的content时传入拼接后的字符
print(f"第一轮响应：{completion_1.choices[0].message.model_dump()}")

# 构造assistant_message
assistant_message = {
    "role": "assistant",
    "content": completion_1.choices[0].message.content}

# 将assistant_message添加到messages中
messages.append(assistant_message)

# 将追加文档的fileid添加到messages中
# 请将 'file-fe-xxx2' 替换为您实际对话场景所使用的 file-id。
system_message = {'role': 'system', 'content': f'fileid://file-fe-pHOYGDvtlXjUMC5zAEVHTtHH'}
messages.append(system_message)

# 添加用户问题
messages.append({'role': 'user', 'content': '这两篇文章讨论的方法有什么异同点？'})

# 追加文档后的响应
completion_2 = client.chat.completions.create(
    model="qwen-long",
    messages=messages,
    stream=True,
    stream_options={
        "include_usage": True
    }
)

# 流式打印出追加文档后的响应
print("追加文档后的响应：")
full_content = ""
for chunk in completion_2:
    if chunk.choices and chunk.choices[0].delta.content:
        full_content += chunk.choices[0].delta.content
print(chunk.model_dump())

# print({full_content})
# for chunk in completion_2:
#     print(chunk.model_dump())