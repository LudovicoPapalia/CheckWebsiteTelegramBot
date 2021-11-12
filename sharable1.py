# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
import telegram.ext
import validators
# pip install python-telegram-bot

# here i define all the sites that i want to check

sites = ['https://telegra.ph/test-notificaiton-11-11', 'https://telegra.ph/test-notificaiton-2-11-11']


time.sleep(2)

counter = 0
HashDictionary = {}


print("arrived to line 20")


# here i start the telegram bot

TOKEN = 'CENSORED'

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

# here i define a password (a variable set on yes) to keep the bot "private". i want make it work only if the passord is correct,
# in the other cases i want to recieve an error message

password = "yes"

# bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help' and others

def start(update,context):
    print("readin start funzion")
    password = "x"
    update.message.reply_texy("Hey, i'll notify you on sites changes")
    time.sleep(30)
    if {update.message.text} == "Clock":
      update.message.reply_texy(f"Password correct, welcome")
      password = "yes"
    elif {update.message.text} != "Clock":
        password = "no"
        #update.message.reply_texy(f"password errata! Il bot è in beta e per te non funzionerebbe comunque!")


def help(update, context):
    print("reading help funcion")
    update.message.reply_texy("send a message to add a new website")

#now i'll handle ordinary messages.
# i want to check if a message is a valid url. If it is i append it on the url list
# if it's not i just send a message saying that the url it's not correct

def handle_message(update, context):

    print("working on ordinary messages now")

    validate = URLValidator()
    try:
        response = requests.get({update.message.text})
        print("URL is valid and exists on the internet")
        sites.append({update.message.text})
        update.message.reply_texy(f"url added correctly")

    except requests.ConnectionError as exception:
        print("URL does not exist on Internet")
        update.message.reply_texy(f"This is not an url. Please send a valid url")


#now i want to activate the functions

print("working on the activation of the funcions")
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

#using the following comand, the terminal says that there is an error si the comand it's not active

### updater.start_pooling()


updater.idle()

#-----
# form here i want to start a loop to continuosly check if a website is changed

# ATTENTION! THE LOOP IS STARTING

print("outside the loop. starting the loop now")

while True:
   # verification of the password. the value should be checked during the start function
    if password == "yes":
        print ("passord verification passed")

        counter = counter + 1

        for site in sites:
            # defining the position of the url that i'm analysing at the moment
            position = sites.index(site)

            url = site

            print("actualy checking the site " + site)
            time.sleep(3)

# here i'm veryfing if there is already an hash for thet sites

            if position in HashDictionary:
                response = urlopen(url).read()
                newHash = hashlib.sha224(response).hexdigest()
                time.sleep(10)

            #checking if the ash is the same
                if newHash == HashDictionary[position]:
                    continue

            #if it's not I SEND A NOTIFICATION USING TELEGRAM (notification to all users)
                else:
                    print("something changed")
                    update.message.reply_texy(f"qualcosa è cambiato alla url: " + site)

            #now, i save the new hash to notify other changes
                    response = urlopen(url).read()
                    currentHash = hashlib.sha224(response).hexdigest()
                    time.sleep(10)
                    HashDictionary[position] = currentHash

                    continue


# here, i add the hash to the dictionary if i don't have one for that website
            else:

# i define the answer ad i save it ad hash
# im' saving in a dictionary where the key is the position and the value is the hash
                response = urlopen(url).read()
                currentHash = hashlib.sha224(response).hexdigest()
                time.sleep(10)
                HashDictionary[position] = currentHash

                continue



# now i'. using this els to notify the user if the password is wrong
    else:
        print("verifica password superata con esisto negativo")

# this notification was not working so i deactivated it
      #  update.message.reply_texy(f"wrong password! This bot is still in private beta")
        continue

# disp.add_handler(telegram.ext.CommandHandler("start", start))
# disp.add_handler(telegram.ext.CommandHandler("help", help))
# disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# updater.start_pooling()
# updater.idle()



# @bot.message_handler(func=lambda message: True)
# def echo_message(message):


