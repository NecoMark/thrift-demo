#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Operation(object):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

    _VALUES_TO_NAMES = {
        1: "ADD",
        2: "SUBTRACT",
        3: "MULTIPLY",
        4: "DIVIDE",
    }

    _NAMES_TO_VALUES = {
        "ADD": 1,
        "SUBTRACT": 2,
        "MULTIPLY": 3,
        "DIVIDE": 4,
    }


class calException(TException):
    """
    Attributes:
     - reason
    """


    def __init__(self, reason=None,):
        self.reason = reason

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.reason = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('calException')
        if self.reason is not None:
            oprot.writeFieldBegin('reason', TType.STRING, 1)
            oprot.writeString(self.reason.encode('utf-8') if sys.version_info[0] == 2 else self.reason)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CalParam(object):
    """
    Attributes:
     - num1
     - num2
     - op
    """


    def __init__(self, num1=None, num2=None, op=None,):
        self.num1 = num1
        self.num2 = num2
        self.op = op

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.num1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.num2 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.op = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('CalParam')
        if self.num1 is not None:
            oprot.writeFieldBegin('num1', TType.I32, 1)
            oprot.writeI32(self.num1)
            oprot.writeFieldEnd()
        if self.num2 is not None:
            oprot.writeFieldBegin('num2', TType.I32, 2)
            oprot.writeI32(self.num2)
            oprot.writeFieldEnd()
        if self.op is not None:
            oprot.writeFieldBegin('op', TType.I32, 3)
            oprot.writeI32(self.op)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(calException)
calException.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'reason', 'UTF8', None, ),  # 1
)
all_structs.append(CalParam)
CalParam.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'num1', None, None, ),  # 1
    (2, TType.I32, 'num2', None, None, ),  # 2
    (3, TType.I32, 'op', None, None, ),  # 3
)
fix_spec(all_structs)
del all_structs
