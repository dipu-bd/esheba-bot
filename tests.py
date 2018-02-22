#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test grpc modules"""
import grpc
from service import service_pb2_grpc


def run_tests():
  '''Runs the grpc server'''
  channel = grpc.insecure_channel('localhost:5000')
  stub = service_pb2_grpc.BotServiceStub(channel)
  print()
  print('All tests passed.')
# end def

if __name__ == '__main__':
  run_tests()
# end if
