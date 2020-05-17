"""
once the pdb prompt is open at your set location using pdb.set_tracer()
you have all this commands available to you.:
    n: read an run next line
    [space_bar]: run previous command
    p [variable_name]: print the variable(usefull to see if u actually have data)
    locals(): print every you have at a locals scopes (lines that've been ran already)
    globals(): print every you have at global scopes
    c: quit pdb prompt, rest of code will run
    q: quit pdb prompt, rest of code won't run
    u: run pdb promt till the end, but won't exit promt

explore pdb more!
"""

import pdb

class ExampleClass(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def example_entry(self):
        pdb.set_trace() # the pdb prompt will be open at this line
        return "The example name is {0} with the number {1}".format(self.name,
        self.number)

if __name__ == '__main__':
    example = ExampleClass("Carla", 456)
    print(example.example_entry())
