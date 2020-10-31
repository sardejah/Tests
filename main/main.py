# -*- coding: utf-8 -*-

def hello(name):
    try :
        return 'Hello ' + name
    except : 
        return 'Type error'



print(hello('world'))
print(hello(1))