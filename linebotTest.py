from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('gXj3xJZf60WN/iLnmq6t5ZAp8tLmL+nnoMRx4+9dkFu9tDPqcMcbEjUXm8owSEgj8ysjoWSQB6bXUgBDewC2vu7jiHrywA8/EJ3fDp7xIaiMUO/kj3FYM5/nRJQhuN2VIthQJFB+ji8a1Iw9hF0WswdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f8bcd3bd34388b36331990f9e0ce9d45')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()
