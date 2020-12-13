from discord.ext import commands
import discord
def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
class slowmodeCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
     await ctx.channel.edit(slowmode_delay=seconds)
     await ctx.send(f"I've set the slowmode to **{seconds}** seconds in {ctx.channel.mention}!")

def setup(bot):
    bot.add_cog(slowmodeCog(bot))

