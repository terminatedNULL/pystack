from abc import abstractmethod, ABC
from enum import Enum

from pystack.core.exceptions import InvalidProtocolStateError


class ProtocolCategory(Enum):
    PHYSICAL = "Physical"             # PhySTACK
    LINK = "Link"                     # LinkSTACK
    BLUETOOTH = "Bluetooth"           # BlueSTACK
    NETWORK = "Network"               # NetSTACK
    TRANSPORT = "Transport"           # TranSTACK
    TUNNEL = "Tunnel"                 # TunnelSTACK
    ROUTING = "Routing"               # RouteSTACK
    SECURITY = "Security"             # SecSTACK
    MANAGEMENT = "Management"         # MgmtSTACK
    APPLICATION = "Application"       # AppSTACK
    DIAGNOSTICS = "Diagnostics"       # DiagSTACK


class ProtocolStateBase(Enum):
    """
    Base class for all protocol state enums.
    Protocol-specific states should inherit from this.
    """

    def is_terminal(self) -> bool:
        """
        Optional method to mark terminal / closed states.

        Returns:
            bool: Whether a given state is terminal.
        """
        return False

class ProtocolBase(ABC):
    """Generic base protocol."""
    protocol_type: ProtocolCategory

    def send(self, data: bytes):
        """Send data if applicable."""
        raise NotImplementedError

    def receive(self) -> bytes:
        """Receive data if applicable."""
        raise NotImplementedError

    def process_event(self, event):
        """Handle protocol-specific events."""
        pass

class StatefulProtocolBase(ProtocolBase):
    """
    Base class for protocols that maintain internal states.
    """

    state_enum: type[ProtocolStateBase]

    def __init__(self, initial_state: ProtocolStateBase):
        if not isinstance(initial_state, self.state_enum):
            raise InvalidProtocolStateError(self.state_enum, initial_state)
        self.state = initial_state

    @abstractmethod
    def change_state(self, new_state: ProtocolStateBase):
        """Method to update the protocol state."""
        if not isinstance(new_state, self.state_enum):
            raise InvalidProtocolStateError(self.state_enum, new_state)
        self.state = new_state

class StatelessProtocolBase(ProtocolBase):
    """
    Base class for protocols that do not maintain internal states.
    """
    pass
