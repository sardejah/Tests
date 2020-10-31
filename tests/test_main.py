# -*- coding: utf-8 -*-
from main.main import *

def test_hello_good_output():
    assert hello('world') == 'Hello world'

def test_hello_wrong_type1():
    assert hello(1) == 'Type error'

def test_hello_wrong_output():
    assert hello('abc') != 'Hello world'