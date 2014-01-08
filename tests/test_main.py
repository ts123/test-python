# -*- coding: utf-8 -*-
import sys
import os
import datetime

import mock
import pytest

sys.path.append('.')
import greeter

@pytest.mark.parametrize("hour,min,sec,expect", [
    ( 0,  0,  0, u'こんばんは'),
    ( 0,  0,  1, u'こんばんは'), 
    ( 4, 59, 59, u'こんばんは'), 
    ( 5,  0,  0, u'おはよう'), 
    ( 5,  0,  1, u'おはよう'), 
    (11, 59, 59, u'おはよう'), 
    (12,  0,  0, u'こんにちは'), 
    (12,  0,  1, u'こんにちは'), 
    (17, 59, 59, u'こんにちは'), 
    (18,  0,  0, u'こんばんは'), 
    (18,  0,  1, u'こんばんは'), 
    (23, 59, 59, u'こんばんは'), 
    # (24, 0, 0, u'こんばんは'), 
])
def test_greet(hour, min, sec, expect):
    class datetimeMock(datetime.datetime):
        @classmethod
        def now(cls):
            return datetime.datetime(2000, 1, 1, hour, min, sec)
    with mock.patch('datetime.datetime', datetimeMock):
        assert greeter.greet() == expect

