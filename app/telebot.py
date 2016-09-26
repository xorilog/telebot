from twx.botapi import TelegramBot, ReplyKeyboardMarkup

"""
Setup the bot
"""

bot = TelegramBot('BOTID')
bot.update_bot_info().wait()
print(bot.username)

"""
Send a message to a user
"""
user_id = int(userid)

result = bot.send_message(user_id, 'test message body').wait()
print(result)

"""
Get updates sent to the bot
"""
updates = bot.get_updates().wait()
for update in updates:
    print(update)
