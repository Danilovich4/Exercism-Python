"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """

    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """

    coordenadas_azara = convert_coordinate(azara_record[1])

    if coordenadas_azara == rui_record[1]:
        return True
    else:
        return False


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """

    report = ""

    for record in combined_record_group:
        # 1. Quitamos la posición 1 (la coordenada de Azara) usando slicing
        # Tomamos el primer elemento (record[0:1]) y se lo pegamos a del tercero en adelante (record[2:])
        clean_record = record[0:1] + record[2:]

        # 2. Convertimos la tupla a string, le añadimos el salto de línea y lo sumamos al reporte
        report += f"{clean_record}\n"

    return report
