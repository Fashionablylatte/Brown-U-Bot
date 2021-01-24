import configparser as cp


def get_oauth(file_path):
    """
    Gets the oauth information from the configuration file.
    :param file_path: a config file of the format .ini
    :return: the oauth requirements as a n-tuple.
    """
    config = cp.ConfigParser()
    config.read(file_path)
    client_id = config['OAUTH']['client_id']
    client_secret = config['OAUTH']['client_secret']
    password = config['OAUTH']['password']
    user_agent = config['OAUTH']['user_agent']
    username = config['OAUTH']['username']
    return client_id, client_secret, password, user_agent, username


def get_subreddit(file_path):
    """
    Gets the subreddit parameter from the configuration file.
    :param file_path: a config file of the format .ini
    :return: the subreddit as a string.
    """
    config = cp.ConfigParser()
    config.read(file_path)
    sub = config['OTHER']['subreddit']
    return sub


def get_state(file_path):
    """
    Gets the state parameter from the configuration file.
    :param file_path: a config file of the format .ini
    :return: the US state abbreviation as a string.
    """
    config = cp.ConfigParser()
    config.read(file_path)
    st = config['OTHER']['state']
    web = config['OTHER']['web']
    return st, web


def get_user(file_path):
    """
    Gets the username parameter from the configuration file.
    :param file_path: a config file of the format .ini
    :return: the username as a string.
    """
    config = cp.ConfigParser()
    config.read(file_path)
    un = config['OAUTH']['username']
    return un
