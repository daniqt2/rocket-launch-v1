FROM python:3.8 AS bot
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "bot.py", "--host", "0.0.0.0", "--port", "80"]