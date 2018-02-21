#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Helper methods used in crawling"""
import io
import json
from PIL import Image
from os import path, makedirs
from splinter import Browser
import tesserocr as ocr

CHROME_DRIVER = path.join('lib', 'chromedriver')


def get_browser():
    '''open a headless chrome browser in incognito mode'''
    return Browser('chrome',
                #    headless=True,
                   incognito=True,
                   executable_path=CHROME_DRIVER)
# end def

def solve_captcha(image_bytes):
    '''get captcha code from image url'''
    image = Image.open(io.BytesIO(image_bytes))
    api = ocr.PyTessBaseAPI()
    api.SetVariable("tessedit_char_whitelist", "0123456789")
    api.SetPageSegMode(ocr.PSM.SINGLE_WORD)
    api.SetImage(image)
    api.Recognize()
    return api.GetUTF8Text()
# end def
