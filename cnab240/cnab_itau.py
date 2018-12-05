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
