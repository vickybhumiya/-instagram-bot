from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Live - Vicky"

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == "vicky123":
            return request.args.get("hub.challenge")
        return "Verification failed"
    else:
        print(request.json)
        return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
