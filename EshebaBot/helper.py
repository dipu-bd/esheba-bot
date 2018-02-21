#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Helper methods used in crawling"""
from captcha_solver import CaptchaSolver

def solve_captcha(image):
    '''get captcha code from image url'''
    return CaptchaSolver('browser').solve_captcha(image)
# end def
