# GCI Telegram Bot

Simple telegram bot that fetches the number of forks from fedora-infra

# How to use this

Install telegram desktop, then talk to [Bot Father](https://telegram.me/BotFather) to make a bot. You'll recieve a token for using the bot and also and also the telegram link of the bot. Now put the token in `token.txt` , run this in a shell

```bash
# make sure you have the token of the bot in token.txt
python3 bot.py
```

Then try to talk to  the bot using it's telegram link. Tell it
`how many forks does fedora-infra have`

and it will fetch the results from github API, and reply something like
`Fedora infra has 154 forks.`

Fork the fedora-infra repo then ask it again to verify yourself.

# How it should look like

![Fedora Infra Bot.png](../master/fedora_infra_bot.png?raw=true)
