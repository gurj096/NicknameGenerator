#Imports required modules
import discord
from discord.ext import commands
import random
import yaml
import time
#DISCORD INVITE: https://discord.com/api/oauth2/authorize?client_id=1161553117528215552&permissions=201403392&scope=bot

# It is assumed that the .yaml file is in the same directory as this script
# Can be updated accordingly if file structure changes
with open('adjectives.yml', 'r') as file:
    adjectives = yaml.safe_load(file)

#establishes intents before initiating bot
intents = discord.Intents.default()
intents.message_content = True
#Sets the prefix which will queue the bot to listen in on commands
bot = commands.Bot(command_prefix='!', intents=intents)

# Uses .command to initialize bot
# Defines the wake command as '/nickname <arguments>'. Once entered with accompanying string(s) the bot will generate
# a new nickname for the user if permissions allow
@bot.command()
async def nickname(ctx, *args):
    # Handle case of empty arguments
    if len(args) == 0:
        await ctx.send(f'Invalid name. Please enter a valid name to add a nickname to. See `!help nickname` command for additional info.')
        return
    
    # Grab subsequent strings afte command and account for whitespace input
    user_preferred_name: str = " ".join(args).lower()

    # Use the first character of the name input by user to choose adjective
    # from a precompiled list of adjectives to use in the generated nickname
    first_char_of_name = user_preferred_name[0].lower()
    adjective_set = adjectives[first_char_of_name]
    chosen_adjective: str = random.choice(adjective_set)

    # Saves new nickname to a variable
    new_nickname: str = f'{chosen_adjective.title()} {user_preferred_name.title()}'

    await ctx.send(f'Your new nickname is __**{new_nickname}**__')

     

    # Attempt to change the nickname property of the user
    try:
        await ctx.author.edit(nick=new_nickname) # Tries to change name of author to new nickname
        await ctx.send(f"Changed your nickname to {new_nickname}.") # Sends confirmation 
    except: await ctx.send('Could not successfully change nickname.') # Error message if name could not be changed. (Most likely d/t to Discord's policy of not allowing bots to change names of Admins)
    
    # TODO: Bypass roles that prevent nickname changes to persist
    # 1) Attempt to remove current non-admin roles initially
    # 2) Store them for re-apply later?
    # 3) Apply nickname
    # 4) Re-add roles to user
    

# Remove provided help command
bot.remove_command('help')

# Bot Command: /help
# Sends message describing usage and functionality of the bot
@bot.command()
async def help(ctx, *args):
    # Handle case of empty arguments -- send message of how to use help command
    if len(args) == 0:
        await ctx.send(f'Use `!help <command_name>` to see documentation about that command\n__Example__: `!help nickname`')
        return
    # Check which command to display documentation for
    command: str = args[0].lower()
    match command:
        case "nickname":
            message: str = '__Usage__: `!nickname <name>`\n__Description__: Changes the server nickname of the user who called the command. After `/nickname` is used, the bot will prompt the user to type in their name and then generate an adjective to be used in their new nickname in the format of `<adjective> <name>`'
            await ctx.send(f'{message}')
        case _:
            await ctx.send(f'No documentation provided for the command / non-existant command input.')

bot.run() # This would normally include unique key provided by Discord
