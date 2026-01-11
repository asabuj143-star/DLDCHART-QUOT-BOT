import telebot
from telebot import types

# আপনার বোট টোকেন
API_TOKEN = '8457629333:AAE2BiEUT9E3NNdRJhAw7AyO6ArXQOTzsWY'
bot = telebot.TeleBot(API_TOKEN)

# প্রধান মেনু ফাংশন (যাতে বারবার কল করা যায়)
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
    bot.send_message(message.chat.id, "Main menu:", reply_markup=get_main_menu_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "activation":
        # আপনার স্ক্রিনশটের মতো টেক্সট
        activation_text = (
            "✅ Step 1: Register using our partner link:\n"
            "https://broker-qx.pro/sign-up/?lid=1703970  "
            "https://market-qx.pro/sign-up/?lid=1703970\n\n"
            "⏳ Wait at least 60 seconds, then send your UID here."
        )
        
        # Cancel বাটন
        markup = types.InlineKeyboardMarkup()
        cancel_btn = types.InlineKeyboardButton("❌ Cancel", callback_data='main_menu')
        markup.add(cancel_btn)
        
        # মেসেজ এডিট করে অ্যাক্টিভেশন টেক্সট দেখানো
        bot.edit_message_text(chat_id=call.message.chat.id, 
                              message_id=call.message.message_id, 
                              text=activation_text, 
                              reply_markup=markup, 
                              disable_web_page_preview=False)
    
    elif call.data == "main_menu":
        # Cancel চাপলে মেসেজটি আবার মেইন মেনুতে ফিরে যাবে
        bot.edit_message_text(chat_id=call.message.chat.id, 
                              message_id=call.message.message_id, 
                              text="Main menu:", 
                              reply_markup=get_main_menu_markup())

bot.polling()
