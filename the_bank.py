#!/bin/python3

class Account:

	ID_COUNT = 1

	def	__init__(self, name, **kwargs):

		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount

class Bank:
	def __init__(self):
		self.accounts = []

	def _check(self, account):
		if not isinstance(account, Account):
			raise TypeError("Invalid account")

		attrs = list(vars(account).items())
		if len(attrs) % 2 == 0:
			return False

		check = {'id': 0,'name': 0, 'value':0, 'zip':0, 'addr':0}

		for a in attrs:
			if a[0] == 'name':
				if not isinstance(a[1], str):
					return False
				check['name'] += 1

			elif a[0] == 'id':
				if not isinstance(a[1], int):
					return False
				check['id'] += 1
			elif a[0] == 'value':
				if not isinstance(a[1], int) and not isinstance(a[1], float):
					return False
				check['value'] += 1
			elif a[0].startswith('zip'):
				check['zip'] += 1
			elif a[0].startswith('addr'):
				check['addr'] += 1
			elif a[0].startswith('b'):
				return False

		for element in check:
			if check[element] == 0:
				return False

		self.accounts.append(account)
		return True

	def add(self, new_account):
		if not isinstance(new_account, Account):
			raise TypeError("Invalid account")

		if new_account in self.accounts:
			print("Account already exists")
			return False

		re = self._check(new_account)
		return re

	def transfer(self, origin, dest, amount):
		if self._check(origin) and self._check(dest) and amount > 0 and origin.value >= amount:
				origin.value -= amount
				dest.transfer(amount)
		else:
			return False

	def fix_account(self, name):

		check = ['id', 'value', 'zip', 'addr']
		for e in self.accounts:
			if e.name == name:
				break
		if e.name != name:
			return False
		if self._check(e):
			return False

		a = dir(e)
		for element in a:
			if element == "zip":
				check.remove("zip")
			elif element == "addr":
				check.remove("addr")
			elif element == "id":
				check.remove("id")
			elif element == "value":
				check.remove("value")
			elif element.startswith("b"):
				del e.element

		for key in check:
			if key == "zip" or key == "addr":
				setattr(e, key, key + "_default")
			else:
				setattr(e, key, 0)

		return True
