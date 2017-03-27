import logging

from bot.bot import Haikubot
import config

VERSION = 'v0.0.1'

logging.info('Running haikubot ' + VERSION)

if __name__ == "__main__":
    bot = Haikubot(config.API_KEY)
    try:
        bot.run()
    except:
        bot.clean_up()