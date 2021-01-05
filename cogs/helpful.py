import discord
from discord.ext import commands


class KitsuneHelpMenu(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title="Help menu:",
            description='```<> = Required argument\n[] = Optional argument```\n[Support](https://discord.gg/Ph3zRHWG8E) | [website (WIP)](https://elf.is-a.dev/kitsune/) | [Invite](https://discord.com/api/oauth2/authorize?client_id=768967985326456874&permissions=470281318&scope=bot)'
        )
        cogs_to_display = []
        for cog, command in mapping.items():
            if not cog:
                continue
            if len(cog.get_commands()) > 0:
                cogs_to_display.append(f'• **{cog.qualified_name}**')

        embed.add_field(name='**Modules**', value='\n'.join(cogs_to_display))
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=command.qualified_name)
        embed.add_field(name="Usage:", value=self.get_command_signature(command))
        embed.add_field(name='Info:', value=command.help, inline=False)
        embed.add_field(name='Simply put:', value=command.brief, inline=False)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_cog_help(self, cog):
        for command in cog.walk_commands():
            print(command.qualified_name)


class HelpMenu(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(HelpMenu(bot))
