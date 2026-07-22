# importing class TextBlob from textblob library
from textblob import TextBlob

## Block 1- quote 1
# storing statement in quote as string aka str
quote = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."

# creating variable sentiment to analyze the statement
sentiment = TextBlob(quote).sentiment

#printing the output
print(quote + " has a sentiment of " + str(sentiment))

## Block 2- quote 2
# storing the quote in the variable quote2
quote2 = "Darcy, as well as Elizabeth, really loved them; and they were both ever sensible of the warmest gratitude towards the person who, by bringing her into Derbyshire, had been the means of uniting them."

# running TextBlob on quote2 to get things ready
# followed by .sentiment to analyze the statement immidiately 
sentiment2 = TextBlob(quote2).sentiment

# printing the result of .sentiment on quote2
print(quote2 + " has a sentiment of " + str(sentiment2))