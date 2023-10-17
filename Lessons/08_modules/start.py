from random import randint

import settings
from settings import app_name

import models.user
from models.account import account_number


print("Hello, world!")
print("This is a main file!")
print("App name:", app_name)
print("App version:", settings.app_version)
print("Random int:", randint(1, 1000))
print("Today is", settings.datetime.now())
print("User name:", models.user.user_name)
print("Account number:", account_number)
