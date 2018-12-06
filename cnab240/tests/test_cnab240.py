import pytest
from cnab240.cnab240 import Cnab240


def test_parameter():
    with pytest.raises(TypeError) as e:
        Cnab240()
        if not (str(e.value)) == "__init__() missing 1 required positional arguments: 'file_name'":
            AssertionError()

    with pytest.raises(FileNotFoundError):
        Cnab240('test.txt')


def test_tipo_registro(cnab240):
    assert cnab240._Cnab240__tipo_registro('00000001') == '1'


def test_codigo_banco(cnab240):
    assert cnab240._Cnab240__codigo_banco('00000001') == '000'


def test_header(cnab240):
    data = '21200000         29999999999999929                  00001 0000009999999 xxxxxxxxxxxxxxxxxxxx          BANCO ORIGINAL                          114092018000000001212100                                                                          '

    #assert cnab240._Cnab240__header(data)
