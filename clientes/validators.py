from rest_framework import serializers
from clientes.valida_cpf import validate
import re


def cpf_valido(cpf):
    return validate(cpf)


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(rg):
    return len(rg) < 9


def celular_valido(celular):
    '''Valida número de celular ((000) 000-0000)'''
    modelo1 = r'[(]{0,1}[0-9]{3}[)]{0,1} [0-9]{3}[-]{0,1}[0-9]{4}'
    modelo2 = r'[(]{0,1}[\d]{2}[)]{0,1} [\d]{5}[-]{0,1}[\d]{4}'
    c = re.compile('|'.join([modelo1, modelo2]))
    resposta = c.match(celular)
    return resposta
 