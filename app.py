import ai
import db
from wxauto import *
import time

wx = WeChat()

listen_list = [] 

# 读取好友列表
file_path = 'names.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.readlines() 
        listen_list = [name.strip() for name in names]

except FileNotFoundError:
    print(f"文件 {file_path} 未找到，请检查文件路径是否正确！")
except Exception as e:
    print(f"读取文件时发生错误：{e}")

for i in listen_list:
    print(f"开始监听好友 {i} 的消息...")
    wx.AddListenChat(who=i, savepic=True)
    ai.add_user(i)

wait = 1  # 设置间隔时间

# 创建数据库
db.create_db()

while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who  # 获取聊天窗口名（人或群名）
        one_msgs = msgs[chat]  # 获取消息内容
        for msg in one_msgs:
            msgtype = msg.type  # 获取消息类型
            content = msg.content  # 获取消息内容
            print(f'【{who}】：{content}')

            if msgtype == 'friend':
                chat.SendMsg(ai.chat(who, content))
    time.sleep(wait)
