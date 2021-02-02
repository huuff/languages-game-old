#!/usr/bin/env python
import http.client
import os
from ...lib import command
from ...lib.testcase import FuncTestCase

def make_get_request():
    client = http.client.HTTPConnection('localhost', 8000) #TODO: Parameterize port
    client.request('GET', '')
    response = client.getresponse()
    return response.status


def test_cases():
    return [
            FuncTestCase(make_get_request, 200)
            ]

