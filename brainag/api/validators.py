# validators.py
import re

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return False

    soma = sum(int(dig) * (10 - i) for i, dig in enumerate(cpf[:-2]))
    primeiro_digito = 11 - (soma % 11)
    primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

    if primeiro_digito != int(cpf[-2]):
        return False

    soma = sum(int(dig) * (11 - i) for i, dig in enumerate(cpf[:-1]))
    segundo_digito = 11 - (soma % 11)
    segundo_digito = 0 if segundo_digito > 9 else segundo_digito

    return segundo_digito == int(cpf[-1])


def validar_cnpj(cnpj):

    cnpj = re.sub(r'\D', '', cnpj)

    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14 or cnpj == cnpj[0] * len(cnpj):
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(dig) * (5 if i < 12 else 6) for i, dig in enumerate(cnpj[:-2]))
    primeiro_digito = (soma % 11)
    primeiro_digito = 0 if primeiro_digito < 2 else 11 - primeiro_digito

    if primeiro_digito != int(cnpj[12]):
        return False

    # Cálculo do segundo dígito verificador
    soma = sum(int(dig) * (6 if i < 13 else 7) for i, dig in enumerate(cnpj[:-1]))
    segundo_digito = (soma % 11)
    segundo_digito = 0 if segundo_digito < 2 else 11 - segundo_digito

    return segundo_digito == int(cnpj[13])
