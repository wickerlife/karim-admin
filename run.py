"""
Generate Telegram Client String Session manually from terminal
"""
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
client = TelegramClient(StringSession(), int('insert api_id here'), 'insert api_hash here').start()
print(client.session.save())