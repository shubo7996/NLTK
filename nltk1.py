from nltk.tokenize import sent_tokenize, word_tokenize

#nltk.download()

#tokenizers

#word tokenizer - seperating by word
#sentence tokenizer - seperated by sentences

#lexicon and corporas
#corpora - body of text ex: presenditial speech, a paragraph from your book.
#lexicon - word and their mean (dictionary)
#words with dual meaning depending on the sentence

example_text = "The sky was tuned to the color of the dead televison. hello darkness, my old friend. i've come to talk to you gain."
print (sent_tokenize(example_text))
print (word_tokenize(example_text))

