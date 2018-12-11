from types import SimpleNamespace
from cnab240.utils import format_date, format_currency

class Itau:
    @staticmethod
    def header(line):
        return SimpleNamespace(
            codigo_banco=line[0:3].strip(' '),
            codigo_lote=line[3:7].strip(' '),
            tipo_registro=line[7:8].strip(' '),
            # brancos = line[8:14],
            versao_layout=line[14:17].strip(' '),
            tipo_doc=line[17:18].strip(' '),
            cnpj=line[18:32].strip(' '),
            # brancos = line[32:52],
            nro_agencia_debitada=line[52:57].strip(' '),
            # brancos = line[57:58],
            nro_conta_debitada=line[58:70].strip(' '),
            # brancos = line[70:71],
            dac_agencia=line[71:72].strip(' '),
            nome_empresa=line[72:102].strip(' '),
            nome_banco=line[102:132].strip(' '),
            # brancos = line[132:142],
            tipo_arquivo=line[142:143].strip(' '),
            data_arquivo=line[143:151].strip(' '),
            hora_arquivo=line[151:157].strip(' '),
            # zeros = line[157:166],
            densidade_arquivo=line[166:171].strip(' '),
            # brancos = line[171:240]
        )

    @staticmethod
    def header_lote(line):
        return SimpleNamespace(
            codigo_banco=line[0:3].strip(' '),
            codigo_lote=line[3:7].strip(' '),
            tipo_registro=line[7:8].strip(' '),
            tipo_operacao=line[8:9].strip(' '),
            tipo_pagamento=line[9:11].strip(' '),
            forma_pagamento=line[11:13].strip(' '),
            versao_layout=line[13:16].strip(' '),
            # brancos = line[16:17],
            tipo_inscricao=line[17:18].strip(' '),
            cnpj=line[18:32].strip(' '),
            ident_extrado=line[32:36].strip(' '),
            complemento_ident=line[36:52].strip(' '),
            nro_agencia_debitada=line[52:57].strip(' '),
            # brancos = line[57:58]
            nro_conta_debitada=line[58:70].strip(' '),
            # brancos = line[70:71],
            dac_agencia=line[71:72].strip(' '),
            nome_empresa=line[72:102].strip(' '),
            finalidade=line[102:132].strip(' '),
            complemento_historico=line[132:142].strip(' '),
            logradouro=line[142:172].strip(' '),
            numero=line[172:177].strip(' '),
            complemento=line[177:192].strip(' '),
            cidade=line[192:212].strip(' '),
            cep=line[212:220].strip(' '),
            estado=line[220:222].strip(' '),
            # brancos=line[222:230],
            # ocorrencias=line[230:240],
        )

    @staticmethod
    def record_a(line):
        return SimpleNamespace(
            codigo_banco=line[0:3].strip(' '),
            codigo_lote=line[3:7].strip(' '),
            tipo_registro=line[7:8].strip(' '),
            nro_registro=line[8:13].strip(' '),
            segmento=line[13:14].strip(' '),
            tipo_movimento=line[14:17].strip(' '),
            #complemento=line[17:20],
            codigo_banco_favorecido=line[20:23].strip(' '),
            agencia_conta_favorecido=line[23:43].strip(' '),
            nome_favorecido=line[43:73].strip(' '),
            nro_doc=line[73:93].strip(' '),
            data_prevista_pag=format_date(line[93:101].strip(' ')),
            tipo_moeda=line[101:104].strip(' '),
            #complemento=line[104:119],
            valor_previsto=format_currency(line[119:134].strip(' ')),
            nosso_numero=line[134:149].strip(' '),
            #complemento=line[149:154],
            data_real_pagto=line[154:162].strip(' '),
            valor_real_pagto=line[162:177].strip(' '),
            nro_nota_fiscal=line[177:191].strip(' '),
            #complemento=line[191:197],
            nro_doc_ted_op=line[197:203].strip(' '),
            cnpj_cpf_favorecido=line[203:217].strip(' '),
            tipo_identificacao_favorecido=line[217:218].strip(' '),
            #complemento=line[218:229],
            aviso_ao_favorecido=line[229:230].strip(' '),
            codigo_ocorrencias=line[230:240].strip(' '),
        )
