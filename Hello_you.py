def greet(name):
    """ function that returns a greeting for a user"""
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name) 