import os
from telegram.ext import Updater, MessageHandler, filters

# 从环境变量中获取 Telegram 机器人的令牌
telegram_token = os.environ.get('TELEGRAM_BOT_TOKEN')

# 从环境变量中获取要监控的群组 ID
group_id = os.environ.get('GROUP_ID')

# 文件存储目录
file_directory = '/var/www/html/files'

# 重命名后的文件名
new_file_name = 'cfip.txt'

def handle_message(update, context):
    # 监听群聊中的文件消息
    message = update.message
    if message.document and message.chat_id == group_id:
        file = message.document
        file_id = file.file_id

        # 下载文件到指定目录
        file_path = os.path.join(file_directory, new_file_name)
        context.bot.get_file(file_id).download(file_path)

def main():
    # 创建 Telegram 机器人
    updater = Updater(telegram_token, use_context=True)
    dispatcher = updater.dispatcher

    # 注册消息处理程序
    message_handler = MessageHandler(filters.document, handle_message)
    dispatcher.add_handler(message_handler)

    # 启动 Telegram 机器人
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
