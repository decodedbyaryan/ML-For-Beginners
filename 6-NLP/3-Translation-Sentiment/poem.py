## Assignment

## Pretext and Important update

# The original assignment wanted us to compare our TextBlob results with 
# the Azure output made available but because the orignial dataset which 
# was used in the Azure report wasn't available we are using another dataset
# containing the poems by the same author but as it is a different dataset
# we won't be comparing the results with the Azure dataset but rather stating 
# our own human observation instated.

# importing TextBlob from textblob library
from textblob import TextBlob as tb

# opening and reading poems.txt
with open("poems.txt", "r", encoding="utf-8") as f:
    text = f.read()

# creating TextBlob object from the entire text
poems = tb(text)

# creating empty lists to store absolute positive and negative vurses
positive = []
negative = []

# looping through each line in the poem
for sentence in poems.sentences:
    # checking if polarity is absolutely positve
    if sentence.sentiment.polarity == 1:
        positive.append(str(sentence))
    # checking if polarity is absolutely negative
    if sentence.sentiment.polarity == -1:
        negative.append(str(sentence))

# printing the results out
print("Positive verses: ", len(positive))
for s in positive:
    print(s)

print("Negative verses: ", len(negative))
for s in negative:
    print(s)

## Observation

## RESULT or OUTPUT TextBlob
# -> Positive verses in the poem- 19
# -> Negative verses in the poem- 4

## Postive verse observation
# overall the results look pretty good but when we
# dive down deeper we see things that the results are
# not reflecting the right outcome 

# example- "A perfect, paralyzing bliss Contented as despair."

# This example above doesn't seem exactly positive but rather a negative experice
# or despair

## Negative verse observation
# Surprisingly this time it seemed like it was able to 
# detect polar negative verses without picking any positive
# verse in disguise, which is pretty impressive
# and tells us that tools like TextBlob can be pretty
# accurate if the input is straight to the point without
# any hidden meanings or sarcasm.