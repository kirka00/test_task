from telethon import TelegramClient
from config import api_id, api_hash


def bot_run(text):
    with TelegramClient('telega_bot/anon', api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message('me', text))