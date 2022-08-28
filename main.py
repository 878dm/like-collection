import telegram
import json
from telegram.ext import Updater,Messagehanler,Filters,CallbackContext
from telegram import Update

Token='5468504239:AAFnCFuZH99q0HYYF0iux_DGPrZoyFLwk9A'
updater = Updater(Token)
bot = telegram.Bot(token = Token)

def echo(update:Updatte, context:CallbackContext):
    text = update.message.text
    chat_id = update.message.chat.id 


    with open('like.json', 'r') as f:
        data = json.loads(f.read() or {})
    if not data or not data.get(f"{chat_id}"):
        data[f'{chat_id}']={
            "like"=0,
            'dilike'=0
        }

    if text = "👍":
        data[f"{chat_id}"]['like']+=1
    elif text = "👎":
        data[f"{dislike}"]["dislike"]+=1

    with open ("like.json", 'w') as f:
        f.write(json.dumps(data, indent = 2))

    bot.senMessage(chat_id,f"{data[f"{chat_id}"]["like"]}, {data[f"{chat_id}"]["dislike"]}")

updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))
updater.idle()