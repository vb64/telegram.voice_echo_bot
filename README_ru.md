# telegram.voice_echo_bot
Пример использования [Yandex SpeechKit Cloud](https://developer.tech.yandex.ru) и библиотеки [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI). Вы отправляете голосовое сообщение боту Telegram, а он в ответ присылает вам текст этого сообщения.

## Предварительные требования
* [Python 2.x](https://www.python.org/downloads/release/python-2714/). Если не установлен, нужно скачать и установить.
* Токен и username вашего бота в Telegram Bot API. Для получения токена нужно открыть диалог Telegram с ботом [@BotFather](https://t.me/botfather) и сделать несколько шагов (описанных [здесь](https://core.telegram.org/bots#6-botfather)).
* Ваш ключ в Yandex SpeechKit Cloud API. Для получения ключа вам нужно зарегистрироваться на [SpeechKit Cloud](https://developer.tech.yandex.ru).

## Установка
[Скачайте архив исходников](https://github.com/vb64/telegram.voice_echo_bot/archive/master.zip) и распакуйте в каталог `telegram.voice_echo_bot`. Или
```
git clone https://github.com/vb64/telegram.voice_echo_bot
```
Затем
```
cd telegram.voice_echo_bot
sudo python -m pip install -r requirements.txt
```
Затем отредактируйте файл `source/settings.py` и укажите ваш токен Telegram Bot API в ключе `TELEGRAM_KEY`:
```
TELEGRAM_KEY = 'YOUR_BOT_TOKEN_HERE'
```
Укажите ваш ключ Yandex SpeechKit Cloud API в ключе `YANDEX_KEY`:
```
YANDEX_KEY = 'YOUR_SpeechKit_Cloud_KEY_HERE'
```

В файле `source/settings.py` также можно настроить:
* максимальную продолжительность голосового сообщения в секундах (ключ `MAX_MESSAGE_DURATION`)
* максимальный размер голосового сообщения в байтах (ключ `MAX_MESSAGE_SIZE`)
* язык для распознавания голоса. Поддерживаются английский, русский, украинский и турецкий языки. (ключ `VOICE_LANGUAGE`)

Сохраните файл `source/settings.py` для завершения установки.

## Использование
```
python source/voice_echo.py
```
Ваш бот запустится. Вы можете взаимодействовать с ним в любом клиенте Telegram. Напечатайте в поле поиска клиента username вашего бота и начните диалог с ним. Username бота это строка, которую вы указали при регистрации бота в диалоге с BotFather.

Для остановки работы бота нажмите Ctrl+C.
