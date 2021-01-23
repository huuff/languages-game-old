#!/usr/bin/env python
import os
import subprocess
import unittest
import configparser
import http.client
import time

configFile = 'config'

class HTTPServerTest(unittest.TestCase):
    def buildPath(self, root, fileName):
        return root + '/' + fileName

    def test_template(self):
        config = configparser.ConfigParser()
        config['Commands'] = {'fileName': '', 'runCommand': ''}
        configVars = config['Commands']
        for root, dirs, files in os.walk(".", topdown=True):
            if configFile in files:
                config.read(self.buildPath(root, configFile))
            if configVars['fileName'] in files:
                command = [configVars['runCommand'], self.buildPath(root, configVars['fileName'])]

                server = subprocess.Popen(command)
                time.sleep(1)
                client = http.client.HTTPConnection('localhost', 8000)
                client.request('GET', '')
                response = client.getresponse()

                server.terminate()
                server.wait()

                self.assertEqual(200, response.status)


    
    def configure_command(self, test_case, command): pass

if __name__ == '__main__':
    unittest.main()
