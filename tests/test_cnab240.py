from types import SimpleNamespace

import pytest
from cnab240.cnab240 import Cnab240
import datetime
from decimal import Decimal


def test_parameter():
    with pytest.raises(TypeError) as e:
        Cnab240()
        if not (str(e.value)) == "__init__() missing 1 required positional arguments: 'file_name'":
            AssertionError()

    with pytest.raises(FileNotFoundError):
        Cnab240('test.txt')


def test_instance_variables(cnab240):
    assert cnab240.file
    assert cnab240.lines
    assert cnab240.code_bank


def test_tipo_registro(cnab240):
    assert cnab240._Cnab240__record_type('00000001') == '1'


def test_codigo_banco(cnab240):
    assert cnab240._Cnab240__code_bank('00000001') == '000'


def test_header_not_implemented(cnab240_not_implemented):
    with pytest.raises(NotImplementedError):
        cnab240_not_implemented._Cnab240__header('000')


def test_header(cnab240):
    data = '21200000         29999999999999929                  00001 0000009999999 xxxxxxxxxxxxxxxxxxxx          BANCO ORIGINAL                          114092018000000001212100                                                                          '
    expect = SimpleNamespace(
        cnpj_cpf='99999999999999',
        codigo_banco='212',
        codigo_lote='0000',
        dac_agencia='',
        data_arquivo='14092018',
        densidade_arquivo='',
        hora_arquivo='000000',
        nome_banco='BANCO ORIGINAL',
        nome_empresa='xxxxxxxxxxxxxxxxxxxx',
        nro_agencia_debitada='00001',
        nro_conta_debitada='000000999999',
        tipo_arquivo='1',
        tipo_inscricao='2',
        tipo_registro='0',
        versao_layout=''
    )
    assert cnab240._Cnab240__header(data) == expect


def test_header_lote_not_implemented(cnab240_not_implemented):
    with pytest.raises(NotImplementedError):
        cnab240_not_implemented._Cnab240__header_lote('000')


def test_header_lote(cnab240):
    data = '21200011C2041045 200000000000000                    00001 0000009474544 xxxxxxxxxxxxxxxxxxxx                                                                                                                                                    '
    expect = SimpleNamespace(cep='',
                             cidade='',
                             cnpj_cpf='00000000000000',
                             codigo_banco='212',
                             codigo_lote='0001',
                             complemento='',
                             complemento_historico='',
                             complemento_ident='',
                             dac_agencia='',
                             estado='',
                             finalidade='',
                             forma_pagamento='41',
                             ident_extrado='',
                             logradouro='',
                             nome_empresa='xxxxxxxxxxxxxxxxxxxx',
                             nro_agencia_debitada='00001',
                             nro_conta_debitada='000000947454',
                             numero='',
                             tipo_inscricao='2',
                             tipo_operacao='C',
                             tipo_pagamento='20',
                             tipo_registro='1',
                             versao_layout='045',
                             )
    assert cnab240._Cnab240__header_lote(data) == expect


def test_record_a_not_implemented(cnab240_not_implemented):
    with pytest.raises(NotImplementedError):
        cnab240_not_implemented._Cnab240__record_a('000')


def test_record_a(cnab240):
    data = '2120001300002A0     21200001 0000000659657 xxxxxxxxxxxxxxxxxxxxxxxxxxx   12122               17092018BRL               000000000050000                                                                     000000000000002                      '
    expect = SimpleNamespace(agencia_conta_favorecido='00001 0000000659657',
                             aviso_ao_favorecido='',
                             cnpj_cpf_favorecido='00000000000000',
                             codigo_banco='212',
                             codigo_banco_favorecido='212',
                             codigo_lote='0001',
                             codigo_ocorrencias='',
                             data_prevista_pag=datetime.datetime.strptime('17092018', '%d%m%Y'),
                             data_real_pagto='',
                             nome_favorecido='xxxxxxxxxxxxxxxxxxxxxxxxxxx',
                             nosso_numero='',
                             nro_doc='12122',
                             nro_doc_ted_op='',
                             nro_nota_fiscal='',
                             nro_registro='00002',
                             segmento='A',
                             tipo_inscricao='2',
                             tipo_moeda='BRL',
                             tipo_movimento='0',
                             tipo_registro='3',
                             valor_previsto=Decimal(500.00),
                             valor_real_pagto=''
                             )

    assert cnab240._Cnab240__record_a(data) == expect


def test_processar(cnab240):
    result = cnab240.process()
    assert result.header
    assert result.header_lote
    assert result.record_a
