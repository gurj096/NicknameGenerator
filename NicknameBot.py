#Imports required modules
import discord
from discord.ext import commands
import random
import yaml

#Opens yml needed
with open('enter dir of adjectives.yml', 'r') as file:
    adjectives = yaml.safe_load(file)

#establishes intents before initiating bot
intents = discord.Intents.default()
intents.message_content = True
#Sets the prefix which will queue the bot to listen in on commands
bot = commands.Bot(command_prefix='/', intents=intents)

#Uses .command to initialize bot
@bot.command()
async def nickname(ctx): #Defines the wake command as '/nickname'. Once entered, the bot will respond with "What is your name"
    await ctx.send('What is your name')
    name = await bot.wait_for('message') #Bot waits for name from user before continuing
    name = name.content #Converts name into readable string
    f_letter_name = name[0].lower() #Gets the first char of string and saves it to a variable
    adj_list = adjectives[f_letter_name] # Imports list from .yml file associated with variable name
    random_adj = random.choice(adj_list) # Randomly selects one element from list
    await ctx.send(f'Your new nickname is {random_adj.title()} {name.title()}') #Outputs new nickname

bot.run() # This would normally include unique key provided by Discord
