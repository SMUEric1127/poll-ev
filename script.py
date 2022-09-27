from cmath import log
from pollevbot import PollBot

user = 'vue@smu.edu'
password = 'pev1127'
host = 'wickersham2331'

# If you're using a non-UW PollEv account,
# add the argument "login_type='pollev'"
with PollBot(user, password, host, login_type="pollev") as bot:
    bot.run()