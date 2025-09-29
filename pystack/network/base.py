import ipaddress

from typing import Union

IPAddress = Union[ipaddress.IPv4Address, ipaddress.IPv6Address]

class Address:
    """Generic network address."""
    def __init__(self, ip: IPAddress, port: int = None):
        self.ip = ip
        self.port = port
        self.validate()

    def validate(self):
        if not isinstance(self.ip, (ipaddress.IPv4Address, ipaddress.IPv6Address)):
            raise ValueError(f"Invalid IP address type: {type(self.ip)}")
        if self.port is not None and not (0 <= self.port <= 65535):
            raise ValueError(f"Invalid port: {self.port}, must be in range 0-65535")

    def __str__(self):
        return f"{self.ip}:{self.port}" if self.port else str(self.ip)

    def to_tuple(self):
        return (self.ip, self.port) if self.port else (self.ip,)