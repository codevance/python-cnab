from types import SimpleNamespace

from cnab240.cnab240Itau import Itau
from cnab240.cnab240Original import Original

ITAU = '341'
BRASIL = '001'
ORIGINAL = '212'


class Cnab240:
    '''
    class for reading the file CNAB240 - SISPAG
    :param file: file name
    '''

    def __init__(self, file):
        self.file = file

        try:
            f = open(self.file, 'r')
        except FileNotFoundError:
            raise FileNotFoundError('File {} not found.'.format(file))
        except ValueError as e:
            raise ValueError(str(e))

        self.lines = f.readlines()
        f.close()

        self.code_bank = self.__code_bank(self.lines[0])

    def process(self):
        header = None
        header_lote = None
        record_a = []
        for l in self.lines:
            record_type = self.__record_type(l)
            if record_type == '0':
                header = self.__header(l)
            elif record_type == '1':
                header_lote = self.__header_lote(l)
            elif record_type == '3':
                record_a.append(self.__record_a(l))
        return SimpleNamespace(
            header=header,
            header_lote=header_lote,
            record_a=record_a,
        )

    def __record_type(self, line):
        return line[7:8]

    def __code_bank(self, line):
        return line[0:3]

    def __header(self, line):
        if self.code_bank == ITAU:
            return Itau.header(line)
        elif self.code_bank == ORIGINAL:
            return Original.header(line)
        else:
            raise NotImplementedError

    def __header_lote(self, line):
        if self.code_bank == ITAU:
            return Itau.header_lote(line)
        elif self.code_bank == ORIGINAL:
            return Original.header_lote(line)
        else:
            raise NotImplementedError

    def __record_a(self, line):
        if self.code_bank == ITAU:
            return Itau.record_a(line)
        elif self.code_bank == ORIGINAL:
            return Original.record_a(line)
        else:
            raise NotImplementedError
