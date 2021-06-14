import base64
import logging
import os
import time
import uuid

from discord.ext import commands



os.environ["TZ"] = "UTC"
time.tzset()
print(time.tzname)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARN)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("[%(levelname)s]: %(relativeCreated)07d[ms] : %(name)s : %(lineno)s : %(message)s"))
logger.addHandler(handler)


app_credentials_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
base64_credentials = os.environ.get('GOOGLE_CREDENTIALS')
with open(app_credentials_path, 'wb') as out:
    json_str = base64.b64decode(base64_credentials.encode('utf-8'))
    out.write(json_str)
    logger.debug(json_str)

bot_token = os.environ.get('TOKEN')

bot = commands.Bot(command_prefix='')
bot.load_extension('cogs.DiceGame')
bot.load_extension('cogs.SlotGame')
bot.load_extension('cogs.Yomiage')
bot.run(bot_token)
