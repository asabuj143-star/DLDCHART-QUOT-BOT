import telebot
from telebot import types

# আপনার বোট টোকেন
API_TOKEN = '8457629333:AAE2BiEUT9E3NNdRJhAw7AyO6ArXQOTzsWY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    # আপনার বাটনের তালিকা এবং রেফারেল লিঙ্ক
    btn1 = types.InlineKeyboardButton("🔑 Activation (New User / Upgrade)", url="https://broker-qx.pro/sign-up/?lid=1710075")
    btn2 = types.InlineKeyboardButton("🕰️ Old User Verification (TXID)", callback_data='verify')
    btn3 = types.InlineKeyboardButton("📡 Get Signal (FULL only)", callback_data='signals')
    btn4 = types.InlineKeyboardButton("📈 Future Charts (Paid)", callback_data='charts')
    btn5 = types.InlineKeyboardButton("🆘 Support", url="https://t.me/your_telegram_id")
    btn6 = types.InlineKeyboardButton("🔄 Resume Signals", callback_data='resume')
    btn7 = types.InlineKeyboardButton("🛑 Stop Signals", callback_data='stop')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.reply_to(message, "Main menu:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "verify":
        bot.answer_callback_query(call.id, "Please send your TXID to support.")

bot.polling()
