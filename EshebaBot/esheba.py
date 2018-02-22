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

    def __init__(self):
        urllib3.disable_warnings()
        self.session = requests.Session()
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
    # end def

    def start_session(self):
        '''starts the session and get captcha'''
        url = 'https://www.esheba.cnsbd.com/index'
        r = self.session.get(url, verify=False)
        cookies = self.session.cookies.get_dict()
        self.token = cookies['PHPSESSID']
        soup = BeautifulSoup(r.content, 'lxml')
        captcha = soup.select_one('img#captcha')['src']
        self.captcha = path.basename(captcha).strip('.png')
    # end def

    def close_session(self):
        '''stops the session'''
        self.session.close()
    # end def

    def get_captcha_url(self):
        '''Generate text from captcha'''
        if not self.captcha:
            raise Exception('No captcha found!')
        else:
            return 'https://www.esheba.cnsbd.com/images/captcha/%s.png' % self.captcha
        # end if
    #end def

    def login(self, usermail, password, security_code):
        '''login to the website'''
        url = 'https://www.esheba.cnsbd.com/index'
        data = {
            'usermail': usermail,
            'password': password,
            'security_code': security_code,
            'captcha[id]': self.captcha,
            'signin': 'SIGN-IN'
        }
        headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
        r = self.session.post(url, data=data, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        errors = soup.select('#messages .error-msg')
        errors = [x.text.strip() for x in errors if x.text.strip()]
        return '\n'.join(errors).strip()
    # end def

    def check_session(self):
        url = 'https://www.esheba.cnsbd.com/account/index'
        r = self.session.get(url, verify=False)
        soup = BeautifulSoup(r.content, 'lxml')
        captcha = soup.select('img#captcha')['src']
        return len(captcha) == 0
    # end def

    def get_personal_info(self):
        '''gets the personal informations'''
        url = 'https://www.esheba.cnsbd.com/account/index'
        r = self.session.get(url, verify=False)
        soup = BeautifulSoup(r.content, 'lxml')
        table_headers = soup.select('#dashboard .table .home th')
        table_bodies = soup.select('#dashboard .table .home td')
        data = dict()
        for i, th in enumerate(table_headers):
            header = th.text.strip()
            if header == 'Name':
                data['Name'] = table_bodies[i].text
            elif header == 'Email Address':
                data['EmailAddress'] = table_bodies[i].text
            elif header == 'Address':
                data['Address'] = table_bodies[i].text
            elif header == 'Cell Phone Number':
                data['PhoneNumber'] = table_bodies[i].text
            # end if
        # end for
        return data
    # end def

    def test(self, usermail, password):
        '''test if the service works'''
        print('Starting session')
        self.start_session()
        print('Session ID =', self.token)
        print('Captcha =', self.captcha)
        captcha_url = self.get_captcha_url()
        r = self.session.get(captcha_url, verify=False)
        security_code = solve_captcha(r.content)
        r = self.login(usermail, password, security_code)
        print('Login response =', r)
        r = self.get_personal_info()
        print('Personal informations =', r)
    # end def
# end class

if __name__ == '__main__':
    EshebaBot().test(
        usermail=sys.argv[1],
        password=sys.argv[2]
    )
# end if
