import datetime
from decimal import Decimal, InvalidOperation


def format_date(date_str):
    '''

    :param date_str:
    :return:
    '''
    if not isinstance(date_str, str):
        raise ValueError

    try:
        result = datetime.datetime.strptime(date_str, '%d%m%Y')
    except ValueError:
        raise ValueError

    return result


def format_currency(value_str):
    '''

    :param value:
    :return:
    '''
    if not isinstance(value_str, str):
        raise ValueError

    tmp_value = value_str.lstrip('0')
    new_value = tmp_value[0:-2] + '.' + tmp_value[-2:]
    try:
        result = Decimal(new_value)
    except InvalidOperation:
        raise InvalidOperation

    return result
