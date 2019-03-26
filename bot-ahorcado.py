import telebot
token = '647689971:AAHhVj9VjUCakcMzTz0_amDDQJXQsolCfh0'
bot = telebot.TeleBot(token)

dades = {}


# Parameters
known_word = ""
unknown_word = "_"*len(known_word)
fail_count = 0
max_count = 6

# Replace
def replace_letter(known_word, unknown_word, letter):
    new_unknown_word = ""
    for i in range(len(known_word)):
        if known_word[i]==letter:
            new_unknown_word += known_word[i]
        else:
            new_unknown_word += unknown_word[i]
    return new_unknown_word

def formatted_word(word):
    return "".join(l+" " for l in word)

def start_game():
    global known_word, unknown_word, fail_count, max_count
    known_word = "cruzadas"
    unknown_word = "_"*len(known_word)
    fail_count = 0
    max_count = 6
    #var1 = update.message.from_user['id']


# Handles all text messages that contains the commands '/start' or '/inicio'.
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    global known_word, unknown_word, fail_count, max_count, success_count
    start_game()
    chatid = message.chat.id
    bot.send_message(chatid, "Hola, bienvenido al juego del colgado.")
    bot.send_message(chatid, "Trata de adivinar la siguiente palabra.")
    bot.send_message(chatid, formatted_word(unknown_word))

# usar la primera letra
@bot.message_handler(func=lambda msg: True)
def send_something(message):
    global known_word, unknown_word, fail_count, max_count
    chatid = message.chat.id
    if fail_count<=max_count:
        letter = message.text[0].lower()
        bot.send_message(chatid, "Probando con la letra: {}".format(letter))
        if letter in known_word:
            bot.send_message(chatid, "Si, que suerte!")
            unknown_word = replace_letter(known_word, unknown_word, letter)
        else:
            fail_count += 1
            bot.send_message(chatid, "No!!! Te quedan {} intentos".format(max_count-fail_count))        
        bot.send_message(chatid, formatted_word(unknown_word))
        if unknown_word == known_word:
            bot.send_message(chatid, "Bravo, has adivinado!")
            bot.send_message(chatid, "Coloca /start para iniciar otro juego")
    else:
        bot.send_message(chatid, "Has perdido!")
        bot.send_message(chatid, "Coloca /start para iniciar otro juego")

# Apply all
bot.polling()
