from datetime import datetime as dt
import Functions as f
import Classes as c
import pickle as p

"""
_______________________________________________________________________________________
The purpose of this program is to create an inventory system for my food, including
where it is stored, when it was bought, and when it will go bad
_______________________________________________________________________________________
"""

def main():

    print("""Food inventory menu:
          1.Display inventories
          2.New Entry""")
    menu_sel = input('Enter your menu selection: ')
    while int(menu_sel) != 1 or int(menu_sel) != 2:
        try :
            int(menu_sel) == 1 or int(menu_sel) == 2

        except:
            menu_sel = input('Enter your menu selection')

    again = True

    while again:

        if menu_sel == 1:
            print("""Which bin would you like to see?
            1. Fridge
            2. Pantry
            3. Freezer
            4. All
            5. Back""")
            sec_menu_sel = input('Enter your menu selection: ')
            if sec_menu_sel == 1:
                sec_menu_sel = None
                f.inventory_display(sec_menu_sel)
            elif sec_menu_sel == 2:
                sec_menu_sel = None
                f.inventory_display(sec_menu_sel)
            elif sec_menu_sel == 3:
                sec_menu_sel = None
                f.inventory_display(sec_menu_sel)
            elif sec_menu_sel == 4:
                sec_menu_sel = None
                f.inventory_display(sec_menu_sel)
            elif sec_menu_sel == 5:
                sec_menu_sel = None
                continue

        elif menu_sel == 2:
            print("""""")