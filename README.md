# DeepSeek WeChet
## 介绍
DeepSeek WeChet 是一款基于DeepSeek的微信聊天机器人，它可以指定自动回复某个微信好友的消息
## 本地部署DeepSeek
#### 安装Ollama
可以从官网安装也可以从百度网盘下载安装包安装
- [官网安装](https://www.ollamai.com/download/)
- [百度网盘](https://pan.baidu.com/s/1V8TmzpE9WMcX_BrIDEPy8g?pwd=hjje)
- [夸克网盘](https://pan.quark.cn/s/57bda81b0391)（推荐）
#### 在Ollama中安装DeepSeek
---
1. 打开Ollama官网的[DeepSeek模块](https://ollama.com/library/deepseek-r1)
2. 选择合适的版本，复制命令
3. 打开命令行，输入命令，以7b为例
```
ollama install deepseek-r1
```
4. 等待安装完成
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
## 视频教程
[【抛弃手动回复！我让DeepSeek帮我回复微信消息】]( https://www.bilibili.com/video/BV1LCPkeEEsE/?share_source=copy_web&vd_source=a6ee755ed374184a3632d14b07f738a4)