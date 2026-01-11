import telebot
from telebot import types

# আপনার বোট টোকেন
API_TOKEN = '8457629333:AAE2BiEUT9E3NNdRJhAw7AyO6ArXQOTzsWY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # মেনু বাটনগুলো
    # এখানে 'Activation' বাটনের জন্য 'callback_data' ব্যবহার করা হয়েছে যাতে বোট রিপ্লাই দিতে পারে
    btn1 = types.InlineKeyboardButton("🔑 Activation (New User / Upgrade)", callback_data='activation')
    btn2 = types.InlineKeyboardButton("🕰️ Old User Verification (TXID)", callback_data='verify')
    btn3 = types.InlineKeyboardButton("📡 Get Signal (FULL only)", callback_data='signals')
    btn4 = types.InlineKeyboardButton("📈 Future Charts (Paid)", callback_data='charts')
    btn5 = types.InlineKeyboardButton("🆘 Support", url="https://t.me/your_telegram_id")
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.reply_to(message, "Main menu:", reply_markup=markup)

# বাটন ক্লিকের রেসপন্স হ্যান্ডলার
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "activation":
        # আপনার স্ক্রিনশটের মতো হুবহু টেক্সট এবং লিঙ্ক
        activation_text = (
            "✅ Step 1: Register using our partner link:\n"
            "https://broker-qx.pro/sign-up/?lid=1703970  "
            "https://market-qx.pro/sign-up/?lid=1703970\n\n"
            "⏳ Wait at least 60 seconds, then send your UID here."
        )
        
        # 'Cancel' বাটন যোগ করা
        markup = types.InlineKeyboardMarkup()
        cancel_btn = types.InlineKeyboardButton("❌ Cancel", callback_data='main_menu')
        markup.add(cancel_btn)
        
        bot.send_message(call.message.chat.id, activation_text, reply_markup=markup, disable_web_page_preview=False)
    
    elif call.data == "main_menu":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_welcome(call.message)

bot.polling()
