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
    test_comments_file = open("test_comments.json", "r")
    test_comments = json.load(test_comments_file)

    for test_comment in test_comments:
        comment = Comment(test_comment["author"], test_comment["body"])

        hellothere.process_submission(comment)


test_comments()