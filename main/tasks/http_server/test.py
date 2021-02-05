#!/usr/bin/env python
import http.client
import os
from ...lib import command
from ...lib.testcase import FuncTestCase
from ...lib import config

def make_get_request():
    client = http.client.HTTPConnection('localhost', config.current().get_port()) 
    client.request('GET', '')
    response = client.getresponse()
    return response.status


def test_cases():
    return [
            FuncTestCase(make_get_request, 200)
            ]

