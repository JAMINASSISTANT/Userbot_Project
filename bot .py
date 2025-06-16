from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio, requests, random

# Your API ID, HASH, and SESSION STRING
api_id = 21046086
api_hash = "55d6e403f0361578d0f9d058bfe1e0ed"
session_string = "1BVtsOIUBu6aefE2vqezAX5ajN6Ba870nIHV1GDsGPHWPbtXHAmuqQVls35rKZuDQCJloaawV7OLvHZD3c8K-Mm7xoWN8x5lBznujiqZgNFmt7JQARujvnI1McfPJOg4NwwxV2wHpsRGKpnPSZaH-28yCGung8NBBAhMFQlPH4WhwYA1BHS-rqtl5ojJ8wGtiY8aVLO_WS5hWyMOJSxPALSG213r3Ije9GmUFeGhr5eD7dILUtbAFdFtSef8X2O6aFTjfd41xYGUvoJTFFQ5apKx-7hUQUuyDEle9S__ehgRs7-lgzAeEDeF-fcIwLchR_grRhMQxj9AZzEnKQcsW1NGsM_sSbNg="

client = TelegramClient(StringSession(session_string), api_id, api_hash)

# Basic Commands
@client.on(events.NewMessage(outgoing=True, pattern=r".ping"))
async def ping(event):
    await event.edit("🏓 Pong! Bot is alive.")

@client.on(events.NewMessage(outgoing=True, pattern=r".alive|.start"))
async def alive(event):
    await event.edit("✅ **Userbot is Alive & Working!**")

@client.on(events.NewMessage(outgoing=True, pattern=r".help"))
async def help_cmd(event):
    cmds = """**🛠 Userbot Commands:**

.ping – Bot Status  
.alive / .start – Bot Working  
.help – Show Commands  
.temp – Weather  
.last – Last Message  
.spam – Repeat message  
.heart – ❤️ Emojis  
.hack – Hacking Simulation  
.tagall – Tag group members  
.rraid – Abuse spam  
.draid – Cute lines spam  
.fraid – Girls-friendly lines  
"""
    await event.edit(cmds)

@client.on(events.NewMessage(outgoing=True, pattern=r".temp"))
async def temp(event):
    res = requests.get("http://api.weatherapi.com/v1/current.json?key=a4a1f8ebe2024baab9870319250506&q=Bharatpur")
    res = res.json()
    loc = res['location']['name']
    temp_c = res['current']['temp_c']
    cond = res['current']['condition']['text']
    await event.edit(f"🌡️ **{loc}**: {temp_c}°C, {cond}")

@client.on(events.NewMessage(outgoing=True, pattern=r".spam (\d+) (.+)"))
async def spam(event):
    count = int(event.pattern_match.group(1))
    msg = event.pattern_match.group(2)
    for _ in range(count):
        await event.respond(msg)
        await asyncio.sleep(0.2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r".last"))
async def last(event):
    async for msg in client.iter_messages(event.chat_id, limit=2):
        if msg.id != event.id:
            await event.edit(f"🔙 Last Message:\n{msg.text}")
            break

@client.on(events.NewMessage(outgoing=True, pattern=r".hack"))
async def hack(event):
    text = "Hacking...\n[░░░░░░░░░░] 0%"
    await event.edit(text)
    for i in range(1, 11):
        await asyncio.sleep(0.5)
        text = f"Hacking...\n[{'█'*i}{'░'*(10-i)}] {i*10}%"
        await event.edit(text)
    await asyncio.sleep(1)
    await event.edit("✅ Target hacked successfully!")

@client.on(events.NewMessage(outgoing=True, pattern=r".heart"))
async def heart(event):
    emojis = "❤️🧡💛💚💙💜🖤💘💖💗💓💞💕💝"
    await event.edit(" ".join(random.choices(emojis, k=25)))

@client.on(events.NewMessage(outgoing=True, pattern=r".tagall"))
async def tagall(event):
    async for user in client.iter_participants(event.chat_id):
        if user.bot or user.deleted:
            continue
        name = f"{user.first_name}"
        await client.send_message(event.chat_id, name)
        await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r".rraid (\d+) (.+)"))
async def rraid(event):
    count = int(event.pattern_match.group(1))
    user = event.pattern_match.group(2)
    gaalis = [
        "Teri bahan ki chhoti chut me mota lund de dunga",
        "Teri bahan ke dudh dikha de kya unme se doodh aata hai",
        "Teri bahan ka muh chhota hai usme mota land de du",
        "Hair straightener lagake teri bahan ke jhant seedhe kar dunga",
        "Teri bahan ko online nilam kar du",
        "Telegram pe apni bahan ki chut dikhane aaya hai kya",
        "Chup sale chut ke fate virus",
        "Teri bahan ki chut ke 2 palla kar du",
        "Teri bahan ke muh me land rakh ke so jau",
        "Teri maa ki chut me kutta ka land de du"
    ]
    for _ in range(count):
        await client.send_message(user, random.choice(gaalis))
        await asyncio.sleep(0.5)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r".draid (\d+)"))
async def draid(event):
    count = int(event.pattern_match.group(1))
    lines = [
        "Tumhari aankhon mein kuch toh baat hai",
        "Ladkiyon jaise aap, duniya mein kam milti hai",
        "Cute ho tum, aur dil se bhi"
    ]
    for _ in range(count):
        await event.respond(random.choice(lines))
        await asyncio.sleep(0.5)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r".fraid (\d+)"))
async def fraid(event):
    count = int(event.pattern_match.group(1))
    lines = [
        "Tere jaisa smile to filter bhi nahi de sakta",
        "Tu ek hi dil hai, kitni baar jeetega",
        "Aisi ladkiyan fairy tale mein hoti hain"
    ]
    for _ in range(count):
        await event.respond(random.choice(lines))
        await asyncio.sleep(0.5)
    await event.delete()

# 🔒 Auto Delete Link if message contains Telegram or any URL
@client.on(events.NewMessage())
async def auto_delete_links(event):
    if event.is_group or event.is_channel:
        text = event.raw_text.lower()
        if "t.me/" in text or "telegram.me/" in text or "http://" in text or "https://" in text:
            try:
                await event.delete()
            except:
                pass

print(">> USERBOT STARTED <<")
client.start()
client.run_until_disconnected()
