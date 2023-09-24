import discord # Подключаем библиотеку
from discord.ext import commands
from random import randint
import random
import string
import calendar
import time
from time import sleep

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
# С помощью декоратора создаём первую команду
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
		num2 = randint(10, 99) #генерация букв и цифр для номера
		print('---------')
		print(b[b1])
		print(num)
		print(b[b2])
		print(b[b3])
		print(num2)
		print('---------')
		kones = b[b1] + str(num) + b[b2] + b[b3] + str(num2)
		print(kones) #вывод и комбинирование букв и цифр номера
		wrt = kones + '\n'
		f = open('/storage/emulated/0/documents/Pydroid3/num.txt', 'a')
		f.write(wrt)
		f.close #сохранение в текстовик
		#sleep(0.2) #задержка
		await ctx.send(kones)
@bot.command()
async def ghoul(ctx):
	await ctx.send('Внимание возможен бан бота за спам')
	sleep(1)
	x = 1000
	for i in range(143):
		x2 = 7 
		x3 = x - x2
		x = x3
		await ctx.send(x3)
@bot.command()
async def test(ctx):
     
    def generate_password(length):
    	characters = string.ascii_letters + string.digits
    	password = ''.join(random.choice(characters) for _ in range(length))
    	return password
    	
    	for _ in range(20):
    		length = 50
    		password = generate_password(length)
    		print(password)
    await ctx.send(password)
@bot.command()
async def send(ctx):
        for sraka in range(100):
          for channel in ctx.guild.channels:
            	if channel.name == "основной-не":
            		
            		channel = bot.get_channel(channel.id)
            		test = input('')
            		await ctx.send(test)
@bot.command()
async def create(ctx):
	guild = ctx.guild
	for pon in range(50):
		name = 'не' + str(randint(1,500000))
		channel = await guild.create_voice_channel(name)
		await channel.send('Канал Создан')
@bot.command()
async def time(ctx):
	yy = (resultt.tm_year)
	mm = (resultt.tm_mon)
	mday = (resultt.tm_mday)
	clac = (calendar.month(yy, mm))
	await ctx.send(clac)
	await ctx.send("Сейчас: " + str(mday) + " Число") #ТАДЖИК БААЧАА
@bot.command()
async def lol(ctx):
	await ctx.send(f'sus')
	await ctx.send(file=discord.File("photo.png"))
bot.run('TOKEN')
