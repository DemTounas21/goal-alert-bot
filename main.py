import requests
import time
import os

# Βάλε εδώ το API key σου από το TheSportsDB ή άλλο provider
API_KEY = "YOUR_API_KEY"
API_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/livescore.php?s=Soccer"

# Βάλε εδώ το Telegram Bot Token και Chat ID
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=payload)

def check_live_matches():
    try:
        response = requests.get(API_URL)
        data = response.json()

        if data and data.get("events"):
            for match in data["events"]:
                home = match["strHomeTeam"]
                away = match["strAwayTeam"]
                score = f"{match['intHomeScore']} - {match['intAwayScore']}"
                time_min = match.get("intTime", "0")

                # Αν το ματς είναι μετά το 75' και είναι ισοπαλία -> πιθανότητα για γκολ
                if time_min.isdigit() and int(time_min) >= 75:
                    message = f"⚽ Υψηλή πιθανότητα γκολ!\n{home} vs {away}\nΣκορ: {score}\nΛεπτό: {time_min}'"
                    send_telegram_message(message)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    while True:
        check_live_matches()
        time.sleep(60)  # έλεγχος κάθε 60 δευτερόλεπτα
