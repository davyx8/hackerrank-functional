import itertools
import types

def tramp(gen, *args, **kwargs):
    """ 
        Copyright, 2012, Alex Beal
        Used by permission
    """
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g
resolv = {'(':')' , '[':']','{':'}'}
resolv = {'(':')' , '[':']','{':'}'}
def check_par(string, stack):
    try:
        char = next(string)
    except Exception as e:
        yield True if not len(list(stack)) else False
    try:
        yield (
            check_par(string ,itertools.chain([char],stack)) if char in resolv else
            check_par(string ,stack) if resolv[next(stack)] == char else
            False )
    except Exception as e:
        yield False

def is_matched(expression):
    a = (char for char in expression)
    return tramp(check_par,a , [] )