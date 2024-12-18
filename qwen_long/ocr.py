# pip install -U openai
import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-vl-ocr",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241108/ctdzex/biaozhun.jpg",
                    "min_pixels": 28 * 28 * 4,
                    "max_pixels": 1280 * 784
                },
                {"type": "text", "text": "Read all the text in the image."},
            ]
        }
    ],
    top_p=0.01,
    temperature=0.1,
    max_tokens=2000)
        
print(completion.choices[0].message.content)