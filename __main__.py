#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main point of execution"""
import sys
from server import run_server
from tests import run_tests, direct_test


def show_help():
    '''displays help'''
    print('EshebaBot:')
    print('  python . [options]')
    print()
    print('OPTIONS:')
    print(' -S, --server        Run the server')
    print(' -T, --test-grpc     Test running server')
    print(' -t, --test          Test methods directly')
    print()
# end def

'''main method to call'''
if len(sys.argv) < 2:
    show_help()
elif sys.argv[1] in ['--server', '-S']:
    run_server()
elif sys.argv[1] in ['--test', '-t']:
    direct_test()
elif sys.argv[1] in ['--test-grpc', '-T']:
    run_tests()
else:
    show_help()
# end if
