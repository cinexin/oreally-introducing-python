from random import choice

def get_description():
    '''Return random weather,
     just like professionals'''
    possibilities = ['rain','snow','sleet','fog','sunny','who knows']
    return choice(possibilities)