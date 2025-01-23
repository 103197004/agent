import requests

# 假设Qwen提供了一个RESTful API
QWEN_API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
API_KEY = "sk-5fbc8001f88a41a8b64bd2cc781be8f8"

def analyze_intent(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "text": user_input
    }
    response = requests.post(QWEN_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        print(response)
        return response.json()  # 假设返回的JSON包含意图信息
    else:
        raise Exception("Failed to analyze intent")

def call_tool(intent):
    # 根据意图调用相应的工具
    if intent == "weather":
        return "It's sunny today."
    elif intent == "news":
        return "Here are today's top news headlines."
    else:
        return "I'm not sure how to help with that."

def main():
    user_input = input("Please enter your question: ")
    try:
        intent_data = analyze_intent(user_input)
        intent = intent_data.get("intent")
        result = call_tool(intent)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
