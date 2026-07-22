# importing TextBlob from textblob library
from textblob import TextBlob as tb

# opening and reading pride.txt
with open("pride.txt", "r", encoding="utf-8") as f:
    text = f.read()

# creating a TextBlob object from the entire text
book = tb(text)

# creating empty lists to store positive and negative sentences
positive_sentences = []
negative_sentences = []

# looping through each sentence in the book
for sentence in book.sentences:
    #checking if polarity is absolutely positive
    if sentence.sentiment.polarity == 1:
        positive_sentences.append(str(sentence))
    # checking if polarity is absolutely negative
    if sentence.sentiment.polarity == -1:
        negative_sentences.append(str(sentence))

# printing results
print("Positive sentences:", len(positive_sentences))
for s in positive_sentences:
    print(s)

print("\nNegative sentances:", len(negative_sentences))
for s in negative_sentences:
    print(s)