import os
import telebot
from flask import Flask

API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running and alive!"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot của Cường Bo đang hoạt động ổn định trên Render!")

# Lắng nghe bot và web server trên cùng một tiến trình
if __name__ == "__main__":
    # Bỏ qua polling để tránh xung đột, hoặc thiết lập webhook nếu cần. Sử dụng phương thức polling đơn giản:
    bot.remove_webhook()
    
    # Khởi động Flask web server trên cổng Render chỉ định
    port = int(os.environ.get("PORT", 10000))
    
    # Khởi động bot polling ở mức độ cơ bản
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    
    app.run(host="0.0.0.0", port=port)
