import requests
import time

# 🔑 Βάλε εδώ το API key σου από το TheSportsDB (ή άλλη υπηρεσία με live scores)
API_KEY = "YOUR_API_KEY"
API_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/livescore.php?s=Soccer"

# 🤖 Βάλε εδώ το Telegram Bot Token και το Chat ID σου
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

def send_telegram_message(message):
    """Στέλνει μήνυμα στο Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=payload)

def check_live_matches():
    """Ελέγχει τα live παιχνίδια και ειδοποιεί αν υπάρχει πιθανότητα για γκολ"""
    try:
        response = requests.get(API_URL)
        data = response.json()

        if "events" in data and data["events"]:
            for match in data["events"]:
                home = match
