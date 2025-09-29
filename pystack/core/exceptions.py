from pystack.core.base import ProtocolStateBase


class InvalidProtocolStateError(Exception):
    """
    Raised when a state is passed to a protocol that
    does not belong to its allowed state enum.
    """
    def __init__(self, expected_enum: type[ProtocolStateBase], received_state: ProtocolStateBase):
        message = (
            f"Invalid protocol state: {received_state}, "
            f"expected instance of {expected_enum.__name__}"
        )
        super().__init__(message)
        self.expected_enum = expected_enum
        self.received_state = received_state