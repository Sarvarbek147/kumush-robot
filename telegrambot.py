import telebot
bot = telebot.TeleBot('1905657319:AAEVISQ9ktq71tZECKes_cSnafWaIzlFgG4')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    while 1:
        bot.reply_to(message, f'Temur jura tuzalib ket  ')
 
    

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
     while 1:
  
        bot.send_message("Akkuy singilcha")



 

bot.polling(none_stop=True) 