# -*- coding: utf-8 -*-
from main.main import *

def test_hello():
    assert hello('David') == 'Hello David'

def test_hello2():
    assert hello('David') != 'Hello Pierre'
