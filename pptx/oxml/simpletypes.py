# encoding: utf-8

"""
Simple type classes, providing validation and format translation for values
stored in XML element attributes. Naming generally corresponds to the simple
type in the associated XML schema.
"""

from __future__ import absolute_import

from ..util import Emu


class BaseSimpleType(object):

    @classmethod
    def from_xml(cls, str_value):
        return cls.convert_from_xml(str_value)

    @classmethod
    def to_xml(cls, value):
        cls.validate(value)
        str_value = cls.convert_to_xml(value)
        return str_value

    @classmethod
    def validate_int(cls, value):
        if not isinstance(value, int):
            raise TypeError(
                "value must be <type 'int'>, got %s" % type(value)
            )

    @classmethod
    def validate_int_in_range(cls, value, min_inclusive, max_inclusive):
        cls.validate_int(value)
        if value < min_inclusive or value > max_inclusive:
            raise ValueError(
                "value must be in range %d to %d inclusive, got %d" %
                (min_inclusive, max_inclusive, value)
            )

    @classmethod
    def validate_string(cls, value):
        if isinstance(value, str):
            return value
        try:
            if isinstance(value, basestring):
                return value
        except NameError:  # means we're on Python 3
            pass
        raise TypeError(
            "value must be a string, got %s" % type(value)
        )


class BaseStringType(BaseSimpleType):

    @classmethod
    def convert_from_xml(cls, str_value):
        return str_value

    @classmethod
    def convert_to_xml(cls, value):
        return value

    @classmethod
    def validate(cls, value):
        cls.validate_string(value)


class BaseIntType(BaseSimpleType):

    @classmethod
    def convert_from_xml(cls, str_value):
        return int(str_value)

    @classmethod
    def convert_to_xml(cls, value):
        return str(value)

    @classmethod
    def validate(cls, value):
        cls.validate_int(value)


class XsdString(BaseStringType):
    pass


class XsdUnsignedInt(BaseIntType):

    @classmethod
    def validate(cls, value):
        cls.validate_int_in_range(value, 0, 4294967295)


class ST_Coordinate32(BaseIntType):
    pass


class ST_HexColorRGB(BaseStringType):

    @classmethod
    def convert_to_xml(cls, value):
        """
        Keep alpha characters all uppercase just for consistency.
        """
        return value.upper()

    @classmethod
    def validate(cls, value):
        # must be string ---------------
        str_value = cls.validate_string(value)

        # must be 6 chars long----------
        if len(str_value) != 6:
            raise ValueError(
                "RGB string must be six characters long, got '%s'"
                % str_value
            )

        # must parse as hex int --------
        try:
            int(str_value, 16)
        except ValueError:
            raise ValueError(
                "RGB string must be valid hex string, got '%s'"
                % str_value
            )


class ST_Percentage(BaseIntType):
    """
    String value can be either an integer, representing 1000ths of a percent,
    or a floating point literal with a '%' suffix.
    """
    @classmethod
    def convert_from_xml(cls, str_value):
        if '%' in str_value:
            return cls._convert_from_percent_literal(str_value)
        return int(str_value)

    @classmethod
    def _convert_from_percent_literal(cls, str_value):
        float_part = str_value[:-1]  # trim off '%' character
        percent_value = float(float_part)
        int_value = int(round(percent_value * 1000))
        return int_value


class ST_SlideId(XsdUnsignedInt):

    @classmethod
    def validate(cls, value):
        cls.validate_int_in_range(value, 256, 2147483647)


class ST_SlideSizeCoordinate(BaseIntType):

    @classmethod
    def convert_from_xml(cls, str_value):
        return Emu(str_value)

    @classmethod
    def validate(cls, value):
        cls.validate_int(value)
        if value < 914400 or value > 51206400:
            raise ValueError(
                "value must be in range(914400, 51206400) (1-56 inches), got"
                " %d" % value
            )