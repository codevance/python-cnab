from cnab240.cnab_itau import Itau

ITAU = '341'
BRASIL = '001'
ORIGINAL = '212'
BANKS = (ITAU, BRASIL, ORIGINAL)


class Cnab240:
    def __init__(self, file_name, bank):

        if not bank in BANKS:
            raise ValueError()

        self.file_name = file_name
        self.bank = bank

        try:
            file = open(self.file_name, 'r')
        except FileNotFoundError:
            raise FileNotFoundError('File {} not found.'.format(file_name))

        self.lines = file.readlines()
        file.close()

        self.header = self.__header(self.lines[0])

    def __header(self, line):
        if self.bank == ITAU:
            return Itau.header(line)
        else:
            raise NotImplementedError
