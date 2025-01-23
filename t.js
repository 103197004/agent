import OpenAI from "openai";

const openai = new OpenAI(
    {
        // 若没有配置环境变量，请用百炼API Key将下行替换为：apiKey: "sk-xxx",
        apiKey: process.env.DASHSCOPE_API_KEY,
        baseURL: "https://dashscope.aliyuncs.com/compatible-mode/v1"
    }
);

async function main() {
    const response = await openai.chat.completions.create({
        model: "qwen-vl-max",
        messages: [{role: "user",content: [
            { type: "text", text: "这是什么？" },
            { type: "image_url",image_url: {"url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"}}
        ]}]
    });
    console.log(JSON.stringify(response));
}

main();

//https://bailian.console.aliyun.com/?spm=a2c4g.11186623.0.0.1a8c4823e1E9Ba#/model-market/detail/qvq-72b-preview?tabKey=sdk

// sk-5fbc8001f88a41a8b64bd2cc781be8f8