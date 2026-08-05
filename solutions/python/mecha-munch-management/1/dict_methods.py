"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:       
        current_cart[item] = current_cart.setdefault(item,0) + 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    return dict.fromkeys(notes,1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)

    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    cart_ordenada = dict(sorted(cart.items()))

    return cart_ordenada


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    fulfillment_cart = {}
    
    # 1. Ordenamos las claves del carrito alfabéticamente y luego las invertimos (Z a A)
    # sorted(cart.keys()) las ordena de A a Z
    # reversed(...) les da la vuelta para que vayan de Z a A
    for item in reversed(sorted(cart.keys())):
        # 2. Obtenemos la cantidad del carrito del usuario
        quantity = cart[item]
        
        # 3. Obtenemos la info de la tienda (pasillo y si va refrigerado) desde aisle_mapping
        store_info = aisle_mapping[item]  # Ejemplo: ['Aisle 5', False]
        
        # 4. Juntamos la cantidad con la info de la tienda en una sola lista: [cantidad, pasillo, refrigeración]
        fulfillment_cart[item] = [quantity] + store_info
        
    return fulfillment_cart
        
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    # Recorremos cada producto y su información en el carrito de cumplimiento
    for item, order_info in fulfillment_cart.items():
        # order_info[0] es la cantidad que el usuario ha comprado (el primer elemento de la lista)
        ordered_quantity = order_info[0]
        
        # Restamos la cantidad comprada al stock actual de la tienda (que está en la posición 0 de la lista del inventario)
        store_inventory[item][0] -= ordered_quantity
        
        # Comprobamos si el stock se ha quedado a 0 (o menos)
        if store_inventory[item][0] == 0:
            # Si es 0, lo reemplazamos por el texto 'Out of Stock'
            store_inventory[item][0] = 'Out of Stock'
            
    return store_inventory
