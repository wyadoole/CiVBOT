from chatterbot import ChatBot # import so that the lobaraires can create chatbot
from chatterbot.trainers import ListTrainer # import for training chatbots on test data


#####################################################
############ Converstion of Chatbot #################
#### convesations that the Cjat bot uses to make ####
#####################################################

# test conversation [list]  to test and run with user response
conversation = [
    "Hello",
    "Hello There",
    "How are you doing?",
    "I'm doing great.",
    "Great to here",
    "Thank you.",
    "Good Morning",
    "Goodbye",
    "See you later",
]
trainer=ListTrainer(chatbot) #use the lise of statements to chatbot needs to be trained with
trainer.train(conversation)# uses the conversation list to train the chatbot

print("This application is a protype to test to see if Chatterbot works on the laptop")
while True: # while true that application runs
    user_response = input("Please type your response here: ")# user promt to type in what ever they want to say to chatbot
    print(chatbot.get_response(user_response))# prints the user response to the chatbot
    if user_response == "Goodbye": # only quits if the user inputs Goodbye for user_response
        break # application Quits

