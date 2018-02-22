#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test grpc modules"""
import sys
import grpc
import requests
from service import service_pb2_grpc
import service.service_pb2 as bot_pb
from EshebaBot.helper import solve_captcha


def run_tests():
    '''Runs the grpc server'''
    channel = grpc.insecure_channel('localhost:5000')
    stub = service_pb2_grpc.BotServiceStub(channel)

    # start session
    r = stub.StartSession(bot_pb.EmptyRequest())
    session = r.session

    if len(sys.argv) < 3:
        print('Provide usermail and password to test login')
    else:
        # solve captcha
        r = requests.get(r.captcha_url, verify=False)
        security_code = solve_captcha(r.content)

        #login
        usermail = sys.argv[1]
        password = sys.argv[2]
        r = stub.Login(bot_pb.LoginRequest(
            session=session,
            usermail=usermail,
            password=password,
            security_code=security_code
        ))
        print(r.status, r.message)
    # end if

    # check session
    r = stub.CheckSession(bot_pb.SessionRequest(session=session))
    print(r.status, r.message)
    if r.status == 200:
        print('Personal informations')

        # get personal informations
        r = stub.GetPersonalInfos(bot_pb.SessionRequest(session=session))
        print('Personal informations:')
        print(r)
    # end if

    print()
    print('All tests passed.')
# end def

if __name__ == '__main__':
    run_tests()
# end if
