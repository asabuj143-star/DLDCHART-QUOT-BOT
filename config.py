import os
from dotenv import load_dotenv
import pytz

load_dotenv()

# ====== Telegram Bot Settings ======
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
ADMIN_IDS = [123456789]  # আপনার Telegram User ID

# ====== Market Symbols ======
OTC_SYMBOLS = [
    "EURUSD=X", "GBPUSD=X", "USDJPY=X", 
    "XAUUSD=X", "BTC-USD", "ETH-USD"
]

REAL_SYMBOLS = [
    "EURUSD=X", "GBPUSD=X", "USDJPY=X", 
    "XAUUSD=X", "BTC-USD", "ETH-USD"
]

# ====== Timezone Settings ======
TIMEZONES = {
    "UTC": pytz.UTC,
    "GMT+6": pytz.timezone("Asia/Dhaka"),  # বাংলাদেশ সময়
    "IST": pytz.timezone("Asia/Kolkata"),  # ভারতীয় সময়
    "EST": pytz.timezone("US/Eastern"),    # আমেরিকা পূর্বাঞ্চল
    "PST": pytz.timezone("US/Pacific"),    # আমেরিকা পশ্চিমাঞ্চল
    "CET": pytz.timezone("Europe/Berlin"), # ইউরোপ
    "JST": pytz.timezone("Asia/Tokyo"),    # জাপান
    "AEST": pytz.timezone("Australia/Sydney")  # অস্ট্রেলিয়া
}

# ====== Timeframe Settings ======
TIMEFRAMES = {
    "1 Minute": "1m",
    "5 Minutes": "5m", 
    "15 Minutes": "15m",
    "1 Hour": "60m",
    "4 Hours": "240m"
}

# ====== Trading Settings ======
ACCURACY_THRESHOLD = 0.80  # 80% minimum accuracy
MAX_TRADES_PER_DAY = 20
STOP_LOSS_PERCENT = 2.0
TAKE_PROFIT_PERCENT = 3.0

# ====== Signal Strength Levels ======
SIGNAL_STRENGTH = {
    "VERY STRONG": 0.85,   # >85% probability
    "STRONG": 0.70,        # 70-85% probability  
    "NORMAL": 0.55,        # 55-70% probability
    "WEAK": 0.45           # <55% probability
}
