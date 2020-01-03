#!/usr/bin/env python3

# Updater to get the bot
# Message handler to deal with comments
# Filters to filter messages by text
from telegram.ext import Updater, MessageHandler, Filters

import logging

#for scraping

#for get request
from requests import get

#to parse json
from json import loads

TOKEN = '<ENTER BOT TOKEN HERE>'

POSSIBLE_QUERIES =[
    'how many forks fedora infra has',
    'fedora infra number of forks',
    'fedora infra has how many forks?',
    'give me number of fedora infra forks',
    'how many forks does fedora infra have',
    'fedora-infra number of forks'
]

def num_forks():
    #fetch number of forks from github api
    req = get(url='https://api.github.com/orgs/fedora-infra/repos')

    if req.ok:
        data = loads(req.text)
        return data[0]['forks']

def num_fork_handler(update, context):

    query = update.message.text
    if query in POSSIBLE_QUERIES :
        update.message.reply_text(
            'Fedora infra has {x} forks.'
            .format( x=num_forks() )
        )


def main():
    #get bot by token
    #use context to not recieve deprecation warnings
    #the updater is a high-level api that takes care of getting new messages (updates)
    my_bot = Updater(TOKEN, use_context=True)

    #dispatcher is needed to add handlers
    my_bot_dispatcher = my_bot.dispatcher

    #our num fork handler goes here
    my_bot_dispatcher.add_handler(MessageHandler(Filters.text, num_fork_handler))

    #every interval polls telegram
    my_bot.start_polling()
    
    my_bot.idle()

if __name__ == "__main__":
    main()