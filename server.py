#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implements grpc modules"""
import grpc
import service.service_pb2 as BotPB
from service import service_pb2_grpc
from concurrent.futures import ThreadPoolExecutor

class BotService(service_pb2_grpc.BotServiceServicer):

  def StartSession(self, request, context):
    pass
  # end def

  def Login(self, request, context):
    pass
  # end def

  def CheckSession(self, request, context):
    pass
  # end def

  def GetPersonalInfos(self, request, context):
    pass
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
  input('Press enter to stop the server...')
  server.stop(True)
# end def

if __name__ == '__main__':
  run_server()
# end if
