import praw
import utils.config as cf


def get_reddit_instance(config_filepath):
    """
    Gets a PRAW reddit instance.
    :return: a reddit instance.
    """
    client_id, client_secret, password, user_agent, username = cf.get_oauth(config_filepath)
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=user_agent,
                         username=username)
    return reddit


def process_comment(comment_body):
    if "!c19data" in comment_body:
        return "Placeholder message."
    else:
        return ""



