import md5
import requests
from xml.etree import ElementTree
from telebot import TeleBot

TELEGRAM_KEY = 'YOUR_BOT_TOKEN_HERE'
YANDEX_KEY = 'YOUR_SpeechKit_Cloud_KEY__HERE'

MAX_MESSAGE_SIZE = 1000 * 50
MAX_MESSAGE_DURATION = 15

# https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-overview-technology-recogn-docpage/
# ru-RU, en-US, uk-UK, tr-TR
VOICE_LANGUAGE = 'ru-RU'

try:
    from api_key import telegram as TELEGRAM_KEY, yandex as YANDEX_KEY
except:
    pass

requests.packages.urllib3.disable_warnings()
bot = TeleBot(TELEGRAM_KEY)


@bot.message_handler(commands=['start'])
def start_prompt(message):
    reply = ' '.join((
      "Press and hold screen button with microphone picture.",
      "Say your phrase and release the button.",
    ))
    return bot.reply_to(message, reply)


@bot.message_handler(content_types=['voice'])
def echo_voice(message):
    d = message.voice
    if (d.file_size > MAX_MESSAGE_SIZE) or (d.duration > MAX_MESSAGE_DURATION):
        reply = ' '.join((
          "The voice message is too big.",
          "Try to speak in short.",
        ))
        return bot.reply_to(message, reply)

    file_url = "https://api.telegram.org/file/bot{}/{}".format(
      bot.token,
      bot.get_file(d.file_id).file_path
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

    e = ElementTree.fromstring(xml_data)
    if not int(e.attrib.get('success', '0')):
        return bot.reply_to(message, "ERROR: {}".format(xml_data))

    text = e[0].text

    if ('<censored>' in text) or (not text):
        return bot.reply_to(message, "Don't understand you, please repeat.")

    bot.reply_to(message, text)


bot.polling()
