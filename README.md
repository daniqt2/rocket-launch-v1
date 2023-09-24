# When did the rocket launch?

This proyect is a Telegram Bot that uses the bisection method to "guess" the exact frame a rocket lauched based on user input.

- API : https://framex-dev.wadrid.net/api/video/

# LIVE DEMO

You can try it out by intiating a conversation with `@rocket_launch_guess_bot` on Telegram

(Webhook is set to point to server)
I'll provide a BOT_TOKEN so you can test in develop with `@@rocket_launch_dq_bot`

(This could be solved if I used the setWebhook on the running app, didn't have time to test it and I had a lot of trouble deploying this proyect.)

# How to run

You will need **virtualenv** to be able to start the virtual environment.
Inside folder:

- `source venv/bin/activate ` // activates
- `python3 -m pip install -r requirements.txt ` // install requirements
- `python bot.py` // run
