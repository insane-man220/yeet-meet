import os
class Config(object):
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '1703305879:AAH0R6r5hJ-OfMWwyU2SJB3ygltsN4l9dyc')
    GUSERNAME = os.environ.get('GUSER_NAME', 'insaneman220@gmail.com')
    GPASSWORD = os.environ.get('GPASSWORD', 'insane0001')
    SCHEDULE = os.environ.get('SCHEDULE', True)
    USERID = os.environ.get('USERID', '1730969992')
# If you're not familiar with how to set Environment Variables you can do like this instead
# of  setting Environment Variables

# BOT_TOKEN = os.environ.get('BOT_TOKEN', '1703305879:AAH0R6r5hJ-OfMWwyU2SJB3ygltsN4l9dyc')
# GUSERNAME = os.environ.get('GUSER_NAME', 'insaneman220@gmail.com')
# GPASSWORD = os.environ.get('GPASSWORD', 'insane0001')

#NOTE: Putting sensitive information in files is considered unsafe. Try to use ENVIRONMENT VARIABLES 
