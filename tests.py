#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test grpc modules"""
import io
import sys
import time
import grpc
import psutil
import requests
from service import service_pb2_grpc
import service.service_pb2 as bot_pb
from EshebaBot.esheba import EshebaBot
from PIL import Image

def solve_captcha(byte_str):
    im = Image.open(io.BytesIO(byte_str))
    im.show(title='Enter the code of this captcha')
    code = input('Captcha: ')
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()
        # end if
    # end for
    return code
# end def

def direct_test():
    '''test if the service works'''
    bot = EshebaBot()
    print('Starting Session')
    bot.start_session()
    print('Session ID =', bot.token)
    print('Captcha =', bot.captcha)
    captcha_url = bot.get_captcha_url()
    r = bot.session.get(captcha_url, verify=False)
    usermail = input('User email: ')
    password = input('Password: ')
    security_code = solve_captcha(r.content)
    r = bot.login(usermail, password, security_code)
    print('Login response =', r if r else 'No Errors')
    r = bot.get_personal_info()
    print('Personal informations =', r)
    r = bot.check_session()
    print('Session check =', r)
    bot.close_session()
    print('Session closed')
# end def

def run_tests():
    '''Runs the grpc server'''
    channel = grpc.insecure_channel('localhost:5000')
    stub = service_pb2_grpc.BotServiceStub(channel)

    # start session
    r = stub.StartSession(bot_pb.EmptyRequest())
    session = r.session

    # get user
    usermail = input('User email: ')
    password = input('Password: ')
    
    # solve captcha
    r = requests.get(r.captcha_url, verify=False)
    security_code = solve_captcha(r.content)

    # login
    r = stub.Login(bot_pb.LoginRequest(
        session=session,
        usermail=usermail,
        password=password,
        security_code=security_code
    ))
    print('Login:', r.status, r.message)
    # end if

    # check session
    r = stub.CheckSession(bot_pb.SessionRequest(session=session))
    print('Check Session:', r.status, r.message)
    if r.status == 200:
        # get personal informations
        r = stub.GetPersonalInfos(bot_pb.SessionRequest(session=session))
        print('Personal Informations:\n')
        print(r)
    # end if

    # close session
    r = stub.CloseSession(bot_pb.SessionRequest(session=session))
    print('Close session:', r.status, r.message)

    print()
    print('All tests passed.')
# end def

if __name__ == '__main__':
    run_tests()
# end if
