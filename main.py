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

  def weather(self, data):
    """
      This event runs whenever the server has weather report ready for you
    """
    pass

  def news(self, data):
    """
      This event runs whenever server has the news ready for you
    """
    pass

  def speak(self, what_to_speak):
    """
      This events runs when ever the server wants you to say something
    """
    pass

  def de_activate_smith(self, data):
    """
      This events runs after S.M.I.T.H has been De-Activated and KS-BOT has been activated
    """
    pass

  def activate_smith(self, data):
    """
      This event runs after S.M.I.T.H has been activated
    """
    pass

# To create a user account go to https://www.kidssmit.com
bot = CustomBot("<your name>", "<your password>")
bot.run()
bot.send_command("Hello", log=True)