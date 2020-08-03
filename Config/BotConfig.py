import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "03c58a80-4810-4297-b1de-0d9f359873ff")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "ZWHmY36-Z5-27qwLE.7-Oqq51ygoK8XnVv")