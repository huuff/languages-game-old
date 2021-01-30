#!/usr/bin/env python
import http.client
import os
from ...lib import testbase
from ...lib import command

def make_get_request():
    client = http.client.HTTPConnection('localhost', 8000) #TODO: Parameterize port
    client.request('GET', '')
    response = client.getresponse()
    return response.status


class Test(testbase.BaseTest):
    def test_cases(self):
        return {
                '1': 200
                }

    # TODO: Improve test classes in their own class so they admit
    # arbitrary code blocks besides input and output pairs
    def configure_command(self, test_case, base_command):
        return command.LongRunningCommand(base_command, make_get_request)
