from telebot import TeleBot, types
from flask import Flask, request
from os import environ
from google.cloud import secretmanager


# Create the Secret Manager client.
client = secretmanager.SecretManagerServiceClient()
# Access the secret.
secret = client.access_secret_version(request={
    "name": f"projects/{environ['PROJECT_ID']}/secrets/MUB_TOKEN/versions/latest"
})
# Get bot token from secret payload.
BOT_TOKEN = secret.payload.data.decode("UTF-8")
# Instantiate the bot.
bot = TeleBot(BOT_TOKEN, parse_mode="HTML")
# Instantiate the Flask app.
app = Flask(__name__)


# Message handlers
import mockuserbot.handlers


@app.route('/' + BOT_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"{environ['GAE_URL']}" + BOT_TOKEN)
    return "!", 200
