# Monitora uma URL e envia mensagem para Telegram quando houver mudança
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = os.getenv("URL_MONITORADA", "https://example.com")
DELAY = int(os.getenv("CHECK_INTERVAL", "60"))

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": texto})

def pegar_conteudo():
    r = requests.get(URL, timeout=10)
    return r.text[:2000]

def main():
    ultimo = None
    while True:
        atual = pegar_conteudo()
        if ultimo is None:
            ultimo = atual
        elif atual != ultimo:
            enviar_mensagem("🔔 Mudança detectada em " + URL)
            ultimo = atual
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
