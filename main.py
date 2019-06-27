# -*- coding: utf-8 -*- 
import telebot as telebot
from telebot import apihelper
from deeppavlov import configs, train_model
from deeppavlov.core.common.file import read_json
from deeppavlov.core.commands.infer import build_model
from deeppavlov.core.commands.train import train_evaluate_model_from_config

print("import successful")
far = train_evaluate_model_from_config("./config.json")
faq = build_model("./config.json", download = True)
model_config = read_json("./config.json")
model_config["dataset_reader"]["data_path"] = "./faq_school_en.csv"
model_config["dataset_reader"]["data_url"] = None
faq = train_model(model_config)
print("train model")
bot = telebot.TeleBot('301914397:AAEmR8WlfzyxQT53zdpqHrSwR8iwaKEr-h8')

def GetAnswer(question):
    print("get question")
    return faq([question])[0][0][0]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print("text handler")
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        answer = GetAnswer(message.text)
        bot.send_message(message.from_user.id, answer)

bot.polling(none_stop=True, interval=0)
