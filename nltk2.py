from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = " hey maa, i'm coming home"
stop_words = set(stopwords.words("english"))

print(stop_words)