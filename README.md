# When did the rocket launch?

This proyect is a Telegram Bot that uses the bisection method to "guess" the exact frame a rocket lauched based on user input.

- API : https://framex-dev.wadrid.net/api/video/
- Telegram API used: https://pypi.org/project/pyTelegramBotAPI/

# LIVE DEMO

You can try it out by intiating a conversation with `@rocket_launch_guess_bot` on Telegram

(Webhook is set to point to server)
I'll provide a BOT_TOKEN so you can test in develop with `@@rocket_launch_dq_bot`

(This could be solved if I used the setWebhook on the running app, didn't have time to test it and I had a lot of trouble deploying this proyect.)

# How to run

### virtualenv

You will need **virtualenv** to be able to start the virtual environment.
Inside folder:

- `source venv/bin/activate ` // activates
- `python3 -m pip install -r requirements.txt ` // install requirements
- `python bot.py` // run

### DOCKER

- `docker-compose up -d` // this will launch the container, if you have the correct BOT_TOKEN it will run

# Mantainability

- Al functions are documented so that their goal is clear.
- Code is divided into different files (each one of them is focused on a type of task) and each file has its own small functions (again, each one of them focuses in a small task).
- clear names for all variables and functions
