# Impleament business logic here for item

from app.config import Config
from app import models 

config = Config()



class ItemManager:

    def get(self, id) -> models.Item:
        pass