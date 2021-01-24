import praw
import utils.config as cf
import data_pull as dp


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
        tb = dp.pull("RI")
        message = f"| | Total Deaths | Increase in Deaths | Infected | Increase in Infected |\n" \
                  f"| --- | --- | --- | --- | --- |\n" \
                  f"| Current | {tb['total_deaths']} | {tb['inc_deaths']} | {tb['infected']} " \
                  f"| {tb['inc_infected']} |\n"\
                  f"| 5 Day | {tb['5_day_deaths']}|{tb['5_day_inc_deaths']}|{tb['5_day_infected']}" \
                  f"|{tb['5_day_inc_infected']}|\n" \
                  f"| 10 Day | {tb['10_day_deaths']}|{tb['10_day_inc_deaths']}|{tb['10_day_infected']}" \
                  f"|{tb['10_day_inc_infected']}|"
        return message
    else:
        return ""


def get_subreddit(config_filepath):
    return cf.get_subreddit(config_filepath)
