import configparser as cp

def get_oauth(file_path):
    """
    Gets the oauth information from the configuration files.
    :param file_path: a config file of the format .ini
    :return: the oauth requirements as a n-tuple.
    """
    config = cp.ConfigParser()
    config.read(file_path)
    return