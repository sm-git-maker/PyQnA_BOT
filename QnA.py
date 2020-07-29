from botbuilder.core import TurnContext, ActivityHandler, MessageFactory
from botbuilder.ai.qna import  QnAMaker, QnAMakerEndpoint

class QnABOT(ActivityHandler):
    def __init__(self):
        qna_Endpoint = QnAMakerEndpoint("3034c004-bd79-478a-9ede-52febd8f0763","2831d414-42df-4359-b3c0-655b81d1b9ee","https://ohs-faq.azurewebsites.net/qnamaker")
        self.qna_maker = QnAMaker(qna_Endpoint)

    async def on_message_activity(self, turn_context: TurnContext):
        response = await self.qna_maker.get_answers(turn_context)
        if response and len(response) > 0:
            await turn_context.send_activity(MessageFactory.text(response[0].answer))


