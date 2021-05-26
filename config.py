import os
class Config(object):
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    GUSERNAME = os.environ.get('GUSER_NAME')
    GPASSWORD = os.environ.get('GPASSWORD')
    SCHEDULE = os.environ.get('SCHEDULE', True)
    USERID = os.environ.get('USERID')
# If you're not familiar with how to set Environment Variables you can do like this instead
# of  setting Environment Variables

# BOT_TOKEN = os.environ.get('BOT_TOKEN', '1703305879:AAEDC7W-YHM6_XdBUufrjjXv4-YoEZMEsmM')
# GUSERNAME = os.environ.get('GUSER_NAME', 'insaneman220@gmail.com')
# GPASSWORD = os.environ.get('GPASSWORD', 'insane0001')

#NOTE: Putting sensitive information in files is considered unsafe. Try to use ENVIRONMENT VARIABLES 
