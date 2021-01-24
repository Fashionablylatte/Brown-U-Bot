import post_scripts.reddit as rd


def main():
    reddit = rd.get_reddit_instance("config.ini")
    # reddit.subreddit("test").submit("Test Submission", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    subreddit = reddit.subreddit("test")  # TODO remove hard-coding
    for comment in subreddit.stream.comments(skip_existing=True):
        resp = rd.process_comment(comment.body)
        if resp != "":  # TODO kinda sloppy
            comment.reply(resp)


if __name__ == '__main__':
    main()
