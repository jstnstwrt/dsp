#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py).
# Your program should be called from the command line with two arguments: 
# the name of a file containing text to read, and the number of words to
# generate. For example, if `chains.txt` contains the short story by
# Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself
# playing our well-connected game went on. Our friend was absolutely correct:
# nobody from the group needed this way. We never been as the Earth has the
# network of eternity.

# There are design choices to make; feel free to experiment and shape the
# program as you see fit. Jeff Atwood's [Markov and You]
# (http://blog.codinghorror.com/markov-and-you/) 
# is a fun place to get started learning about what you're trying to make.


import pandas as pd

text_file_path = "COPYRIGHT.TXT"

text_file = open(text_file_path, "r")
lines = text_file.readlines()

text = ''
for l in lines:
	text += ' ' + l.strip(chr(10))

words = text.strip().split()


## parse the text file in to correct ngram order (order-2)

## create the probability table


for i in range(10):
	print tuple(words[i:i+2]), words[i+2]




## create a string of the desired length simply by choosing randomly 
## a traversal through the markov table


def main(text_file_path, num_of_words):
	pass
