#!/bin/python3

import random

def generator(text, sep=" ", option=None):
	'''Splits the text using the sep and yields the substrings.
	option indicates whether some action should be performed on the string before yielding it'''



	if not isinstance(text, str) or not isinstance(sep, str):
		yield "ERROR"
		return
	text = text.split(sep)
	if (option == "unique"):
		text1 = []
		[text1.append(word) for word in text if word not in text1]
		text = text1
	elif option == "ordered":
		text = sorted(text)
	elif option == "shuffle":
		l = []
		i = 0
		length = len(text)
		while i < length:
			v = random.randint(0, length)
			if v not in l:
				l.append(v)
				i += 1
			else:
				continue
		text = [text[e] for e in l]
	elif option == None:
		pass
	else:
		yield "ERROR"
		return

	for word in text:
		yield word
