# Importing the tool TextBlob from the library textblob
from textblob import TextBlob

# Assigning the variable blob to the TextBlob+the_statement
# Follwoed by printing the variable alongside noun_phrase property of text blob
# which allows it to identify nouns
blob = TextBlob("I have the hightest respect for your nerves, they are my old friends.")
print(blob.noun_phrases)

# using the property of textblob, sentiment and sentiment.polarity
# to find the sentiment and the extent of polarity in the sentance
print(blob.sentiment)
print(blob.sentiment.polarity)