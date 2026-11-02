from flask import Flask, request
import requests
app = Flask(__name__)
VERIFY_TOKEN = "e322cb247118a6a"
ACCESS_TOKEN = "EAAN9xZAy5W7YBS7vUyjsZCPKew9rtI4E4rXBXsJg0hIzLXdPzmaLhJ0Ck92nur25ebNDCBI4YZCNCPrFwx3QeuKRwLdw0UM7PeXBT9gjZCOV3BEq1ZCiC1jJ2KZCZCjh6Sz3LcpFi0jQ8pFkkDakDmlq5k7SxdqjmeYzYWzMiZCZA6wUndj4cKzZAyuHvAyZCZBaDlqdR3TDvPP4FjUQVJVhK35cZCsVIHVrBtJkZC7EsHydEwWSAyJJRHaaPX6KgGbrCdK3sDQBDtWUZCKbzwFGF0dMzF0PWRmlAZD"
PHONE_ID = "780819962413712"
@app.route('/')
def home(): return "Bot is Live - Vicky"
@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        return "Verification failed", 403
    data = request.get_json()
    try:
        val = data['entry'][0]['changes'][0]['value']
        if 'messages' in val:
            frm = val['messages'][0]['from']
            txt = val['messages'][0]['text']['body']
            url = f"https://graph.facebook.com/v19.0/{PHONE_ID}/messages"
            headers = {"Authorization": f"Bearer {ACCESS_TOKEN}","Content-Type":"application/json"}
            body = {"messaging_product":"whatsapp","to":frm,"text":{"body":f"Aapne bheja: {txt} ✅\nBot Active Hai!"}}
            requests.post(url, json=body, headers=headers)
    except: pass
    return "OK", 200
if __name__ == '__main__': app.run(host='0.0.0.0', port=10000)
