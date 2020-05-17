''' The following code is somewhat outdated, it should only be used as reference
for further research.
'''

# Testing using the verbose module
# must have space beteen >>> and func_name()
# the you run your test like this:
#     python -m doctest -v simple_doctest.py
# -m: run py file using a module, -v: verbose output
# if you want to add documentations, you must separated it from your test by empty line
def simple_math(x, y):
    '''
    This function will return x + y
    we can use it on numbers. Passing 1 and 2:

    >>> simple_math(1, 2)
    3

    We should get 3 as a return value
    It will also work on strings. Passing the strings 'k' and 'v':

    >>> simple_math('k', 'v')
    'kv'

    We should get 'kv'
    '''

    return x + y



class SimpleClass():
    def __init__(self, func):
        pass

obj = {}
# doctest requires an actual output to match the predicted one, but we can't predict memory locations
# their is a work around that, if the work around is not present 
# this test will fail because it is evaluating an object in memory(we can't predict location in memory)
"""
def class_testing_method_ahoy(obj):
    ''' Should return a list containing the object

    >>> SimpleClass(class_testing_method_ahoy(obj))
    [<doctest_class_testing_method_ahoy.SimpleClass object at /
    0x10382a390] 
    '''

    return [obj]
"""


def class_testing_method_ahoy(obj):
    ''' Should return a list containing the object

    >>> class_testing_method_ahoy(SimpleClass()) /
        # doctest: ELLIPSIS
    [<simple_doctest.SimpleClass object at /
    0x...>] 
    '''
    # the 'doctest: +ELLIPSIS' lets doctest know that what follows the '...' can be any value

    return [obj]

"""
The ELLIPSIS constant is also useful if you are checking that a list is returned, such as when using
the range() method. Say you want to make sure you get back the numbers 1–4,590 when you call
range(4589). Rather than print the entire list of 4,590 numbers, you can use the ELLIPSIS constant
and simply have your result be [0, 1, ... , 4588, 4589]

"""