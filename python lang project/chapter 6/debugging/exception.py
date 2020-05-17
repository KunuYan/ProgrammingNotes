'''
try:
    some_function()
except:
    graceful_function()
finally:
    cleanup_function()
'''

class TestClass(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def return_values(self):
        try:
            if type(self.number) is int:
                return "The values are: ", type(self.name), type(self.number)
            else:
                raise notANumber(self.number)
        except notANumber as e:
            print("The value for number must be an int you passed: ", str(type(e.value)))


# making our own exception
# error if self.number is not a number
class notANumber(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


exampl = TestClass('string1', 'string2')
exampl.return_values()

# you can also test it in interactive mode:
#   python -i filename.py

