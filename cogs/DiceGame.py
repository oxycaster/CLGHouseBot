import discord
from discord.ext import commands
import random


class DiceGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='さいころ')
    async def dice_hiragana(self, ctx, *, member: discord.Member = None):
        await ctx.channel.send(self.dice(ctx.author.name))

    @commands.command(name='サイコロ')
    async def dice_katakana(self, ctx, *, member: discord.Member = None):
        await ctx.channel.send(self.dice(ctx.author.name))

    @staticmethod
    def dice(name):
        random_case = random.randint(1, 3)
        dice = random.randint(1, 100)
        if random_case == 1:
            msg = "```" + name + "さんのサイコロ結果 : " + str(dice) + "```"
        elif random_case == 2:
            msg = "```" + name + "さんがサイコロを振りました！ : " + str(dice) + "```"
        elif random_case == 3:
            msg = "```" + name + "さんが出したサイコロの目は！ : " + str(dice) + "```"
        return msg


def setup(bot):
    bot.add_cog(DiceGame(bot))
