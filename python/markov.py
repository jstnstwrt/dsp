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

from random import choice

text_file_path = "clinton.txt"
text_file = open(text_file_path, "r")
lines = text_file.readlines()
text = ''
for l in lines:
	text += ' ' + l.strip(chr(10))
words = text.strip().split()



order = 2
markov_dict = {}
for i, word in enumerate(words):
	if i + order < len(words):
		key = tuple(words[i:i+order])
		val = words[i+order]
		if key in markov_dict:
			markov_dict[key].append(val)
		else:
			markov_dict[key] = [val]




endings = {'.', '?', '!'}

def write_sentence(markov_dict):
	caps = [key for key in markov_dict.keys() if key[0][0].isupper()]
	sentence = []

	key = choice(caps)
	first, second = key

	sentence.append(first)
	sentence.append(second)
	while True:
	    third = choice(markov_dict[key])
	    sentence.append(third)
	    if third[-1] in endings:
	        break
	    key = (second, third)
	    first, second = key
	return ' '.join(sentence) , len(sentence)


def extend_text(max_length):
	text = ''
	text_length = 0
	while text_length < max_length:
		sentence, sentence_length = write_sentence(markov_dict)
		text += ' ' + sentence
		text_length +=  sentence_length

	return text.strip()













def main(text_file_path, num_of_words):
	pass
