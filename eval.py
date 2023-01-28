#!/bin/python

class Evaluator:
	@staticmethod
	def zip_evaluate(words, coefs):
		if not isinstance(words, list) or not isinstance(coefs, list):
			raise TypeError("Words and coefs must be of type 'list'")
		if len(words) != len(coefs):
			return -1
		l = [len(i) * j for i, j in zip(words, coefs)]
		re = sum(x for x in l)
		return re

	@staticmethod
	def enumerate_evaluate(words, coefs):
		if not isinstance(words, list) or not isinstance(coefs, list):
			raise TypeError("Words and coefs must be of type 'list'")
		if len(words) != len(coefs):
			return -1
		l = [len(j) * coefs[i] for i, j in enumerate(words)]
		re = sum(x for x in l)
		return re
