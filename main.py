import telebot
import constants

bot = telebot.TeleBot(constants.token)

#bot.send_message(783659796, "test");

upd = bot.get_updates();
#print(upd)
"""
last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)
"""

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Hi" or message.text == "hi":
        bot.send_message(message.chat.id, "Hi "+message.from_user.first_name)
        print(message)

bot.polling(none_stop=True, interval=0)