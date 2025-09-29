from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive!"

def run_server():
    port = int(os.environ.get("PORT", 8080))  # Railway автоматически задаёт PORT
    app.run(host="0.0.0.0", port=port)

# Запуск сервера в отдельном потоке
threading.Thread(target=run_server).start()
