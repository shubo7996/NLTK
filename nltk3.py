from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

Example_words = ["ride","riding","rode", "ridden"]

for w in Example_words:
    print (ps.stem(w))

    
