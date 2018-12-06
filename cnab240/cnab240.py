from types import SimpleNamespace

from cnab240.cnabitau import Itau

ITAU = '212'
BRASIL = '001'
ORIGINAL = '212'


class Cnab240:
    '''
    classe para leitura do arquivo padrao CNAB240 - SISPAG
    :param file_name: nome do arquivo
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
                header = SimpleNamespace(header=self.__header(l))
            elif tipo_registro == '1':
                header_lote = SimpleNamespace(header_lote=self.__header_lote(l))
            elif tipo_registro == 'A':
                pass

    def __tipo_registro(self, line):
        return line[7:8]

    def __codigo_banco(self, line):
        return line[0:3]

    def __header(self, line):
        if self.codigo_banco == ITAU:
            return Itau.header(line)
        else:
            raise NotImplementedError

    def __header_lote(self, line):
        if self.codigo_banco == ITAU:
            return Itau.header_lote(line)
        else:
            raise NotImplementedError

    def __registro_a(self, line):
        if self.codigo_banco == ITAU:
            return Itau.registroA(line)
        else:
            raise NotImplementedError
