import requests
import json

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
URL = 'https://api.telegram.org/bot' + TOKEN + '/'

class Api:
    def __init__(self):
        self.last_message = 0;

    def read_messages(self, message):
        text = message['message']['text']
        user = message['message']['from']['first_name']
        id_chat = message['message']['chat']['id']
        id_update = message['update_id']

        return id_chat, user, text, id_update

    def update(self, last_message):
        request = requests.get(URL + 'getUpdates?offset=' + str(last_message) + "&timeout=" + str(100))
        message_js = request.content.decode('UTF-8')
        messages = json.loads(message_js)
        return messages

    def send_message(self, id, text):
        requests.get(URL + 'sendMessage?text=' + text + '&chat_id=' + str(id))