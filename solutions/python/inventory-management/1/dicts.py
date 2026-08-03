"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    inventario = {}
    
    for item in items:
        inventario [item]= inventario.get(item, 0) +1

    return inventario


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    for item in items:
        # 1. Primero comprobamos que el objeto realmente está en el inventario
        if item in inventory:
            # 2. Si su cantidad es mayor que 0, le restamos 1
            if inventory[item] > 0:
                inventory[item] -= 1  # Esto es lo mismo que inventory[item] = inventory[item] - 1
                
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item,None)

    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    resultado = []
    for item,cantidad in inventory.items():
        if cantidad >0:
            resultado.append((item,cantidad))

    return resultado
        
