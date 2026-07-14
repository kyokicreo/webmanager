import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def send_telegram_message(chat_id: str, text: str):
    if not chat_id or not BOT_TOKEN:
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=5)
    except Exception:
        pass