from telethon import TelegramClient, events

api_id = 21046086
api_hash = '55d6e403f0361578d0f9d058bfe1e0ed'

client = TelegramClient('userbot_session', api_id, api_hash)

@client.on(events.NewMessage(pattern='/hello'))
async def handler(event):
    await event.reply('Hello! Main aapka userbot hoon.')

client.start()
print("Userbot chaloo ho gaya!")
client.run_until_disconnected()
