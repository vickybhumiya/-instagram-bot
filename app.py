from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "vicky123"

@app.route('/')
def home():
    return "WhatsApp Short Editor Bot Live - Vicky"

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == VERIFY_TOKEN:
        return challenge
    return "Verification Failed", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Message Aaya:", data)
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
