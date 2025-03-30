#  WeChet-ai
## 介绍
 一款基于DeepSeek的微信聊天机器人，它可以指定自动回复某个微信好友的消息
## 本地部署DeepSeek
#### 安装Ollama以及大模型
从官网安装
- [官网安装](https://www.ollamai.com/download/)

#### 在Ollama中安装DeepSeek
---[教程](https://blog.csdn.net/star_nwe/article/details/143141025)

等待安装完成
## 配置Python环境
#### 更换pip源（选）
```
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```
### 安装依赖包
---
#### 使用requirements.txt安装依赖包
```
pip install -r requirements.txt
```
#### 手动安装依赖包
```
pip install wxauto
pip install openai
```

## 使用
1. 登录微信电脑版
2. 修改names.txt文件
3. 将ai.py中第5行替换成本地部署的deepseek版本，例如（1.5b）
```python
model='deepseek-r1:1.5b',
```
4. 运行app.py
```
python app.py
```
4. 将会自动打开微信并监听消息

