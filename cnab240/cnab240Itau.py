from types import SimpleNamespace


class Itau:
    @staticmethod
    def header(line):
        return SimpleNamespace(
            codigo_banco=line[0:3],
            codigo_lote=line[3:7],
            tipo_registro=line[7:8],
            # brancos = line[8:14],
            versao_layout=line[14:17],
            tipo_doc=line[17:18],
            cnpj=line[18:32],
            # brancos = line[32:52],
            nro_agencia_debitada=line[52:57],
            # brancos = line[57:58],
            nro_conta_debitada=line[58:70],
            # brancos = line[70:71],
            dac_agencia=line[71:72],
            nome_empresa=line[72:102],
            nome_banco=line[102:132],
            # brancos = line[132:142],
            tipo_arquivo=line[142:143],
            data_arquivo=line[143:151],
            hora_arquivo=line[151:157],
            # zeros = line[157:166],
            densidade_arquivo=line[166:171],
            # brancos = line[171:240]
        )

    @staticmethod
    def header_lote(line):
        return SimpleNamespace(
            codigo_banco=line[0:3],
            codigo_lote=line[3:7],
            tipo_registro=line[7:8],
            tipo_operacao=line[8:9],
            tipo_pagamento=line[9:11],
            forma_pagamento=line[11:13],
            versao_layout=line[13:16],
            # brancos = line[16:17],
            tipo_inscricao=line[17:18],
            cnpj=line[18:32],
            ident_extrado=line[32:36],
            complemento_ident=line[36:52],
            nro_agencia_debitada=line[52:57],
            # brancos = line[57:58]
            nro_conta_debitada=line[58:70],
            # brancos = line[70:71],
            dac_agencia=line[71:72],
            nome_empresa=line[72:102],
            finalidade=line[102:132],
            complemento_historico=line[132:142],
            logradouro=line[142:172],
            numero=line[172:177],
            complemento=line[177:192],
            cidade=line[192:212],
            cep=line[212:220],
            estado=line[220:222],
            # brancos=line[222:230],
            # ocorrencias=line[230:240],
        )

    @staticmethod
    def registro_a(line):
        return SimpleNamespace(
            codigo_banco=line[0:3],
            codigo_lote=line[3:7],
            tipo_registro=line[7:8],
            nro_registro=line[8:13],
            segmento=line[13:14],
            tipo_movimento=line[14:17],
            #complemento=line[17:20],
            codigo_banco_favorecido=line[20:23],
            agencia_conta_favorecido=line[23:43],
            nome_favorecido=line[43:73],
            nro_doc=line[73:93],
            data_prevista_pag=line[93:101],
            tipo_moeda=line[101:104],
            #complemento=line[104:119],
            valor_previsto=line[119:134],
            nosso_numero=line[134:149],
            #complemento=line[149:154],
            data_real_pagto=line[154:162],
            valor_real_pagto=line[162:177],
            nro_nota_fiscal=line[177:191],
            #complemento=line[191:197],
            nro_doc_ted_op=line[197:203],
            cnpj_cpf_favorecido=line[203:217],
            tipo_identificacao_favorecido=line[217:218],
            #complemento=line[218:229],
            aviso_ao_favorecido=line[229:230],
            codigo_ocorrencias=line[230:240],
        )
