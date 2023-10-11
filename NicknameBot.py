#Imports required modules
import discord
from discord.ext import commands
import random
import yaml
#DISCORD INVITE: https://discord.com/api/oauth2/authorize?client_id=1161553117528215552&permissions=201403392&scope=bot
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
    print(ctx.author.name)
    time.sleep(0.5) # To prevent code from looping on itself as there appears to be a delay between running the code and displaying results on Discord
    while True:
        try:
           
            #while True: #Loop to prompt the user to enter a different name if first char of entered name is not a key in the dictionary
            name = await bot.wait_for('message') #Bot waits for name from user before continuing
            name = name.content #Converts name into readable string
            f_letter_name = name[0].lower() #Gets the first char of string and saves it to a variable
            adj_list = adjectives[f_letter_name] # Imports list from .yml file associated with variable name
            random_adj = random.choice(adj_list) # Randomly selects one element from list
            await ctx.send(f'Your new nickname is {random_adj.title()} {name.title()}') #Outputs new nickname
            new_nick = f'{random_adj.title()} {name.title()}' #Saves new nickname to a variable
            break
        #Tests whether an error will be thrown or not depending on if the f_letter_name variable is a key 
        except:
            await ctx.send('Please enter a valid name')
            time.sleep(1)
            
    try:
        await ctx.author.edit(nick=new_nick) # Tries to change name of author to new nickname
        await ctx.send(f"Changed your nickname to {new_nick}.") # Sends confirmation 
    except: await ctx.send('Could not successfully change nickname') # Error message if name could not be changed. (Most likely d/t to Discord's policy of not allowing bots to change names of Admins)

bot.run() # This would normally include unique key provided by Discord
