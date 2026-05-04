import os
import telebot
from flask import Flask, request

API_TOKEN = os.getenv('API_TOKEN')
# Lấy URL Render của bạn (ví dụ: https://cuongbo-bot.onrender.com)
APP_URL = os.getenv('APP_URL')

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running via Webhook!"

@app.route('/' + API_TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

if __name__ == "__main__":
    # Đặt Webhook
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL + '/' + API_TOKEN)
    
    # Khởi chạy ứng dụng Web trên cổng Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
