import telebot
from telebot import types

# আপনার বোট টোকেন
API_TOKEN = '8457629333:AAE2BiEUT9E3NNdRJhAw7AyO6ArXQOTzsWY'
bot = telebot.TeleBot(API_TOKEN)

# আপনার নিজের টেলিগ্রাম আইডি (এখানে আপনার আইডি দিন, যা @userinfobot থেকে পাবেন)
ADMIN_ID = 123456789  # উদাহরণ হিসেবে দেওয়া, আপনার আইডিটি এখানে লিখুন

# ইউজারদের আইডি সেভ করার জন্য একটি সেট (মেমোরিতে থাকবে)
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
    
    if user_id not in known_users:
        # প্রথমবার আসলে নোটিশ দেখাবে
        announcement_text = (
            "📢 **IMPORTANT ANNOUNCEMENT** 📢\n\n"
            "🇬🇧 **English**\n"
            "We are accepting only 400 members for now...\n\n"
            "🇧🇩 **বাংলা**\n"
            "আমরা এখন মাত্র ৪০০ জন মেম্বার নেব।"
        )
        bot.send_message(message.chat.id, announcement_text, reply_markup=get_main_menu_markup(), parse_mode='Markdown')
        known_users.add(user_id) # নতুন ইউজারকে লিস্টে যোগ করা হলো
    else:
        bot.send_message(message.chat.id, "Welcome back! Main menu:", reply_markup=get_main_menu_markup())

# শুধুমাত্র আপনার জন্য স্ট্যাটিসটিকস দেখার কমান্ড
@bot.message_handler(commands=['stats'])
def show_stats(message):
    # কোডটি চেক করবে আপনিই এডমিন কি না
    if message.from_user.id == ADMIN_ID:
        total_users = len(known_users)
        bot.reply_to(message, f"📊 বোটের বর্তমান মোট ইউজার সংখ্যা: {total_users}")
    else:
        bot.reply_to(message, "দুঃখিত, এই কমান্ডটি শুধুমাত্র এডমিনের জন্য।")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "activation":
        activation_text = "✅ Step 1: Register using our link...\n"
        markup = types.InlineKeyboardMarkup()
        cancel_btn = types.InlineKeyboardButton("❌ Cancel", callback_data='main_menu')
        markup.add(cancel_btn)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=activation_text, reply_markup=markup)
    
    elif call.data == "main_menu":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Main menu:", reply_markup=get_main_menu_markup())

bot.polling()
