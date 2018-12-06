from types import SimpleNamespace

from cnab240.cnab240Itau import Itau
from cnab240.cnab240Original import Original

ITAU = '341'
BRASIL = '001'
ORIGINAL = '212'


class Cnab240:
    '''
    classe para leitura do arquivo padrao CNAB240 - SISPAG
    :param arquivo: nome do arquivo
    '''

    def __init__(self, arquivo):
        self.arquivo = arquivo

        try:
            f = open(self.arquivo, 'r')
        except FileNotFoundError:
            raise FileNotFoundError('File {} not found.'.format(arquivo))
        except ValueError as e:
            raise ValueError(str(e))

        self.lines = f.readlines()
        f.close()

        self.codigo_banco = self.__codigo_banco(self.lines[0])

    def processar(self):
        header = None
        header_lote = None
        registro_a = []
        for l in self.lines:

            tipo_registro = self.__tipo_registro(l)
            if tipo_registro == '0':
                header = self.__header(l)
            elif tipo_registro == '1':
                header_lote = self.__header_lote(l)
            elif tipo_registro == '3':
                registro_a.append(self.__registro_a(l))
        return SimpleNamespace(
            header=header,
            header_lote=header_lote,
            registros_a=registro_a,
        )

    def __tipo_registro(self, line):
        return line[7:8]

    def __codigo_banco(self, line):
        return line[0:3]

    def __header(self, line):
        if self.codigo_banco == ITAU:
            return Itau.header(line)
        elif self.codigo_banco == ORIGINAL:
            return Original.header(line)
        else:
            raise NotImplementedError

    def __header_lote(self, line):
        if self.codigo_banco == ITAU:
            return Itau.header_lote(line)
        elif self.codigo_banco == ORIGINAL:
            return Original.header_lote(line)
        else:
            raise NotImplementedError

    def __registro_a(self, line):
        if self.codigo_banco == ITAU:
            return Itau.registro_a(line)
        elif self.codigo_banco == ORIGINAL:
            return Original.registro_a(line)
        else:
            raise NotImplementedError
