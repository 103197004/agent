import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key='sk-5fbc8001f88a41a8b64bd2cc781be8f8', 
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-plus", # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁？'}],
    )
    
print(completion.model_dump_json())


# https://bailian.console.aliyun.com/?spm=a2c4g.11186623.0.0.1a8c4823e1E9Ba#/model-market/detail/qwq-32b-preview?tabKey=sdk