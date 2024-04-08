# Communicated with food and drink
import logging

from Food.food import Food
from Drink.drink import Drink

# Der Logger muss auf Class Level Implementiert werden. Mit self!
# Der Level in der logging.ini muss Debug sein!

class Menu:

    def __init__(self) -> None:
        self.food_list = []
        self.drink_list = []
        self.order_list = []
        self.current_list = []
        self.sum_price = 0
        self.logger = logging.getLogger()
        self.logger.debug('Class Menu created')

    def main_navigation(self):
        choices = ['0 Abbrechen','1 Food','2 Drinks','3 Rechnung']
        for item in choices:
            print(item)
        self.logger.info('Waiting for User Input')
        user_input = int(input('Enter a number to navigate: '))
        print()
        self.logger.debug('User Interface shown')
        return user_input    

    def create_menu(self):
        pizza_1 = Food('Pizza Pepperoni',6,'Pepperoni') # 3 Pizza. 3 Drink. Normalerweise in eine Datenbank
        self.food_list.append(pizza_1)
        self.logger.debug('Item added to menu')
        pizza_2 = Food('Pizza Fungi',5,'Pilze')
        self.food_list.append(pizza_2)
        self.logger.debug('Item added to menu')
        pizza_3 = Food('Pizza Margerita',4,'Käse')
        self.food_list.append(pizza_3)
        self.logger.debug('Item added to menu')

        drink_1 = Drink('Wasser',1,'2 Teil Wasserstoff, 1 Teil Sauerstoff')
        self.drink_list.append(drink_1)
        self.logger.debug('Item added to menu')
        drink_2 = Drink('Tee',2,'0,2 Liter Gesunde Kräuter')
        self.drink_list.append(drink_2)
        self.logger.debug('Item added to menu')
        drink_3 = Drink('Rum',3,'50 ml Geschmacksorgasmus für Alcohol Connoisseurs')
        self.drink_list.append(drink_3)
        self.logger.debug('Item added to menu')


    def show_menu_food(self):
        # print('-1 Delete last added item')
        print('0 Zurück')
        id = 0
        for item in self.food_list:
            id += 1
            print(id,item.get_title())
        print('4 Info')
        self.current_list = self.food_list
        self.logger.debug('show_menu_drink function -> Food List shown')
    

    def show_menu_drink(self):
        # print('-1 Delete last added item')
        print('0 Zurück')
        id = 0
        for item in self.drink_list:
            id += 1
            print(id,item.get_title())
        print('4 Info')
        self.current_list = self.drink_list
        self.logger.debug('show_menu_drink function -> Drink List shown')

    # def show_menu_info2(self):
        # for item in self.current_list:
            # print(item.get_title(),'->',item.get_info())
        # print()
    
    def show_menu_info(self):
        self.logger.info('Waiting for User Input')
        user_input = int(input('Zu welchem Angebot möchten sie zusätzliche Informationen? '))
        print()
        print(self.current_list[user_input-1].get_title(),'->',self.current_list[user_input-1].get_info())
        print()
        self.logger.debug('show_menu_info function -> Info shown')

    def add_order(self):
        self.logger.info('Waiting for User Input')
        user_input = int(input('Was möchten sie bestellen? '))
        print()
        # if user_input == -1:
            # self.order_list.pop()
        if user_input == 0:
            self.logger.debug('add_order function -> User Input given : 0')
            return user_input
        if  user_input == 4:
            self.logger.debug('add_order function -> User Input given : 4')
            return user_input
        else:
            self.order_list.append(self.current_list[user_input-1])
            print('Item added')
            self.logger.debug('add_order function -> User Input given : other')
            print()
            return 100


    def show_orders(self):
        id = 0
        for item in self.order_list:
            id += 1
            print(id,item.get_title(),item.get_price())
            self.sum_price += item.get_price()
        print(self.sum_price)
        self.logger.debug('show_orders function -> orders shown') 
        print()
        print('1 Yes')
        print('2 Not yet')
        self.logger.info('Waiting for User Input')
        user_input = int(input('Would you like to pay with hard earned money? '))
        print()
        self.logger.debug('show_orders function -> User Input given: 1 ')
        return user_input,self.order_list,self.sum_price



