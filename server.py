#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implements grpc modules"""
import time
import grpc
import service.service_pb2 as bot_pb
from service import service_pb2_grpc
from EshebaBot.esheba import EshebaBot
from concurrent.futures import ThreadPoolExecutor

class BotService(service_pb2_grpc.BotServiceServicer):

    bots = dict()

    def StartSession(self, request, context):
        bot = EshebaBot()
        bot.start_session()
        self.bots[bot.token] = bot  # cache bot
        return bot_pb.SessionStartResponse(
            session=bot.token,
            captcha_url=bot.get_captcha_url()
        )
    # end def

    def CloseSession(self, request, context):
        """Closes a session
        """
        session = request.session
        if session not in self.bots:
            return bot_pb.StatusResponse(status=500, message='Invalid session')
        # end if
        self.bots[session].close_session()
        return bot_pb.StatusResponse(status=200, message='OK')
    # end def

    def Login(self, request, context):
        session = request.session
        if session not in self.bots:
            return bot_pb.StatusResponse(status=500, message='Invalid session')
        # end if
        error = self.bots[session].login(
            usermail=request.usermail,
            password=request.password,
            security_code=request.security_code
        )
        return bot_pb.StatusResponse(
            status=500 if error else 200,
            message=error or 'OK'
        )
    # end def

    def CheckSession(self, request, context):
        session = request.session
        if session not in self.bots:
            return bot_pb.StatusResponse(status=500, message='Invalid session')
        # end if
        r = self.bots[session].check_session()
        return bot_pb.StatusResponse(
            status=200 if r else 401,
            message='OK' if r else 'Not logged in'
        )
    # end def

    def GetPersonalInfos(self, request, context):
        session = request.session
        if session not in self.bots:
            return bot_pb.PersonalInformations()
        # end if
        info = self.bots[session].get_personal_info()
        return bot_pb.PersonalInformations(**info)
    # end def
# end class


def run_server():
    '''Runs the grpc server'''
    port = '5000'
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_BotServiceServicer_to_server(BotService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print('Server running at http://localhost:%s' % port)
    while True:
        time.sleep(100)
    # end white
    input('Press enter to stop the server...')
    server.stop(True)
# end def

if __name__ == '__main__':
    run_server()
# end if
