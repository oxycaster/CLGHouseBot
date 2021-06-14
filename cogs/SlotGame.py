import discord
from discord.ext import commands
import random


class SlotGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='すろっと')
    async def slot_hiragana(self, ctx, count=1, *, member: discord.Member = None):
        repeat = self.parse_repeat_count(count)
        await ctx.channel.send(self.slot(ctx.author.name, repeat))

    @commands.command(name='スロット')
    async def slot_katakana(self, ctx, count=1, *, member: discord.Member = None):
        repeat = self.parse_repeat_count(count)
        await ctx.channel.send(self.slot(ctx.author.name, repeat))

    @staticmethod
    def parse_repeat_count(count):
        # 回数指定
        repeat = 1
        try:
            repeat = int(count)
            if repeat > 10:
                repeat = 10
                return repeat
            else:
                return repeat
        except:
            return repeat

    @staticmethod
    def slot(name, repeat):
        # スロット
        slot_list = [':cherries:', ':bell:', ':rofl:', ':cat:', ':frog:', ':gem:', ':slot_machine:']
        count = 0
        msg = ""
        for i in range(1, repeat + 1):
            slot1 = random.sample(slot_list, 3)
            slot2 = random.sample(slot_list, 3)
            slot3 = random.sample(slot_list, 3)

            msg += "{0}回目：".format(i)

            random_case = random.randint(1, 3)
            if random_case == 1:
                msg += name + "さんが回しました！\n"
            elif random_case == 2:
                msg += name + "の渾身のスロット！\n"
            elif random_case == 3:
                msg += name + "選手！回しましたッ\n"

            msg += "┃  " + slot1[0] + "  ┃  " + slot2[0] + "  ┃  " + slot3[0] + "  ┃\n"
            msg += "┃  " + slot1[1] + "  ┃  " + slot2[1] + "  ┃  " + slot3[1] + "  ┃\n"
            msg += "┃  " + slot1[2] + "  ┃  " + slot2[2] + "  ┃  " + slot3[2] + "  ┃\n"

            # 揃ったかチェック
            if slot1[0] == slot2[0] == slot3[0] \
                or slot1[1] == slot2[1] == slot3[1] \
                or slot1[2] == slot2[2] == slot3[2] \
                or slot1[0] == slot2[1] == slot3[2] \
                or slot1[2] == slot2[1] == slot3[0]:
                count += 1

        msg += "揃った回数 : {0} / {1}".format(count, repeat)
        return msg


def setup(bot):
    bot.add_cog(SlotGame(bot))
