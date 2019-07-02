def zero_fuel(distance_to_pump, mpg, fuel_left):
    """is there enough fuel to return home"""
    if distance_to_pump > mpg *  fuel_left :
        return False
    return True
