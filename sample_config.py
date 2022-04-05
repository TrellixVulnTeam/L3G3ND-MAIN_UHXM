import os


class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 19560819))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "3d084d3c5a5d90b8ffcb5ea105c9bb81")
    LEGEND_STRING = os.environ.get("LEGEND_STRING", "1AZWarzsBu4lB_-8BeeWWyYgTuGGIRt6kTc7kWNxfqtFk1QCgaiP2dPtPCqwynAZf2AbrHyNZLHPLwCBquub4DRG1tMsujL_a1NFQ2-b0cFR2rq3ySmC7Q_xrsmqIkTIMuu81_eUKT3LRwf5eEz_LDwD4cKYLdSfGVROY7204Zy6ElT8OPQtPjKZ0DMcdijWtmFnAX9xdS7LUNT4rOtNMHxcvznKWkyuNiXdCEmRxWo8DDer8rXEiwQb1EbLAkg7TYbgA6TBIgdrBSjwqVNwasUO-Qcxg7RUk-2QVjemKxCdVtCqQ3nKrTnfFYARHBqg4RJSnuSb5fijvLRhjsg1cxRm2bAZxdFE=")
    DB_URI = os.environ.get("DATABASE_URL", )
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    WHITELIST_USERS = set(int(x) for x in os.environ.get("WHITELIST_USERS", "").split())
    BLACKLIST_USERS = set(int(x) for x in os.environ.get("BLACKLIST_USERS", "").split())
    DEVLOPERS = set(int(x) for x in os.environ.get("DEVLOPERS", "").split())
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5049168988").split())
    SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL", -752681387)
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5290293392:AAHCgAZSK7yq6Nz3Cuv2jqv15KkxUXOlJM0")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "rootubbot")
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    PM_PERMIT_GROUP_ID = os.environ.get("PM_PERMIT_GROUP_ID", -752681387)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
        t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", -752681387)
    if PRIVATE_GROUP_ID != None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )


class Development(Var):
    LOGGER = True
