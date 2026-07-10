"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    Parameters:
        temperature (int or float): The temperature value in kelvin.
        neutrons_emitted (int or float): The number of neutrons emitted per second.

    Returns:
        bool: Is criticality balanced?

    Note:
        A reactor is said to be balanced in criticality if it satisfies the following conditions:
            - The temperature is less than 800 K.
            - The number of neutrons emitted per second is greater than 500.
            - The product of temperature and neutrons emitted per second is less than 500000.

    """
    return (temperature < 800) and (neutrons_emitted > 500) and (temperature * neutrons_emitted < 500000)
        


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    Parameters:
        voltage (int or float): Voltage value.
        current (int or float): Current value.
        theoretical_max_power (int or float): The power level that corresponds to a 100% efficiency.

    Returns:
        str: One of ('green', 'orange', 'red', or 'black').

    Note:
        Efficiency can be grouped into 4 bands:
            1. green -> efficiency of 80% or more,
            2. orange -> efficiency of less than 80% but at least 60%,
            3. red -> efficiency below 60%, but still 30% or more,
            4. black ->  less than 30% efficient.

        The percentage value is calculated as
        (generated power/ theoretical max power)*100
        where generated power = voltage * current
    """
    # 1. Calculamos la potencia generada
    generated_power = voltage * current
    
    # 2. Calculamos el porcentaje de eficiencia
    efficiency = (generated_power / theoretical_max_power) * 100
    
    # 3. Clasificamos de mayor a menor
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    Parameters:
        temperature (int or float): The value of the temperature in kelvin.
        neutrons_produced_per_second (int or float): The neutron flux.
        threshold (int or float): The threshold for the category.

    Returns:
        str: One of ('LOW', 'NORMAL', 'DANGER').

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    # 1. Calculamos el valor actual del reactor
    current_value = temperature * neutrons_produced_per_second
    
    # 2. Calculamos los límites basados en los porcentajes del threshold
    low_bound = threshold * 0.9
    high_bound = threshold * 1.1

    # 3. Clasificamos usando la estructura condicional
    if current_value < low_bound:
        return 'LOW'
    elif current_value <= high_bound:
        # Como ya sabemos que no es menor a 'low_bound', si es menor o igual
        # a 'high_bound', significa que está exactamente en el rango del 10%
        return 'NORMAL'
    else:
        # Si no es bajo ni normal, está críticamente alto
        return 'DANGER'
