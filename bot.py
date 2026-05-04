import os
import telebot
from flask import Flask
from threading import Thread

# Khởi tạo bot
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot của Cường Bo đang hoạt động ổn định trên Render!")

# Tạo một web server nhỏ để Render không báo lỗi
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Chạy bot và web song song
if __name__ == "__main__":
    t = Thread(target=run_flask)
    t.start()
    bot.infinity_polling()
