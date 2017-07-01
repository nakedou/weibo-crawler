from wechat_sender import Sender


def send(msg):
    Sender().send(msg)

if __name__ == '__main__':
    send('hello')
