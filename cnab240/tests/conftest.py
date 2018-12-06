import pytest
from cnab240.cnab240 import Cnab240


@pytest.fixture
def cnab240():
    return Cnab240('cnab240/tests/cnab240_banco_original.txt')


@pytest.fixture
def cnab240_not_implemented():
    f=open('cnab240/tests/test.txt', 'w')
    f.write('999')
    f.close()
    return Cnab240('cnab240/tests/test.txt')
