# telegram.voice_echo_bot
Example of usage [Yandex SpeechKit Cloud](https://developer.tech.yandex.ru) with [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) library.

## Requirements

* Python 2.x. If it don't installed, [download and install](https://www.python.org/downloads/release/python-2714/).
* Telegram Bot API Access Token and username of your bot. To generate an Access Token, you have to talk to [@BotFather](https://t.me/botfather) and follow a few simple steps (described [here](https://core.telegram.org/bots#6-botfather)).
* Yandex SpeechKit Cloud API key. To obtain an API key, you need to register at [SpeechKit Cloud](https://developer.tech.yandex.ru)

## Installing

```
git clone https://github.com/vb64/telegram.voice_echo_bot
cd telegram.voice_echo_bot
sudp python -m pip install -r requirements.txt
```
Then edit `source/voice_echo.py` and put your Telegram Bot API Access Token at the line 9 of the file:
```
TELEGRAM_KEY = 'YOUR_BOT_TOKEN_HERE'
```
Put your Yandex SpeechKit Cloud API key at the line 10 of the file:
```
YANDEX_KEY = 'YOUR_SpeechKit_Cloud_KEY__HERE'
```
And save `source/voice_echo.py` file. Installation complete.

## Usage
```
python source/voice_echo.py
```
Your bot starts. Now you can talk with bot in any Telegram client. Type in search field of Telegram client an username of your bot and start conversation.

Username of the bot it's a string, that you specified when talking with Telegram BotFather. To stop your bot, press Ctrl+C.
