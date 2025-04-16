from item import Item
inventory_list = []

def add_item():
    try:
        name = input('Name: ')
        q = int(input('Quantity: '))
        desc = input('Description: ')
        item = Item(name, q, desc)
        inventory_list.append(item)
    except:
        print('Error')

def print_items():
    for item in inventory_list:
        name = item.name
        q = item.quantity
        desc = item.description
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
        item.quantity = new_q
    except:
        print('Error')