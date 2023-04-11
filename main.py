import bot
from dotenv import load_dotenv


def configure():
    load_dotenv()


if __name__ == '__main__':
    configure()
    bot.run_discord_bot()
