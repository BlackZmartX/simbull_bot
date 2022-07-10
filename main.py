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
    finally:
        fname = update.message.chat.first_name
    update.message.reply_text(f"Hey, {fname}!")
    update.message.reply_text("If you wanna talk, Say 'hi' to me!")
    update.message.reply_text("You can also explore me: /mypowers")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("Watchu want?")
    update.message.reply_text("If you have a problem with me, contact my master: @username")


def mypowers(update: Update, context: CallbackContext):
    update.message.reply_text("Yeah! ik I'm not perfect. But I can at least communicate with you like a human. So, Let's talk about anything and everything.")
    update.message.reply_text( '''And, the following commands are currently available on me:
    
/start -> Fresh Start
/help -> Ask for help
/mypowers -> Discover my abilities
/social -> Connect with my owner ''')


def social(update: Update, context: CallbackContext):
    update.message.reply_text('''Connect with YOUR_NAME
    
> GitHub: github.com/username
> Linktree: linktr.ee/username
> Instagram: instagram.com/username
> Twitter: twitter.com/username
> Website: website.com''')


def handle(update, context):
    text = str(update.message.text).lower()
    try:
        username = update.message.chat.username
    finally:
        fname = update.message.chat.first_name
    sys.stdout = open("chatlog.txt", "a")
    timezonelist = ['Asia/Colombo']
    for zone in timezonelist:
        now = datetime.now(timezone(zone))
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt, "[", username, "|", fname, "]", "-> ", text)
    response = R.sample_responses(text)
    update.message.reply_text(response)
    print(dt, "[ simbull_bot | Simbull ] -> ", response)
    sys.stdout.close()


def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('mypowers', mypowers))
    dp.add_handler(CommandHandler('social', social))

    dp.add_handler(MessageHandler(Filters.text, handle))

    updater.start_polling()

main()
