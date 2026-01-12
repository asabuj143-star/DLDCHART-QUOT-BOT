import telebot
from telebot import types

# আপনার বোট টোকেন
API_TOKEN = '8457629333:AAE2BiEUT9E3NNdRJhAw7AyO6ArXQOTzsWY'
bot = telebot.TeleBot(API_TOKEN)

# আপনার সঠিক আইডি (আপনার প্রোফাইল অনুযায়ী)
ADMIN_ID = 46200863 

# ইউজারদের মনে রাখার জন্য একটি লিস্ট
known_users = set()

def get_main_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("🔑 Activation (New User / Upgrade)", callback_data='activation')
    btn2 = types.InlineKeyboardButton("🕰️ Old User Verification (TXID)", callback_data='verify')
    btn3 = types.InlineKeyboardButton("📡 Get Signal (FULL only)", callback_data='signals')
    btn4 = types.InlineKeyboardButton("📈 Future Charts (Paid)", callback_data='charts')
    btn5 = types.InlineKeyboardButton("🆘 Support", url="https://t.me/me46200863")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    known_users.add(user_id) # ইউজারের আইডি সেভ করা হলো
    
    # প্রথমবার নোটিশ দেখানো
    announcement_text = (
        "📢 **IMPORTANT ANNOUNCEMENT** 📢\n\n"
        "🇬🇧 **English**\n"
        "We are accepting only 400 members for now...\n\n"
        "🇧🇩 **বাংলা**\n"
        "আমরা এখন মাত্র ৪০০ জন মেম্বার নেব।"
    )
    bot.send_message(message.chat.id, announcement_text, reply_markup=get_main_menu_markup(), parse_mode='Markdown')

# আপনি বোটের ভেতর কেবল /count লিখলেই মেম্বার সংখ্যা দেখাবে
@bot.message_handler(commands=['count', 'stats'])
def show_stats(message):
    if message.from_user.id == ADMIN_ID:
        total_users = len(known_users)
        bot.reply_to(message, f"📊 বর্তমান মোট ইউজার: {total_users}")
    else:
        bot.reply_to(message, "❌ আপনি এই কমান্ডটি ব্যবহারের অনুমতি নেই।")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "activation":
        activation_text = (
            "✅ Step 1: Register using our partner link:\n"
            "https://broker-qx.pro/sign-up/?lid=1710075\n\n"
            "⏳ Wait at least 60 seconds, then send your UID here."
        )
        markup = types.InlineKeyboardMarkup()
        cancel_btn = types.InlineKeyboardButton("❌ Cancel", callback_data='main_menu')
        markup.add(cancel_btn)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=activation_text, reply_markup=markup)
    
    elif call.data == "main_menu":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Main menu:", reply_markup=get_main_menu_markup())

bot.polling()
