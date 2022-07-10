from telegram.ext import *
from telegram.update import Update
from datetime import datetime
from pytz import timezone
import constants as keys
import responses as R
import sys


print("Simbull is running...")
timezonelist = ['Asia/Colombo']
for zone in timezonelist:
  now = datetime.now(timezone(zone))
print("Started on:", now)



def start(update: Update, context: CallbackContext):
    try:
        username = update.message.chat.username
    except:
        username = update.message.chat.first_name
    update.message.reply_text(f"Hey, @{username}!  Please don't fucking talk with me if you're not a virgin")
    update.message.reply_text("Do you understand it?")
    update.message.reply_text("If yes, let's continue babyyy!")
    update.message.reply_text("Tap this command to see what I can do: /mypowers")



def help(update: Update, context: CallbackContext):
    update.message.reply_text("Watchu want?")
    update.message.reply_text("If you have a problem with me, contact my master: @inuraxo")


def mypowers(update: Update, context: CallbackContext):
    update.message.reply_text("Yeah! ik I'm not perfect. But I can do these things.\n\n"
                              "Check my Instagram: /instagram")


def instagram_url(update: Update, context: CallbackContext):
    update.message.reply_text("Here's my Instagram ID:👇 \nwww.instagram.com/blackzmartx")


def handle(update, context):
    text = str(update.message.text).lower()
    try:
        username = update.message.chat.username
    except:
        username = update.message.chat.first_name
    sys.stdout = open("chatlog.txt", "a")
    timezonelist = ['Asia/Colombo']
    for zone in timezonelist:
        now = datetime.now(timezone(zone))
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt, "[", username, "]", "-> ", text)
    response = R.sample_responses(text)
    update.message.reply_text(response)
    print(dt, "[ simbull ] -> ", response)
    sys.stdout.close()


def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('mypowers', mypowers))
    dp.add_handler(CommandHandler('instagram', instagram_url))

    dp.add_handler(MessageHandler(Filters.text, handle))

    updater.start_polling()

main()
