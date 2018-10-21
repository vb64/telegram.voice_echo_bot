"""
This script demonstrate usage of Yandex SpeechCloud API by Telegram bot.
"""
import logging
import md5
from xml.etree import ElementTree
import requests
from telebot import TeleBot, logger, apihelper
from settings import TELEGRAM_KEY, YANDEX_KEY, VOICE_LANGUAGE, MAX_MESSAGE_SIZE, MAX_MESSAGE_DURATION

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
          "Maximum duration: {} sec.".format(MAX_MESSAGE_DURATION),
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

apihelper.CONNECT_TIMEOUT = 15
logger.setLevel(logging.DEBUG)
bot.polling()
