import ks_bot_client

class CustomBot(ks_bot_client.Bot):

  def __init__(self, name:str, password:str):
    """
      :param {string} name - Either Username, First Name of user or email of user
      :param {string} password - User password
    """

    super().__init__(name, password)


  def WelcomeMessage(self, data):
    """
      This event gives you, your previous messages with ks-bot.

      > Feel free to customize it
    """
    print("KS-BOT said 'welcome'")


  def BotProcessReply(self, data):
    """
      Returns bot reply to the message you sent it

      > Feel free to customize it
    """
    print("KS-BOT said: ", data)


  def TimerOver(self, data):
    """
      Handles Event Server sends when timer is over

      > Feel free to customize it
    """

    print("KS-BOT said: Timer is over, Timer: ", data)

# To create a user account go to https://www.kidssmit.com
bot = CustomBot("<your name>", "<your password>")
bot.run()
bot.send_command("Hello", log=True)