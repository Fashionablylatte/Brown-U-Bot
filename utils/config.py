import configparser as cp


def get_oauth(file_path):
    """
    Gets the oauth information from the configuration files.
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
    config = cp.ConfigParser()
    config.read(file_path)
    sub = config['OTHER']['subreddit']
    return sub
