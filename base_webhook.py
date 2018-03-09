from flask import Flask, request

from os import environ
from time import sleep
from split_bot import BOT, UPDATE_QUEUE, TOKEN

URL = "https://split-bot.herokuapp.com/{}".format(TOKEN)

PORT = int(environ.get("PORT", 5000))
app = Flask(__name__)


@app.route("/{}".format(TOKEN), methods=['GET', 'POST'])
def pass_update():
    UPDATE_QUEUE.put(request.data)  # pass update to bot
    return 'OK'


if __name__ == '__main__':
    BOT.setWebhook()
    sleep(1)
    BOT.setWebhook(URL)
    app.run(host="0.0.0.0", port=PORT)
