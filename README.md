# telegram.voice_echo_bot
Example of usage [Yandex SpeechKit Cloud](https://developer.tech.yandex.ru) with [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) library. You send a voice message to Telegrambot bot, and bot sends you the text of this message in reply.

## Requirements
* [Python 2.x](https://www.python.org/downloads/release/python-2714/). If it don't installed, please download and install.
* Telegram Bot API Access Token and username of your bot. To generate an Access Token, you have to talk to [@BotFather](https://t.me/botfather) and follow a few simple steps (described [here](https://core.telegram.org/bots#6-botfather)).
* Yandex SpeechKit Cloud API key. To obtain an API key, you need to register at [SpeechKit Cloud](https://developer.tech.yandex.ru)

## Installing
[Download source](https://github.com/vb64/telegram.voice_echo_bot/archive/master.zip) and unpack to `telegram.voice_echo_bot` directory. Or
```
git clone https://github.com/vb64/telegram.voice_echo_bot
```
Then
```
cd telegram.voice_echo_bot
sudo python -m pip install -r requirements.txt
```
Then edit `source/settings.py` and put your Telegram Bot API Access Token to the `TELEGRAM_KEY` key:
```
TELEGRAM_KEY = 'YOUR_BOT_TOKEN_HERE'
```
Put your Yandex SpeechKit Cloud API key to the `YANDEX_KEY` key:
```
YANDEX_KEY = 'YOUR_SpeechKit_Cloud_KEY_HERE'
```

In `source/settings.py` file you can also set up:
* maximum voice message duration in seconds (`MAX_MESSAGE_DURATION` key)
* maximum voice message size in bytes (`MAX_MESSAGE_SIZE` key)
* language for voice recognition. English, Russian, Ukraine and Turkey are supported. (`VOICE_LANGUAGE` key)

Save `source/settings.py` file to complete installation.

## Usage
```
python source/voice_echo.py
```
Your bot starts. Now you can talk with bot in any Telegram client. Type in search field of Telegram client an username of your bot and start conversation. Username of the bot it's a string, that you specified when talking with Telegram BotFather.

To stop your bot, press Ctrl+C.
