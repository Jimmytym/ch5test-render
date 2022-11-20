from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('awdZYIF5Nu2CBHI3+n5Y8xuqSRo2hEMUpuNNGJVkBfGjzRzSoL4+rLTWsAo/cztO8ysjoWSQB6bXUgBDewC2vu7jiHrywA8/EJ3fDp7xIag5kTJezJvlOumZb29rI86XWB4rtoCUk92YAUoxJhsGUgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33cc2df502263f7f1767ab2151835402')

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
