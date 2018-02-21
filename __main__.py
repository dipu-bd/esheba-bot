#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main point of execution"""
import sys
from EshebaBot.esheba import EshebaBot


def main():
    '''main method to call'''
    if len(sys.argv) < 3:
        return show_help()
    # end if

    email = sys.argv[1]
    password = sys.argv[2]
    EshebaBot(email, password).start()
# end def


def show_help():
    '''displays help'''
    print('EshebaBot:')
    print('  python . <user-email> <password>')
    print()
    print('OPTIONS:')
    print('user-email*  Email of the user to login.')
    print('password*    Password to login')
    print()
    print('HINTS:')
    print('- * marked params are required')
    print()
# end def

main()
