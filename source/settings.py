"""Settings for Telegram bot, that used Yandex SpeechCloud API. """
TELEGRAM_KEY = 'YOUR_BOT_TOKEN_HERE'
YANDEX_KEY = 'YOUR_SpeechKit_Cloud_KEY_HERE'

# https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-overview-technology-recogn-docpage/
# Language code for speech recognition. You can use: ru-RU, en-US, uk-UK, tr-TR
VOICE_LANGUAGE = 'ru-RU'

MAX_MESSAGE_SIZE = 1000 * 50  # in bytes
MAX_MESSAGE_DURATION = 15  # in seconds
