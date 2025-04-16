"""
Create an inventory tracking system that has all of the following features:

Each item will have a name, quantity, and description as a dictionary.

All dictionaries will be saved in a master inventory list.

A function that adds something to that list (creates the dictionary and adds to the list).

A function that displays the inventory in a readable format (i.e. do not just print out the list or dictionary, separate them out).

A function that will change the quantity of an item (this is difficult to do and many ways to do it).

A function that removes an item from the list. Research required :)
"""

inventory_list = []

def add_item():
    try:
        name = input('Name: ')
        q = int(input('Quantity: '))
        desc = input('Description: ')
        new_item = {
            'name': name,
            'quantity': q,
            'description': desc
        }
        inventory_list.append(new_item)
    except:
        print('Error')

def print_items():
    for item in inventory_list:
        name = item['name']
        q = item['quantity']
        desc = item['description']
        index = inventory_list.index(item)
        print(f'Item ID: {index}')
        print(f'Item Name: {name}')
        print(f'Item Quantity: {q}')
        print(f'Item Description: {desc}')

def change_quantity():
    try:
        index = int(input('Item Number: '))
        item = inventory_list[index]
        new_q = int(input('New quantity: '))
        item['quantity'] = new_q
    except:
        print('Error')

def rm_item():
    try:
        index = int(input('Enter Item to remove: '))
        inventory_list.pop(index)
    except:
        print('Error')


add_item()
add_item()
print_items()
rm_item()
print_items()