"""
We are making and observing a better version of Marvin the
chatbot, which doesn't just respond with random output but 
tries to response according to the sentiment polarity detected
"""

# ---- Marvin Bot ----

# importing Textblob from textblob library
from textblob import TextBlob as tb

# printing out instructions for user
print("Hi, I am Marvin your friendly chat bot,\n" \
"Today I will chat with you and you can exit the chat anytime by saying bye\n" \
"The conversation will go on till you say bye, Happy Chatting")

# Getting the users input 
user_input = input("How are you today? ").lower()

# Checking the user input for bye or noun + sentimental polarity
# to respond accordingly
while True:
    if user_input == 'bye':
        break
    
    else:
        response = tb(user_input)
        items = response.noun_phrases
        
        # Statement Response
        if response.sentiment.polarity <= -0.5:
            print("Ohh, I am sorry! that's not good, please tell me more about it. ")
        elif response.sentiment.polarity <= 0.0:
            print("ahh, that sounds bad, do tell me more about it. ")
        elif response.sentiment.polarity <= +0.5:
            print("Hmm, interesting, I would love to hear more about this. ")
        else:
            print("WOW, that's wonderful, I would love to know more. ")

        # noun phrase check
        if items:
            for item in items:
                print(f"Can you tell me more about {item.pluralize()}?")


        user_input = input("> ").lower()
