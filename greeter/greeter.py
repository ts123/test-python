#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import datetime

def greet():
    h = datetime.datetime.now().hour
    if 5 <= h < 12:
        return u'おはよう'
    elif 12 <= h < 18:
        return u'こんにちは'
    else:
        return u'こんばんは'

if __name__ == '__main__':
    print(greet())

