import logging

class Drink:

    def __init__(self,title,price,volume) -> None:
        self.title = title
        self.price = price
        self.volume = volume
        self.logger = logging.getLogger()
        self.logger.debug('Class Drink created')

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def get_info(self):
        return self.volume
