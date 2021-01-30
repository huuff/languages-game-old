#!/usr/bin/env python
import http.client
import os
from ...lib import testbase
from ...lib import command
from ...lib.testcase import FuncTestCase

def make_get_request():
    print("test")
    client = http.client.HTTPConnection('localhost', 8000) #TODO: Parameterize port
    client.request('GET', '')
    response = client.getresponse()
    return response.status


class Test(testbase.BaseTest):
    def test_cases(self):
        return [
                FuncTestCase(make_get_request, 200)
                ]

    def configure_command(self, base_command):
        return command.LongRunningCommand(base_command)

