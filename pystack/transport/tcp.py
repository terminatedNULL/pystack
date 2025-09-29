"""
Transmission Control Protocol (TCP) implementation.
"""
from abc import ABC
from enum import auto

from pystack.core.base import ProtocolStateBase, StatefulProtocolBase, ProtocolCategory


class TCPState(ProtocolStateBase):
    CLOSED = auto()
    LISTEN = auto()
    SYN_SENT = auto()
    SYN_RECEIVED = auto()
    ESTABLISHED = auto()
    FIN_WAIT_1 = auto()
    FIN_WAIT_2 = auto()
    CLOSE_WAIT = auto()
    TIME_WAIT = auto()
    CLOSING = auto()
    LAST_ACK = auto()

    def is_terminal(self) -> bool:
        return self in (self.CLOSED, self.TIME_WAIT)

class TCP(StatefulProtocolBase, ABC):
    state_enum = TCPState
    protocol_type = ProtocolCategory.TRANSPORT

    def __init__(self):
        super().__init__(TCPState.CLOSED)
