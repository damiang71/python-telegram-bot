import telepot
bot = 0

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, 'Te perdono')
    try:
        bot.sendPhoto(chat_id, open('/home/funky/bot/yisus.jpg', 'rb'))
    except Exception as ex:
        print(ex)

    print('sent')

def main():
    global bot
    bot = telepot.Bot('647689971:AAHhVj9VjUCakcMzTz0_amDDQJXQsolCfh0')
    bot.message_loop(handle, run_forever=True)

main()
