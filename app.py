from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "vicky123"

@app.route('/')
def home():
    return "Bot is Live - Vicky"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge
        return "Verification failed", 403
    else:
        print(request.get_json())
        return "ok", 200

if __name__ == '__main__':
    app.run()
