from decimal import Decimal, InvalidOperation
import datetime

import pytest
from cnab240.utils import format_currency, format_date


def test_format_date():
    expect_date = datetime.datetime.strptime('01122018', '%d%m%Y')
    date_str = '01122018'
    assert format_date(date_str) == expect_date


def test_value_err_format_date():
    with pytest.raises(ValueError):
        format_date(0)

    with pytest.raises(ValueError):
        format_date('1')


def test_format_currency():
    value_str = '0000060000'
    assert format_currency(value_str) == Decimal(600.00)


def test_value_err_format_currency():
    with pytest.raises(ValueError):
        format_currency(0)

    with pytest.raises(InvalidOperation):
        format_currency('00004aa0')
