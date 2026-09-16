from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "ZONA_BOT_2026"

@app.route("/")
def home():
    return "🟢 ZONA BOT online!"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    # Verificação da Meta
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200

        return "Token inválido", 403

    # Recebimento de mensagens
    if request.method == "POST":
        data = request.get_json()

        print("📩 Mensagem recebida:")
        print(data)

        return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
