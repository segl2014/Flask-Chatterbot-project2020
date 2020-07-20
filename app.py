#imports
from flask import Flask, render_template, request
from chatterbot import chatBot
from chatterbot.trainers import chatterBotChatbotTrainer

app = Flask(__name__)

#create chatbot
english_bot = chatBot("chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = chatterBotChatbotTrainer(english_bot)
trainer.train("chatterbot.chatbot.english") #train the chatter bot for english

#define app routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

if __name__ == "__main__":
    app.run()
