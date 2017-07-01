from wechat_sender.listener import listen
from wxpy.api.bot import Bot


def run_server():
    bot = Bot()
    listen(bot)

if __name__ == '__main__':
    run_server()
