import praw
import time
import random
import json
import re

memes_file = open("memes.json", "r")
memes = json.load(memes_file)


def main():
    reddit = praw.Reddit(client_id='CLIENT_ID',
                         client_secret='CLIENT_SECRET',
                         user_agent='hellothere-bot-useragent',
                         username='REDDIT_USER',
                         password='REDDIT_PASS')

    subreddit = reddit.subreddit('all')

    for comment in subreddit.stream.comments():
        process_submission(comment)


def process_submission(comment):

    # Don't reply to own comments
    if comment.author != "ThePrequelMemesBot":

        # Check for exact matches
        for meme in memes["exact"]:
            p = re.compile(meme["pattern"], re.I)
            m = p.match(comment.body)
            
            if m:
                print(meme["message"])
                print("reddit.com" + comment.permalink)
                time.sleep(1)
                # Choose answer randomly if mulitple answers
                reply_len = len(meme["reply"])
                if reply_len > 1:
                    comment.reply(meme["reply"][random.randint(0, reply_len - 1)])
                else:
                    comment.reply(meme["reply"][0])


if __name__ == '__main__':
    main()
