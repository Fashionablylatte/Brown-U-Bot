# Brown-U-Bot
A bot intended to be used on the r/BrownU subreddit. Currently provides rudimentary information about RI Covid-19 
statistics whenever it detects a Covid-19 related keyword in a comment. Future iterations may provide 
other types of information. 

To run the bot, please add a config.ini file at the root level, with the format:

[OAUTH] \
client_id = some_value \
client_secret = some_value \
password = some_value \
user_agent = some_value \
username = some_value

[OTHER]
subreddit = some_value \
state = some_value \
web = some_value

Created by Steven Cheung and Joe Han for Hack@Brown 2021. 