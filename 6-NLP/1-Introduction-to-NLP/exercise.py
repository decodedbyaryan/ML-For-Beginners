# Importing the required library to python
import random

# list of pre-fed random responses for the bot
random_responses = [
    "That is quite interesting, please tell me more.",
    "I see. Do go on.",
    "Why do you sat that?",
    "Funny weather we've been having, isn't it?",
    "Let's change the subject.",
    "Did you catch the game last night?"
]

# robot introduction and rules
print(
"""Hello, I am Marvin, the simple robot.
You can end this conversation at any time by typing 'bye'
After typing each answer, press 'enter' 
    
How are you today?"""
)

# the loop at work
while True:
    user_input = input(">>> ")
    if user_input.lower() == "bye":
        print("It was nice talking to you, goodbye!")
        break 
    else:
        print(random.choice(random_responses))