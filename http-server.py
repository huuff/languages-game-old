#!/usr/bin/env python3
import main.tasks.http_server.test

test_case = main.tasks.http_server.test.HTTPServerTest('main/tasks/http_server/')
test_case.test_template()
