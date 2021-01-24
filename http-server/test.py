#!/usr/bin/env python
import unittest
import http.client
import sys
sys.path.append('../lib')
import testbase
import command

def make_get_request():
    client = http.client.HTTPConnection('localhost', 8000) #TODO: Parameterize port
    client.request('GET', '')
    response = client.getresponse()
    return response.status


class HTTPServerTest(testbase.BaseTest):
    test_cases = {
            '1': 200
            }

    # TODO: Improve test classes in their own class so they admit
    # arbitrary code blocks besides input and output pairs
    def configure_command(self, test_case, base_command):
        return command.LongRunningCommand(base_command, make_get_request)



if __name__ == '__main__':
    unittest.main()
