import pytest
from cnab240.cnab240 import Cnab240


@pytest.fixture
def cnab240():
    return Cnab240('cnab240/tests/cnab240_banco_original.txt')
