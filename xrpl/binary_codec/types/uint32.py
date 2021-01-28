"""Derived UInt class for serializing/deserializing 32 bit UInt."""
from xrpl.binary_codec.exceptions import XRPLBinaryCodecException
from xrpl.binary_codec.types import UInt

_WIDTH = 4  # 32 / 8


class UInt32(UInt):
    """Derived UInt class for serializing/deserializing 32 bit UInt."""

    def __init__(self, buffer=bytes(_WIDTH)):
        """Construct a new UInt32 type from a `bytes` value."""
        super().__init__(buffer)

    @classmethod
    def from_parser(cls, parser):
        """Construct a new UInt32 type from a BinaryParser."""
        return cls(parser.read(_WIDTH))

    @classmethod
    def from_value(cls, value):
        """Construct a new UInt32 type from a number."""
        if isinstance(value, int):
            value_bytes = (value).to_bytes(_WIDTH, byteorder="big", signed=False)
            return cls(value_bytes)

        raise XRPLBinaryCodecException("Cannot construct UInt32 from given value")