#!/usr/bin/env python  
# -*- coding:utf-8 -*-
"""
@time: 2019/11/4 14:19

@author: ljyang
"""
from thrift.protocol import TBinaryProtocol
from thrift.protocol.TMultiplexedProtocol import TMultiplexedProtocol
from thrift.transport import TTransport, TSocket

from gen_py import Calculator
from gen_py.ttypes import CalParam, Operation


def main():
    # 以frame为单位进行传输，非阻塞式服务中使用
    transport = TTransport.TFramedTransport(TSocket.TSocket(host="127.0.0.1", port=9999))
    transport.open()
    # 序列化方式
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    multiplexedprotocol = TMultiplexedProtocol(protocol, "calService")

    client = Calculator.Client(multiplexedprotocol)
    param = CalParam(num1=1, num2=2, op=Operation.ADD)
    re = client.getResult(param)
    print(param)
    print(re)
    transport.close()


if __name__ == '__main__':
    main()
