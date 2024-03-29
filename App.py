from flask import Flask, request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext, ConversationState, MemoryStorage
from botbuilder.schema import Activity
import asyncio
import os
from QnA import QnABOT
from Config.BotConfig import DefaultConfig

app = Flask(__name__)
loop = asyncio.get_event_loop()
BOTconfig = DefaultConfig()
#botsettings = BotFrameworkAdapterSettings(BOTconfig.APP_ID, BOTconfig.APP_PASSWORD)
botsettings = BotFrameworkAdapterSettings("","")
botadapter = BotFrameworkAdapter(botsettings)

CONMEMORY = ConversationState(MemoryStorage())
botdialog = QnABOT()

@app.route("/api/messages", methods=["POST"])
def messages():
    if "application/json" in request.headers["content-type"]:
        body = request.json
    else:
        return Response(status=415)

    activity = Activity().deserialize(body)

    auth_header = (request.headers["Authorization"] if "Authorization" in request.headers else "")

    async def call_fun(turncontext):
        await botdialog.on_turn(turncontext)

    task = loop.create_task(
        botadapter.process_activity(activity, auth_header, call_fun)
    )
    loop.run_until_complete(task)



if __name__ == '__main__':

    app.run()
