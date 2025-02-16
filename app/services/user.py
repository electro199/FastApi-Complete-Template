# Impleament logic here for user 


from app.config import Config
from app import models 

config = Config()

class UserManager():

    def get_user(self, id) -> models.User:
        # Add logic here
        pass


def get_user_manager():
    return     UserManager()