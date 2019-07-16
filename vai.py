#importing library
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#derfining name for chatbot and setting trainer
bot=ChatBot('vaishu')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/Home/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('C:/Users/Home/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)

while True:
    message=input('you:')
    if message.strip!='Bye' or message.strip!='bye':
        reply=bot.get_response(message)
        print('Chatbot:',reply)
        
    if message.strip=='Bye' or message.strip=='bye':
        print('Chatbot:It was nice taking to you')
        break
        
