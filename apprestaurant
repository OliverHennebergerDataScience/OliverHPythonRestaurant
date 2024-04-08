# Communicates with menu
import logging

import appconfig.config as cfg

import os
from pathlib import Path

from Menu.menu import Menu

from fpdf import FPDF
# Neustarten hat das import problem gelöst


logger = logging.getLogger()


# print(cfg.APP_FOLDER)
# print(cfg.DATASET_PATH)

def create_pdf_append():
    APP_FOLDER = Path(__file__).parent # changes the working directory to the parent of this file
    # os.chdir(APP_FOLDER)

    p = open(f'{APP_FOLDER}/Rechnung.pdf', mode = "a")
    return p

def create_txt_append():
    APP_FOLDER = Path(__file__).parent # changes the working directory to the parent of this file
    # os.chdir(APP_FOLDER)

    f = open(f'{APP_FOLDER}/Rechnung.txt', mode = "a")
    return f

def convert_txt_to_pdf():
    # Check https://pypi.org/
    # Version 3.9.7 Compatible
    APP_FOLDER = Path(__file__).parent

    # Converter here
    '''
    #Test 3 SUCCESFULL but no style !
    temp_txt = open(f'{APP_FOLDER}/Rechnung.txt', mode = "r")
    data_txt=temp_txt.readlines() # Reads out the Text in python string format
    print(data_txt)

    temp_pdf = open(f'{APP_FOLDER}/Rechnung_Conv_No_style.pdf', mode = "a")
    temp_pdf.write(f'{data_txt}') # No Formatting
    logger.debug('Rechnung PDF geschrieben')
    temp_txt.close
    temp_pdf.close
    '''
   
    # Test 2 Didn't Work
    # save FPDF() class into 
    # a variable pdf
    pdf = FPDF()   
   
    # Add a page
    pdf.add_page()
   
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
  
    # open the text file in read mode
    f = open(f'{APP_FOLDER}/Rechnung.txt', mode = "r")
  
    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10,txt = x , ln = 1, align = 'C')
   
    # save the pdf with name .pdf
    pdf.output(f'{APP_FOLDER}/Rechnung_Converted.pdf')  # 'F' ?  f"{APP_FOLDER}/Rechnung_Converted.pdf"
    logger.debug('Rechnung geschrieben PDF')

'''
def write_pdf(opened_pdf,order_list,sum_price):
    id = 0
    for item in order_list:
        id += 1
        opened_pdf.write(f'\n{id}, {item.get_title()}, {item.get_price()}')
    logger.debug('Item written on Rechnung PDF')    
    opened_pdf.write(f'\n{sum_price}')
    logger.debug('Rechnung geschrieben PDF')
    opened_pdf.close
'''

def write_txt(opened_txt,order_list,sum_price):
    id = 0
    for item in order_list:
        id += 1
        opened_txt.write(f'\n{id}, {item.get_title()}, {item.get_price()}')
    logger.debug('Item written on Rechnung')    
    opened_txt.write(f'\n{sum_price}')
    logger.debug('Rechnung geschrieben')
    opened_txt.close


def app():
    print()
    print('Hallo')
    print('was möchten sie bestellen?')
    print()

    menu1 = Menu()
    menu1.create_menu()
    close_app = 0
    while True:
        if close_app == 1:
            break
        user_input = menu1.main_navigation()  
        if user_input == 0 :
            break

# Menu zeigen Food und bestellen
        if user_input == 1:
            while True:
                menu1.show_menu_food()   
                # User Wünsche Food            
                user_input = menu1.add_order()
                if user_input == 0:
                    break
                if user_input == 4:
                    menu1.show_menu_info()
                    continue
                else:
                    continue
    
# Menu Zeigen Drink und bestellen
        if user_input == 2:
            while True:
                menu1.show_menu_drink()   
                # User Wünsche Food            
                user_input = menu1.add_order()
                if user_input == 0:
                    break
                if user_input == 4:
                    menu1.show_menu_info()
                    continue
                else:
                    continue

# Rechnung Zeigen und Einkauf abschließen
        if user_input == 3:
            while True:
                user_input,order_list,sum_price = menu1.show_orders()
                if user_input == 2:
                    print('Weiter einkaufen')
                    print()
                    break

                if user_input == 1:
                    print('Ihr Bestellung wurde bezahlt, und wird in kürze zugestellt')
                    print()
                    close_app = 1
                    opened_txt = create_txt_append()
                    # opened_pdf = create_pdf_append()

                    write_txt(opened_txt,order_list,sum_price)
                    # write_pdf(opened_pdf,order_list,sum_price) # created pdf was damaged and unreadable
                    break
                

    print('Auf wiedersehen')
    logger.debug('App closed')

app()

convert_txt_to_pdf() # Steht außerhalb der app() weil es sonst das vorherige ungeänderte Rechnung.txt als vorlage genommen hat.
