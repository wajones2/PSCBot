import discord
from discord.ext import commands
from verify import Verify
TOKEN = DISCORD_TOKEN_STRING_HERE

"""Make sure PSC Bot role is above the roles you want to add"""

ver = Verify()
client = commands.Bot(command_prefix = '/', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("------------------------------")


@client.command()
async def verify(ctx, email):
    status = ver.memberVerify(email)

    role = discord.utils.get(ctx.guild.roles, name="Member")

    if status[0] == True:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.nick} has been granted the '{role}' role ")
    else:
        await ctx.send("You must be a member to be granted the '{role}' role")

            

client.run(TOKEN)

