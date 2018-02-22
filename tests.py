#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test grpc modules"""
import sys
import grpc
import requests
from service import service_pb2_grpc
import service.service_pb2 as bot_pb
from EshebaBot.helper import solve_captcha


def run_tests(usermail=None, password=None):
    '''Runs the grpc server'''
    channel = grpc.insecure_channel('localhost:5000')
    stub = service_pb2_grpc.BotServiceStub(channel)

    # start session
    r = stub.StartSession(bot_pb.EmptyRequest())
    session = r.session

    if not (usermail or password):
        print('Provide usermail and password to test login')
    else:
        # solve captcha
        r = requests.get(r.captcha_url, verify=False)
        security_code = solve_captcha(r.content)

        #login
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

    print()
    print('All tests passed.')
# end def

if __name__ == '__main__':
    run_tests()
# end if
