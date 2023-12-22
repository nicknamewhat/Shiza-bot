import discord
from discord.ext import commands
from random import randint
import random
import string
import calendar
import time
from time import sleep
import typing
from gtts import gTTS
import os
import sys
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
resultt =time.localtime()
@bot.command()
async def gen(ctx):
	b = ['А', 'Б', 'В', 'Г', 'У', 'Х', 'Н', 'К', 'Л']
	#список букв
	for i in range(5):
		b1 = randint(0, 8)
		b2 = randint(0, 8)
		b3 = randint(0, 8)
		num = randint(100, 999)
		num2 = randint(10, 99)
		kones = b[b1] + str(num) + b[b2] + b[b3] + str(num2)
		await ctx.send(kones)
@bot.command()
async def send(ctx, *, text):
            			await ctx.send(f'{text}')
            			await ctx.message.delete()
@bot.command()
async def time(ctx):
	yy = (resultt.tm_year)
	mm = (resultt.tm_mon)
	mday = (resultt.tm_mday)
	clac = (calendar.month(yy, mm))
	await ctx.send(clac)
	await ctx.send("Сейчас: " + str(mday) + " Число")
@bot.command()
async def ball(ctx, *, text):
    ballr = randint(1,3)
    balt = (f'{ctx.message.author.mention} задал вопрос **{text}** , ответ')
    if ballr == 1:
    	await ctx.send(balt  + f'\n Да')
    else:
    	if ballr == 2:
    		await ctx.send(f'{text} \n  Нет')
    	else:
    		await ctx.send(f'{text} \n Спроси позже')
@bot.command()
async def хелп(ctx):
	await ctx.send('Мои команды \n !dm \n !join \n !leave \n !ball \n !gen \n !send \n !time \n !faq')
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    message = await ctx.send('Бот зашел в войс канал!')
    await message.add_reaction('<:emoji_1:1171105938250408017>')
@bot.command()
async def dm(ctx, member: discord.Member, *, message):
	await member.send(message)
@bot.command()
async def leave(ctx):
	await ctx.guild.voice_client.disconnect() 
	await ctx.channel.send('Бот вышел')
@bot.command()
async def faq(ctx):
	await ctx.send('Помощь по командам: \n !send <аргумент> \n !ball <аргумент>')
@bot.command()
async def tts(ctx, *, tmss):
	tts = gTTS(text=tmss)
	tts.save("tts.mp3")
	await ctx.send(file=discord.File("tts.mp3"))
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!хелп"))
	sleep(5)
	await bot.change_presence(activity=discord.Game(name="это тестовый бот"))
	sleep(5)
bot.run('MTExMzM5NDgwNDg2OTU3MDU3MA.GO67DD.eczp0HpDa0RvEQJP_RDD3v-475UoBAgCIEmpv4')