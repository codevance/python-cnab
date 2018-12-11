from decimal import Decimal, InvalidOperation

import pytest
from cnab240.utils import format_currency


def test_format_date():
    date_str = '01012018'
    pass


def test_format_currency():
    value_str = '0000060000'
    assert format_currency(value_str) == Decimal(600.00)


def test_value_erro_format_currency():
    with pytest.raises(ValueError):
        format_currency(0)

    with pytest.raises(InvalidOperation):
        format_currency('00004aa0')
