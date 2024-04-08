import logging

class Food:

    def __init__(self,title,price,ingredients) -> None:
        self.title = title
        self.price = price
        self.ingredients = ingredients
        self.logger = logging.getLogger()
        self.logger.debug('Class Food created')

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def get_info(self):
        return self.ingredients
