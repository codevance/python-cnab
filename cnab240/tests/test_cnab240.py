import pytest
from cnab240.cnab240 import Cnab240


def test_parameter():
    with pytest.raises(TypeError) as e:
        Cnab240()
        if not (str(e.value)) == "__init__() missing 2 required positional arguments: 'file_name' and 'bank'":
            AssertionError()

    with pytest.raises(FileNotFoundError):
        Cnab240('test.txt', '341')

    with pytest.raises(ValueError):
        Cnab240('test.txt', '999')
