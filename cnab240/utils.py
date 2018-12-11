import datetime
from decimal import Decimal, InvalidOperation


def format_date(date_str):
    '''
    format date
    :param date_str: date in the format ddmmyyyy
    :return: datetime
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
    format currency value
    :param value: value in format 0000000000 to two decimal places
    :return: Decimal
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
