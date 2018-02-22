#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main point of execution"""
import sys
from tests import run_tests
from server import run_server
from EshebaBot.esheba import EshebaBot


def main():
    '''main method to call'''
    if len(sys.argv) < 2:
        return show_help()
    # end if

    if sys.argv[1] == '--server':
        run_server()
    elif sys.argv[1] == '--test':
        run_tests()
    elif len(sys.argv) < 3:
        return show_help()
    else:
        email = sys.argv[1]
        password = sys.argv[2]
        EshebaBot().test(email, password)
    # end if

# end def


def show_help():
    '''displays help'''
    print('EshebaBot:')
    print('  python . <user-email> <password>')
    print('  python . --server')
    print('  python . --test')
    print()
    print('OPTIONS:')
    print(' user-email* Email of the user to login.')
    print(' password*   Password to login')
    print(' --server    Starts the grpc server')
    print(' --test      Runs grpc test client')
    print()
    print('HINTS:')
    print('- * marked params are required')
    print()
# end def

main()
