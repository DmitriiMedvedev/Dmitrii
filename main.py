import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

token = "MTExNTk0MjEwMDY3Mjk5MTIzMg.GE0971.Z69T-uH-5OaB6-SIMICcYUjODK4KcBq9jvc2Zs"

curseWord = ['Ку']

@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in curseWord):
    
        await message.channel.send(f"{message.author.mention} Ку")
    else:
        return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```Укажите аргументы```')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("```Вы не имеете права```")


@client.event
async def on_ready():
    print("start")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Я Узкий"))

@client.command()
async def info(ctx):
    await ctx.send('Я личный бот <@976759765323644964>, пока я мало что умею...\nСервер "поддержки" https://discord.gg/qVnZ4cSQzf')

















client.run(token)
