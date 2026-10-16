from flask import Flask, request, jsonify
import os
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>JesBot</title><style>body{background:#111;color:white;font-family:Arial;padding:10px}#box{border:1px solid #333;height:65vh;overflow-y:auto;padding:10px;border-radius:10px}.msg{margin:8px;padding:10px;border-radius:12px;max-width:85%}.user{background:#ff8c00;color:black;margin-left:auto;text-align:right}.bot{background:#222;color:#ffb84d;border:1px solid #333}#input-area{display:flex;gap:8px;margin-top:10px}#input{flex:1;padding:12px;border-radius:8px;border:none}button{padding:12px 18px;background:#ff8c00;border:none;border-radius:8px;font-weight:bold}</style></head><body><h2>JesBot</h2><div id="box"><div class="msg bot">Hello! I am JesBot from Jes Gift Cards. Ask me about gift cards!</div></div><div id="input-area"><input id="input" placeholder="Type..."><button onclick="send()">Send</button></div><script>async function send(){let i=document.getElementById('input');let t=i.value.trim();if(!t)return;let b=document.getElementById('box');b.innerHTML+=`<div class="msg user">${t}</div>`;i.value='';let r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:t})});let d=await r.json();b.innerHTML+=`<div class="msg bot">${d.reply}</div>`;b.scrollTop=b.scrollHeight;}</script></body></html>"""

@app.route('/')
def home(): return HTML

@app.route('/chat', methods=['POST'])
def chat():
    m=request.json.get('message','').lower()
    if 'gift' in m or 'card' in m: reply="We have $10 - N15k, $25 - N37.5k, $50 - N75k, $100 - N150k. Instant delivery! Which do you need?"
    elif 'ship' in m or 'deliver' in m: reply="Instant! 5 mins to email after payment."
    elif 'pay' in m: reply="We accept Bank Transfer, Opay, USDT."
    else: reply=f"You said: {m}. Ask about gift cards!"
    return jsonify({'reply':reply})

if __name__=='__main__':
    port=int(os.environ.get('PORT',10000))
    app.run(host='0.0.0.0',port=port)
