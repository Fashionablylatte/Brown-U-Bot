import post_scripts.reddit as rd


def main():
    reddit = rd.get_reddit_instance("config.ini")
    subreddit = reddit.subreddit(rd.get_subreddit("config.ini"))
    for comment in subreddit.stream.comments(skip_existing=True):
        resp = rd.process_comment(comment.body)
        if resp != "":  # TODO kinda sloppy
            comment.reply(resp)


if __name__ == '__main__':
    main()
