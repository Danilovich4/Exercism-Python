"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """

    wagon1, wagon2, *rest_of_train = each_wagons_id
    locomotive, *tail = rest_of_train
    return [locomotive, *missing_wagons, *tail, wagon1, wagon2]


def add_missing_stops(routing_dict, **kwargs):
    # kwargs es un diccionario con las paradas, ej: {'stop_1': 'Washington, DC', ...}
    # Extraemos solo los valores (las ciudades) y los convertimos en una lista:
    stops_list = list(kwargs.values())
    
    # Añadimos la nueva clave "stops" con su lista al diccionario de ruta
    routing_dict["stops"] = stops_list
    
    # Devolvemos el diccionario actualizado
    return routing_dict


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    return [list(row) for row in zip(*wagons_rows)]
