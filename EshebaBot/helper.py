#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Helper methods used in crawling"""
import json
from os import path, makedirs
from splinter import Browser

CHROME_DRIVER = path.join('lib', 'chromedriver')


def get_browser():
    '''open a headless chrome browser in incognito mode'''
    return Browser('chrome',
                   headless=True,
                   incognito=True,
                   executable_path=CHROME_DRIVER)
# end def
