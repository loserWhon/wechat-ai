from openai import OpenAI
import re
import db

message_table = {}
my_model='deepseek-r1:1.5b'

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

def add_user(user_name):
    message_table[user_name] = []

def add_history(user_name, role, content):
    message_table[user_name].append({"role": role, "content": content})

def clean_response(content):
    content = re.sub(r'\[.*?\]', '', content, flags=re.DOTALL)
    # 去除Markdown加粗和倾斜标记
    content = re.sub(r'\*\*\*', '', content)
    content = re.sub(r'\*\*', '', content)
    content = re.sub(r'\*', '', content)
    # 去除行首的#和-
    content = re.sub(r'^\t*[#-]+', '', content, flags=re.MULTILINE)

    content = re.sub(r'\n+', '\n', content)
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL)
    return content.strip()

def chat(user, prompt):
    db.add_history(user, "user", prompt)
    try:
        response = client.chat.completions.create(
            model=my_model,
            messages=db.get_history(user),
        )
        content = response.choices[0].message.content
        content = clean_response(content)
        db.add_history(user, "assistant", content)
        return content
    except Exception as e:
        print(f"Error: {e}")
        return "抱歉，我遇到了一个错误，请稍后再试。"
    