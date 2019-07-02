def enough(cap, on, wait):
    """write a simple program telling him if he will be able to fit all the passengers."""
    if on + wait <= cap : 
        return   0     
    else: return on + wait - cap