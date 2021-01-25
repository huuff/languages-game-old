#!/usr/bin/env python
import sys

task = sys.argv[1]

if task == 'fibonacci' or task == 'fib':
    import main.tasks.fibonacci.test
    main.tasks.fibonacci.test.FibonacciTest('main/tasks/fibonacci/').test_template()
elif task == 'sorting' or task == 'sort':
    import main.tasks.sorting.test
    main.tasks.sorting.test.SortingTest('main/tasks/sorting/').test_template()
elif task == 'http-server' or task == 'server':
    import main.tasks.http_server.test
    main.tasks.http_server.test.HTTPServerTest('main/tasks/http_server/').test_template()
