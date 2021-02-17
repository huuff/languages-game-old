#!/usr/bin/env python
import http.client
import os
from ...lib import command
from ...lib.testcase import FuncTestCase
from ...lib.config import current as config
from functools import partial

def make_get_request(path):
    client = http.client.HTTPConnection(f'localhost', config().port()) 
    client.request('GET', f'/{path}')
    response = client.getresponse()
    return response.status


def test_cases():
    return [
            FuncTestCase(partial(make_get_request, 'server'), '200'),
            FuncTestCase(partial(make_get_request, ''), '404')
            ]

