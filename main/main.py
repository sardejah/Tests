# -*- coding: utf-8 -*-

def hello(name):
    try :
        return 'hello ' + name
    except : 
        return 'Type error'



print(hello('world'))
print(hello(1))