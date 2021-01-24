import praw
import utils.config as cf
import data_pull as dp
import utils.constants as constants


def get_reddit_instance(config_filepath):
    """
    Gets a PRAW reddit instance.
    :return: a reddit instance.
    """
    client_id, client_secret, password, user_agent, username = cf.get_oauth(config_filepath)
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=user_agent,
                         username=username)
    return reddit


def process_comment(comment, config_filepath):
    """
    Processes a Reddit comment.
    :param comment: a PRAW comment object.
    :param config_filepath: a config file of the format .ini
    :return: a string message, or empty string, depending on if the message should trigger a response.
    """
    if comment.author.name == cf.get_user(config_filepath):
        return ""
    elif check_keywords(comment.body):
        state, state_web = cf.get_state(config_filepath)
        tb = dp.pull(state)
        message = f"## Cumulative Covid-19 Statistics for {state}\n" \
                  f"| | Total Deaths | Increase in Deaths | Infected | Increase in Infected |\n" \
                  f"| --- | --- | --- | --- | --- |\n" \
                  f"| Current | {tb['total_deaths']} | {tb['inc_deaths']} | {tb['infected']} " \
                  f"| {tb['inc_infected']} |\n"\
                  f"| 5 Day | {tb['5_day_deaths']}|{tb['5_day_inc_deaths']}|{tb['5_day_infected']}" \
                  f"|{tb['5_day_inc_infected']}|\n" \
                  f"| 10 Day | {tb['10_day_deaths']}|{tb['10_day_inc_deaths']}|{tb['10_day_infected']}" \
                  f"|{tb['10_day_inc_infected']}|\n" \
                  f"### Please stay safe by exercising sound judgement and following all health authority advisories! "\
                  f"For more information, see [{state_web}]({state_web}). Note that all data may be provisional."
        return message
    else:
        return ""


def check_keywords(content):
    """
    Checks a message for any keywords.
    :param content: the message to check.
    :return: a boolean, True if there are any keywords.
    """
    words = content.lower().split()
    for w in words:
        if w in constants.KEYWORDS:
            return True
    return False
