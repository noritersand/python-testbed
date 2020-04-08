import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("법규를 준수하는지 감시")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")

client.run("Njk3MjUyNjA0NTg1MTgxMjQ0.Xo0lYw.007BhwgNGc5-_6f44P8EtXgkIho")

