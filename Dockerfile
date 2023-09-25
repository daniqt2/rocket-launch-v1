FROM python:3.8 AS bot
COPY requirements.txt /app/
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python3 bot.py  --hostname 0.0.0.0 --port $PORT