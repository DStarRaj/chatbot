from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

class Chatter():
    def __init__(self) -> None:
        self.chatbot = ChatBot('Export Example Bot')
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train('chatterbot.corpus.english')

    def resp(self, a) -> str:
        return str(self.chatbot.get_response(a))