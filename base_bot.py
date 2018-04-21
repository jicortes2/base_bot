import telepot
import requests
from command import TOKEN, start, masterdb, not_found
from time import sleep
from telepot.delegate import per_chat_id, create_open, pave_event_space
try:
    from Queue import Queue
except ImportError:
    from queue import Queue


commands = {
    # Public commands
    '/start': start,
    # Admin commands
    '/masterdb': masterdb,
    # Not found
    'not_found': not_found,
}


class Base(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)


    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        user_id = msg["from"]["id"]

        if False:
            # Change for debugging or getting a type
            # Remember to change settings to privacy mode
            self.find_message_type(msg, chat_id)

        text = msg['text']
        if not text.startswith("/"):
            return
        args = text.replace('@<Name_Bot>', '').split(' ', 1)
        func = commands.get(args[0], commands['not_found'])
        print(args)
        answer = func(user_id, *args)
        BOT.sendMessage(chat_id, answer, parse_mode="Markdown")


UPDATE_QUEUE = Queue()  # channel between `app` and `bot`

BOT = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, Base, timeout=10),
])
BOT.message_loop(source=UPDATE_QUEUE)  # take updates from queue
