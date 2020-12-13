from discord.ext import commands
import discord
import asyncio
def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
class unmuteCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member, reason=None):
      role = discord.utils.get(ctx.guild.roles, name="Muted")

      embed = discord.Embed(color=discord.Color.green())
      embed.add_field(name=f"You've been **Unmuted** in {ctx.guild.name}.", value=f"**Action By: **{ctx.author.mention}")
      await member.send(embed=embed)

      await member.remove_roles(role)



def setup(bot):
    bot.add_cog(unmuteCog(bot))
    # Adds the Basic commands to the bot
