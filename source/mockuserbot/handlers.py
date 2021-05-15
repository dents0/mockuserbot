from mockuserbot import app, bot, BOT_TOKEN
from randomuser import RandomUser


@bot.message_handler(commands=['start'])
def handle_command(message):
    """ Sends welcome-message on start """
    bot.send_message(message.chat.id, "Greetings! Please see the list of commands to generate the data you need.")


@bot.message_handler(commands=['user'])
def handle_command(message):
    """ Generate full user profile """
    user = RandomUser()
    bot.send_photo(message.chat.id, user.get_picture())
    bot.send_message(message.chat.id, f"""
<b>Full Name:</b> <i>{user.get_full_name()}</i>
<b>DoB:</b> <i>{user.get_dob()[:10]}</i>
<b>Address:</b>
  <i>{user.get_street()},
  {user.get_city()}
  {user.get_zipcode()}
  {user.get_state()}, {user.get_country()}</i>
""")


@bot.message_handler(commands=['name'])
def handle_command(message):
    """ Generate full name """
    user = RandomUser()
    bot.send_message(message.chat.id, user.get_full_name())


@bot.message_handler(commands=['dob'])
def handle_command(message):
    """ Generate date of birth  """
    user = RandomUser()
    bot.send_message(message.chat.id, user.get_dob()[:10])


@bot.message_handler(commands=['address'])
def handle_command(message):
    """ Generate address  """
    user = RandomUser()
    bot.send_message(message.chat.id, f"""
{user.get_street()},
{user.get_city()}
{user.get_zipcode()}
{user.get_state()}, {user.get_country()}
""")


@bot.message_handler(commands=['pic'])
def handle_command(message):
    """ Generate profile picture """
    user = RandomUser()
    bot.send_photo(message.chat.id, user.get_picture())


@bot.message_handler(commands=['link'])
def handle_command(message):
    """ Link to the bot """
    bot.send_message(message.chat.id, "https://t.me/mockuserbot")
    