import random
import string
import json
import hellothere

class Comment:
	def __init__(self, author, body):
		self.author = author
		self.body = body
		self.permalink = "/" + ''.join(random.choice(string.ascii_lowercase) for x in range(10))

	def reply(self, message):
		print(message)


def test_comments():
	pass

