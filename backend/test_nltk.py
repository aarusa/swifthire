import nltk
# nltk.download('punkt_tab')

text = "Hi, I am Arusha. I am learning NLTK."
sentences = nltk.sent_tokenize(text)

text2 = "Hi, this is fun."
words = nltk.word_tokenize(text2)

print(sentences)
print(words)