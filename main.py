import requests
import time

API_KEY = "123"
API_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/livescore.php?s=Soccer"

TELEGRAM_TOKEN = "8359987952:AAF5duBgp7gTzHUuZ9_GT7Shvq4hr4_oxk8"
TELEGRAM_CHAT_ID = "6092250221"

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
