#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Auto login to Bangladesh Railway website.

[Esheba](https://www.esheba.cnsbd.com) provides railway services and
information about train routes and timetable.
"""
import re
import sys
import json
import urllib3
import requests
from os import path
from bs4 import BeautifulSoup
from .helper import solve_captcha


class EshebaBot:
    '''Create REST bot to esheba'''

    def __init__(self, useremail, password):
        if (not useremail) or (not password):
            raise Exception('User email and password is required')
        # end if
        self.useremail = useremail
        self.password = password
        self.captcha = '1fc9186ed74f4a6cb00b55e88de6b392'
        self.security_code = '13193'
        urllib3.disable_warnings()
    # end def

    def start(self):
        '''start crawling'''
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
        try:
            self.get_tokens(session)
            self.solve_captcha()
            self.login(session)
            self.get_personal_info(session)
        finally:
            session.close()
        # end try
    # end def

    def get_tokens(self, session):
        '''get php session id and captcha code'''
        url = 'https://www.esheba.cnsbd.com/index'
        print('Getting Session ID:', url)
        r = session.get(url, verify=False)
        cookies = session.cookies.get_dict()
        self.token = cookies['PHPSESSID']
        soup = BeautifulSoup(r.content, 'lxml')
        captcha = soup.select_one('img#captcha')['src']
        self.captcha = path.basename(captcha).strip('.png')
        print('Session ID =', self.token)
        print('Captcha =', self.captcha)
    # end def

    def solve_captcha(self):
        '''Generate text from captcha'''
        url = 'https://www.esheba.cnsbd.com/images/captcha/' + self.captcha + '.png'
        print('Getting image:', url)
        r = requests.get(url, verify=False)
        self.security_code = solve_captcha(r.content)
        print('Solved captcha =', self.security_code)
    #end def

    def login(self, session):
        '''login to the website'''
        url = 'https://www.esheba.cnsbd.com/index'
        data = {
            'usermail': self.useremail,
            'password': self.password,
            'security_code': self.security_code,
            'captcha[id]': self.captcha,
            'signin': 'SIGN-IN'
        }
        headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
        r = session.post(url, data=data, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        errors = soup.select('#messages .error-msg')
        errors = [x.text.strip() for x in errors if x.text.strip()]
        if len(errors):
            print('Error: ', '; '.join(errors))
            return False
        # end if
    # end def

    def get_personal_info(self, session):
        '''gets the personal informations'''
        url = 'https://www.esheba.cnsbd.com/account/index'
        r = session.get(url, verify=False)
        soup = BeautifulSoup(r.content, 'lxml')
        table_headers = soup.select('#dashboard .table .home th')
        table_bodies = soup.select('#dashboard .table .home td')
        print('\n--- Personal Informations ---')
        for i in range(min(len(table_bodies), len(table_headers))):
            print(' ', table_headers[i].text, '=', table_bodies[i].text)
        # end for
    # end def

# end class

if __name__ == '__main__':
    EshebaBot(
        useremail=sys.argv[1],
        password=sys.argv[2]
    ).start()
# end if
