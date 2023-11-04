FROM python:3

EXPOSE 443

RUN git clone https://github.com/ESIBot-etsi/TelegramBot.git /telegram_bot

WORKDIR /telegram_bot

RUN pip install -r /telegram_bot/requirements.txt

CMD [ "python3", "/telegram_bot/main.py" ]
