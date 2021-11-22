from unittest.mock import call

import telebot
from telebot import types, TeleBot

bot: TeleBot = telebot.TeleBot("1900873912:AAFnyRgiQUGBi61wVKxalNYNuPG3och3U88")
# создание клавиатуры 1

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Что ты такое?')
keyboard.row('Кто твой создатель?')
keyboard.row('Покажи фоточки животных')
keyboard.row('ты потрясающий!')


# вызвали клавиатуру
def send(id, text):
    bot.send_message(id, text, reply_markup=keyboard)


# забыл про команду для начала чата
@bot.message_handler(commands=['start'])
def start(message):
    send(message.chat.id, 'Приветствую, что вы хотите?')
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу рассказать о проекте, к которому при надлежу. Могу дать контактную информацию. Умею отправлять фото животных. Отлично поднимаю настроение')


# ответ на первый вопрос
@bot.message_handler(content_types=['text'])
def main(message):
    id = message.chat.id
    msg = message.text
    if msg == 'Что ты такое?':
        send(id, 'я бот-дз студента БВТ2105 Стаховского Артёма, он не придумал ничего лучше, чем сделать бота, который шлет фото'
             )
    elif msg == 'Кто твой создатель?':
        send(id,
             'Меня написал студент МТУСИ БВТ2105 Стаховский Артём, вот его контакты:')
        send(id,
             'https://vk.com/id371414821')
        send(id,
             'https://www.instagram.com/artem_stax/')
        send(id,
             'ну раз я бот, который шлет фоточки, отпралю его фоточку')
        send(id,
             'https://sun9-62.userapi.com/impf/yn9DgI7fqRMnp5ij-hsP3jw3MsQY1PSCoRgLZA/VGPlAXWFXfI.jpg?size=864x1080&quality=95&sign=c4422c50170b0247b34606448b5d8a22&type=album')



    elif msg == 'ты потрясающий!':
        send(id,
             'Нет, это ты потрясающий. Вы все потрясающие')
        send(id, 'https://memepedia.ru/wp-content/uploads/2019/06/keanu-meme.jpg')
    elif msg == 'Покажи фоточки животных':
        send(id,
             'могу показать таких животных')
        # Создаем инлайновую клавиатуру
        keyboard2 = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='домашние классик', callback_data='classic')
        keyboard2.add(key1)
        key2 = types.InlineKeyboardButton(text='домашние экзотик', callback_data='exotic')
        keyboard2.add(key2)
        key3 = types.InlineKeyboardButton(text='ферма', callback_data='farm')
        keyboard2.add(key3)
        key4 = types.InlineKeyboardButton(text='лес', callback_data='forest')
        keyboard2.add(key4)
        key5 = types.InlineKeyboardButton(text='пустыня', callback_data='desert')
        keyboard2.add(key5)
        key6 = types.InlineKeyboardButton(text='саванна', callback_data='savanna')
        keyboard2.add(key6)
        bot.send_message(id, 'каких вы хотите увидеть', reply_markup=keyboard2)




    else:
        send(id, 'Я Вас не понимаю')
        # обработчик нажатий
@bot.callback_query_handler(func=lambda call: True)
def otvet2(call):
            if call.data == 'classic':
                bot.send_message(call.message.chat.id, 'https://avatars.mds.yandex.net/get-zen_doc/4343677/pub_60ff0abf77d2ce0c79d17f41_60ff0b15ae6b9012eced9963/scale_1200')
            elif call.data == 'farm':
                bot.send_message(call.message.chat.id, 'https://krasivosti.pro/uploads/posts/2021-07/1626969242_49-krasivosti-pro-p-milaya-svinya-zhivotnie-krasivo-foto-51.jpg')
                bot.send_message(call.message.chat.id, 'https://www.fermerbezhlopot.ru/wp-content/uploads/2021/09/1336_v-prokopevskom-rayone-zhen.jpg')
                bot.send_message(call.message.chat.id, 'https://static.wikia.nocookie.net/apocalypse/images/4/4d/Skolko-vesit-600x450.jpg/revision/latest/top-crop/width/360/height/450?cb=20191109131310&path-prefix=ru')
            elif call.data == 'exotic':
                bot.send_message(call.message.chat.id,'https://i.ytimg.com/vi/85-zeCNQ-I0/maxresdefault.jpg')
                bot.send_message(call.message.chat.id,'https://krasivosti.pro/uploads/posts/2021-09/1630815015_1-krasivosti-pro-p-bolshaya-domashnyaya-zmeya-zhivotnie-krasi-1.jpg')
                bot.send_message(call.message.chat.id, 'https://aquariumsystems.su/images/13.jpg')
            elif call.data == 'forest':
                bot.send_message(call.message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Squirrel_posing.jpg/1200px-Squirrel_posing.jpg')
                bot.send_message(call.message.chat.id,'https://funart.pro/uploads/posts/2019-11/thumbs/1574092751_medved-v-tajge-foto-34.jpg')
                bot.send_message(call.message.chat.id,'https://vsezhivoe.ru/wp-content/uploads/2017/09/20.jpg')
            elif call.data == 'desert':
                bot.send_message(call.message.chat.id, 'https://i.pinimg.com/originals/13/90/0b/13900b8172df2252f800466150af889a.jpg')
                bot.send_message(call.message.chat.id,'https://dogcatdog.ru/wp-content/uploads/5/2/d/52d686e1e0eb70e7840d4fa9c4216cef.jpg')
                bot.send_message(call.message.chat.id,'http://faunazoo.ru/wp-content/uploads/2018/12/Животный-мир-тропических-пустынь2.jpg')
            elif call.data == 'savanna':
                bot.send_message(call.message.chat.id, 'https://dailypix.ru/uploads/posts/2013-04/dailypix.ru_136622472819.jpeg')
                bot.send_message(call.message.chat.id, 'https://i.pinimg.com/736x/b5/cb/2a/b5cb2a0d54247fd03735a9d46a52c5ff--save-animals-wild-animals.jpg')
                bot.send_message(call.message.chat.id, 'http://artes.su/wallpapers/9de3fc2f5dfa1cd5b8ae73be8db75148/6996_5.jpg')





bot.polling(none_stop=True)