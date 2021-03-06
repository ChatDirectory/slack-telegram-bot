import os
import sys
import time

from slack import WebClient
# from telegram.bot import Bot

SLACK_TOKEN = os.environ['SLACK_TOKEN']
slack_client = WebClient(SLACK_TOKEN)

slack_client.chat_postMessage(
  channel="bots-talk",
  text="Hello from your app! :tada:"
)

# TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
# TELEGRAM_TARGET = os.environ['TELEGRAM_TARGET']
# telegram_bot = Bot(TELEGRAM_TOKEN)

# if sc.rtm_connect():
#     while True:
#         messages = sc.rtm_read()
#         for message in messages:
#             try:
#                 if message['type'] == 'message':
#                     if message['channel'][0] == 'G':
#                         channel = sc.api_call(
#                             "groups.info",
#                             channel=message['channel'])['group']
#                     elif message['channel'][0] == 'C':
#                         channel = sc.api_call(
#                             "channels.info",
#                             channel=message['channel'])['channel']
#                     else:
#                         channel = {'name': 'bot'}
#
#                     user = sc.api_call(
#                         "users.info",
#                         user=message['user'])['user']
#
#                     msg_string = '@{} posted to #{}: {}'.format(user['name'], channel['name'], message['text'])
#                     telegram_bot.sendMessage(TELEGRAM_TARGET, msg_string)
#             except:
#                 print('Could not send message.')
#                 print("Unexpected error:", sys.exc_info()[0])
#         time.sleep(1)
# else:
#     print("Connection Failed, invalid token?")