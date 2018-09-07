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

    SLEEP_TIME = 1

    # Don't reply to own comments
    if comment.author != "ThePrequelMemesBot":

        # Check for exact matches
        for meme in memes["exact"]:
            m = re.match(meme["pattern"], comment.body, re.I)
            
            if m:
                print(meme["message"])
                print("reddit.com" + comment.permalink)
                time.sleep(SLEEP_TIME)
                
                # Choose answer randomly if mulitple answers
                reply_len = len(meme["reply"])
                if reply_len > 1:
                    comment.reply(meme["reply"][random.randint(0, reply_len - 1)])
                else:
                    comment.reply(meme["reply"][0])

                return True

        # Check for partial matches
        for meme in memes["partial"]:
            for pattern in meme["pattern"]:

                if all(pattern in comment.body for pattern in meme["pattern"]):

                    print(meme["message"])
                    print("reddit.com" + comment.permalink)
                    time.sleep(SLEEP_TIME)

                    # Choose answer randomly if multiple answers
                    reply_len = len(meme["reply"])
                    if reply_len > 1:
                        comment.reply(meme["reply"][random.randint(0, reply_len - 1)])
                    else:
                        comment.reply(meme["reply"][0])

                    return True

        return False


if __name__ == '__main__':
    main()
