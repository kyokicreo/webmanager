import requests

BOT_TOKEN = "8842165159:AAHunFotrDzMy5wB8iETIHqybINBSPIzmCA"


def send_telegram_message(chat_id: str, text: str):
    if not chat_id:
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=5)
    except Exception:
        pass