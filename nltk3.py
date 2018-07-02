from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

Example_words = ["egg","egglet","eggy", "eggzy"]

for w in Example_words:
    print (ps.stem(w))
    
