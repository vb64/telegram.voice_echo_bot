"""
This script demonstrate usage of Yandex SpeechCloud API by Telegram bot.
"""
import md5
from xml.etree import ElementTree
import requests
from telebot import TeleBot

TELEGRAM_KEY = 'YOUR_BOT_TOKEN_HERE'
YANDEX_KEY = 'YOUR_SpeechKit_Cloud_KEY__HERE'

MAX_MESSAGE_SIZE = 1000 * 50  # in bytes
MAX_MESSAGE_DURATION = 15  # in seconds

# https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-overview-technology-recogn-docpage/
# ru-RU, en-US, uk-UK, tr-TR
VOICE_LANGUAGE = 'ru-RU'
bot = TeleBot(TELEGRAM_KEY)  # pylint: disable=invalid-name


@bot.message_handler(commands=['start'])
def start_prompt(message):
    """Print prompt to input voice message.
    """
    reply = ' '.join((
      "Press and hold screen button with microphone picture.",
      "Say your phrase and release the button.",
    ))
    return bot.reply_to(message, reply)


@bot.message_handler(content_types=['voice'])
def echo_voice(message):
    """Voice message handler.
    """
    data = message.voice
    if (data.file_size > MAX_MESSAGE_SIZE) or (data.duration > MAX_MESSAGE_DURATION):
        reply = ' '.join((
          "The voice message is too big.",
          "Try to speak in short.",
        ))
        return bot.reply_to(message, reply)

    file_url = "https://api.telegram.org/file/bot{}/{}".format(
      bot.token,
      bot.get_file(data.file_id).file_path
    )

    xml_data = requests.post(
      "https://asr.yandex.net/asr_xml?uuid={}&key={}&topic={}&lang={}".format(
        md5.new(str(message.from_user.id)).hexdigest(),
        YANDEX_KEY,
        'queries',
        VOICE_LANGUAGE
      ),
      data=requests.get(file_url).content,
      headers={"Content-type": 'audio/ogg;codecs=opus'}
    ).content

    e_tree = ElementTree.fromstring(xml_data)
    if not int(e_tree.attrib.get('success', '0')):
        return bot.reply_to(message, "ERROR: {}".format(xml_data))

    text = e_tree[0].text

    if ('<censored>' in text) or (not text):
        return bot.reply_to(message, "Don't understand you, please repeat.")

    return bot.reply_to(message, text)


bot.delete_webhook()  # just in case
bot.polling()
