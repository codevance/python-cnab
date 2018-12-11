from types import SimpleNamespace

from cnab240.cnab240Itau import Itau
import datetime
from decimal import Decimal


def test_header():
    data = '34100000         29999999999999929                  00001 0000009999999 xxxxxxxxxxxxxxxxxxxx          BANCO ITAU                              114092018000000001212100                                                                          '
    expect = SimpleNamespace(
        cnpj='99999999999999',
        codigo_banco='341',
        codigo_lote='0000',
        dac_agencia='',
        data_arquivo='14092018',
        densidade_arquivo='',
        hora_arquivo='000000',
        nome_banco='BANCO ITAU',
        nome_empresa='xxxxxxxxxxxxxxxxxxxx',
        nro_agencia_debitada='00001',
        nro_conta_debitada='000000999999',
        tipo_arquivo='1',
        tipo_doc='2',
        tipo_registro='0',
        versao_layout=''
    )
    assert Itau().header(data) == expect


def test_header_lote():
    data = '34100011C2041045 200000000000000                    00001 0000009474544 xxxxxxxxxxxxxxxxxxxx                                                                                                                                                    '
    expect = SimpleNamespace(cep='',
                             cidade='',
                             cnpj='00000000000000',
                             codigo_banco='341',
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
    assert Itau().header_lote(data) == expect


def test_record_a():
    data = '3410001300002A0     21200001 0000000659657 xxxxxxxxxxxxxxxxxxxxxxxxxxx   12122               17092018BRL               000000000050000                                                                     000000000000002                      '
    expect = SimpleNamespace(agencia_conta_favorecido='00001 0000000659657',
                             aviso_ao_favorecido='',
                             cnpj_cpf_favorecido='00000000000000',
                             codigo_banco='341',
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
                             tipo_identificacao_favorecido='2',
                             tipo_moeda='BRL',
                             tipo_movimento='0',
                             tipo_registro='3',
                             valor_previsto=Decimal(500.00),
                             valor_real_pagto=''
                             )

    assert Itau().record_a(data) == expect
