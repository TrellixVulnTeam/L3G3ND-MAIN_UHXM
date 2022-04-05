import os

from sample_config import Var


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 19560819
  API_HASH = "3d084d3c5a5d90b8ffcb5ea105c9bb81"

  # the name to display in your alive message.
  # If not filled anything then default value is LEGEND User.
  ALIVE_NAME = "LEGEND User"

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "Your value"

  # After cloning the repo and installing requirements...
  # Do python string_session.py and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  LEGEND_STRING = "1AZWarzsBu4lB_-8BeeWWyYgTuGGIRt6kTc7kWNxfqtFk1QCgaiP2dPtPCqwynAZf2AbrHyNZLHPLwCBquub4DRG1tMsujL_a1NFQ2-b0cFR2rq3ySmC7Q_xrsmqIkTIMuu81_eUKT3LRwf5eEz_LDwD4cKYLdSfGVROY7204Zy6ElT8OPQtPjKZ0DMcdijWtmFnAX9xdS7LUNT4rOtNMHxcvznKWkyuNiXdCEmRxWo8DDer8rXEiwQb1EbLAkg7TYbgA6TBIgdrBSjwqVNwasUO-Qcxg7RUk-2QVjemKxCdVtCqQ3nKrTnfFYARHBqg4RJSnuSb5fijvLRhjsg1cxRm2bAZxdFE="

  # Create a bot in @botfather and fill the following values with bot token and username.
  BOT_TOKEN = "5290293392:AAHCgAZSK7yq6Nz3Cuv2jqv15KkxUXOlJM0" #token
  BOT_USERNAME = "rootubbot" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  PRIVATE_GROUP_BOT_API_ID = -752681387

  # Custom Command Handler. 
  COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\."
  #User Command Handler
  HANDLER = os.environ.get("COMMAND_HAND_LER", r"\."
  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = []

  # command hanler for sudo users.
  SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\,"
