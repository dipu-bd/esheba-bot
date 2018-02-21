#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Helper methods used in crawling"""
import json
from os import path, makedirs
from splinter import Browser
from captcha_solver import CaptchaSolver

CHROME_DRIVER = path.join('lib', 'chromedriver')


def get_browser():
    '''open a headless chrome browser in incognito mode'''
    return Browser('chrome',
                #    headless=True,
                   incognito=True,
                   executable_path=CHROME_DRIVER)
# end def

def solve_captcha(image):
    '''get captcha code from image url'''
    return CaptchaSolver('browser').solve_captcha(image)
# end def
