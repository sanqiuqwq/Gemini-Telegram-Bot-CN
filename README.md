# Gemini_Telegram_Bot_CN
一个使用 Gemini API 的 Telegram 机器人（已翻译为中文命令）[English ducument](https://github.com/H-T-H/Gemini_Telegram_Bot/blob/main/README_en.md)
# Demo
[点这里](https://t.me/gemini_telegram_demo_bot)  
# 说在前面
Google已停止gemini-2.5-pro模型的免费计划，所以免费用户无法使用该模型
# 如何安装
## (1) Linux系统
1. 安装依赖
```
pip install -r requirements.txt
```
2. 在[BotFather](https://t.me/BotFather)获取Telegram Bot API
3. 在[Google AI Studio](https://makersuite.google.com/app/apikey)获取Gemini API keys
4. 运行机器人，执行以下命令：
```
python main.py ${Telegram 机器人 API} ${Gemini API 密钥}
```
## (2)使用 Docker 部署
### 使用构建好的镜像(x86 only)
```
docker run -d --restart=always -e TELEGRAM_BOT_API_KEY={Telegram 机器人 API} -e GEMINI_API_KEYS={Gemini API 密钥} qwqhthqwq/gemini-telegram-bot:main
```
### 自行构建
1. 在[BotFather](https://t.me/BotFather)获取Telegram Bot API
2. 在[Google AI Studio](https://makersuite.google.com/app/apikey)获取Gemini API keys
3. 克隆项目
```
git clone https://github.com/sanqiuqwq/Gemini-Telegram-Bot-CN.git
```
4. 进入项目目录
```
cd Gemini-Telegram-Bot-CN
```
5. 构建镜像
```
docker build -t gemini_tg_bot .
```
6. 运行镜像
```
docker run -d --restart=always -e TELEGRAM_BOT_API_KEY={Telegram 机器人 API} -e GEMINI_API_KEYS={Gemini API 密钥} gemini_tg_bot
```

# 使用方法
1. 私聊中直接发送你的问题即可
2. 群组中使用 **/gemini** 或者 **/gemini_pro +你的问题**，支持多轮对话
3. 删除对话的历史记录请使用 **/clear**
4. 切换私聊中默认调用的模型请使用 **/switch**
5. 绘图使用 **/draw+你要的图片**，支持多轮对话
6. 编辑图片使用 **/edit + 你上传的图片+你要修改的地方**

# 参考信息
1. [https://github.com/yihong0618/tg_bot_collections](https://github.com/yihong0618/tg_bot_collections)
2. [https://github.com/yym68686/md2tgmd](https://github.com/yym68686/md2tgmd)

