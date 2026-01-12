import telebot
from telebot import types

# আপনার বোট টোকেন
API_TOKEN = '8457629333:AAE2BiEUT9E3NNdRJhAw7AyO6ArXQOTzsWY'
bot = telebot.TeleBot(API_TOKEN)

# যারা একবার বোট চালু করেছে তাদের আইডি রাখার জন্য একটি তালিকা
known_users = set()

def get_main_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("🔑 Activation (New User / Upgrade)", callback_data='activation')
    btn2 = types.InlineKeyboardButton("🕰️ Old User Verification (TXID)", callback_data='verify')
    btn3 = types.InlineKeyboardButton("📡 Get Signal (FULL only)", callback_data='signals')
    btn4 = types.InlineKeyboardButton("📈 Future Charts (Paid)", callback_data='charts')
    btn5 = types.InlineKeyboardButton("🆘 Support", url="https://t.me/your_telegram_id")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    
    # ইউজার যদি আগে না এসে থাকে (প্রথমবার)
    if user_id not in known_users:
        announcement_text = (
            "📢 **IMPORTANT ANNOUNCEMENT** 📢\n\n"
            "🇬🇧 **English**\n"
            "We are accepting only 400 members for now. After that, new user registration will be completely closed for this year.\n"
            "⌛ Don't waste time — join quickly.\n"
            "✅ 90%+ winning accuracy\n"
            "⚠️ 10% signals are intentionally incorrect so that Quotex cannot detect anything during withdrawals.\n"
            "❌ I do not trade personally.\n\n"
            "🇧🇩 **বাংলা**\n"
            "আমরা এখন মাত্র ৪০০ জন মেম্বার নেব। এরপর এই বছরের জন্য নতুন ইউজার নেওয়া পুরোপুরি বন্ধ করে দেওয়া হবে।\n"
            "⏳ তাই সময় নষ্ট না করে দ্রুত জয়েন করুন।\n"
            "✅ 90%+ WIN\n"
            "⚠️ 10% ইচ্ছাকৃতভাবে ভুল দেওয়া হয়, যেন Withdraw এর সময় Quotex বুঝতে না পারে।\n"
            "❌ আমি নিজে ট্রেড করি না।"
        )
        # তাকে নোটিশটি দেখাবে
        bot.send_message(message.chat.id, announcement_text, reply_markup=get_main_menu_markup(), parse_mode='Markdown')
        # ইউজারের আইডি সেভ করে রাখা হচ্ছে যাতে পরের বার নোটিশ না আসে
        known_users.add(user_id)
    else:
        # দ্বিতীয় বার থেকে শুধু মেইন মেনু দেখাবে
        bot.send_message(message.chat.id, "Welcome back! Main menu:", reply_markup=get_main_menu_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "activation":
        activation_text = (
            "✅ Step 1: Register using our partner link:\n"
            "https://broker-qx.pro/sign-up/?lid=1703970\n\n"
            "⏳ Wait at least 60 seconds, then send your UID here."
        )
        markup = types.InlineKeyboardMarkup()
        cancel_btn = types.InlineKeyboardButton("❌ Cancel", callback_data='main_menu')
        markup.add(cancel_btn)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=activation_text, reply_markup=markup)
    
    elif call.data == "main_menu":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Main menu:", reply_markup=get_main_menu_markup())

bot.polling()
