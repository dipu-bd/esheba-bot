#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Auto login to Bangladesh Railway website.

[Esheba](https://www.esheba.cnsbd.com) provides railway services and
information about train routes and timetable.
"""
import re
import sys
import json
import requests
from os import path
from .helper import get_browser

class EshebaBot:
    '''Create REST bot to esheba'''

    def __init__(self, useremail, password):
        if (not useremail) or (not password):
            raise Exception('User email and password is required')
        # end if
        self.useremail = useremail
        self.password = password
    # end def

    def start(self):
        '''start crawling'''
        browser = get_browser()
        try:
            self.login(browser)
        finally:
            browser.quit()
        # end try
    # end def

    def login(self, browser):
        '''get list of chapters'''
        url = 'https://www.esheba.cnsbd.com/index'
        browser.visit(url)
        form = browser.find_by_css('form#loginhome')
        form.find_by_css('input#usermail').fill(self.useremail)
        form.find_by_css('input#password').fill(self.password)
        captcha = form.find_by_css('img#captcha').first['src']
        print(captcha)
    # end def

# end class

if __name__ == '__main__':
    EshebaBot(
        useremail=sys.argv[1],
        password=sys.argv[2]
    ).start()
# end if
