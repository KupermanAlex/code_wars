def areYouPlayingBanjo(name):
    """Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!"""
    if 'R' == name[0] or 'r'==name[0]:
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
   