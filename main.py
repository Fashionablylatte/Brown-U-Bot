import post_scripts.reddit as rd
from utils.constants import CONFIG_FILEPATH
import praw
import time


def main():
    while True:
        try:
            reddit = rd.get_reddit_instance(CONFIG_FILEPATH)
            subreddit = reddit.subreddit(rd.get_subreddit(CONFIG_FILEPATH))
            for comment in subreddit.stream.comments(skip_existing=True):
                resp = rd.process_comment(comment, CONFIG_FILEPATH)
                if resp != "":
                    comment.reply(resp)
        except praw.exceptions.RedditAPIException as rae:
            for subexec in rae.items:
                if subexec.error_type.lower() == 'ratelimit':
                    print(subexec.message)
                    for t in subexec.message.split():
                        try:
                            stime = int(t)
                            time.sleep(stime * 60)
                            break
                        except ValueError:
                            pass
                else:
                    raise SystemExit


if __name__ == '__main__':
    main()
