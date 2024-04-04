from rest_framework import serializers
from clientes.models import Cliente
from clientes.valida_cpf import validate
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def validate(self, data):
        if not cpf_valido(data["cpf"]):
            raise serializers.ValidationError({"cpf": "CPF Inválido!"})
        if not nome_valido(data["nome"]):
            raise serializers.ValidationError(
                {"nome": "Não inclua números neste campo."}
            )
        if not rg_valido(data["rg"]):
            raise serializers.ValidationError(
                {"rg": "Máximo de 9 dígitos neste campo."}
            )
        if not celular_valido(data["celular"]):
            raise serializers.ValidationError(
                {
                    "celular": "Número inválido! Formatos aceitos (000) 000-0000 | (00) 00000-0000."
                }
            )
        return data

    def validate_empty_values(self, data):
        return super().validate_empty_values(data)

    # def cpf_valido(self, cpf):
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError("CPF Inválido!")
    #     return cpf

    # def validate_cpf(self, cpf):
    #     if not validate(cpf):
    #         raise serializers.ValidationError("CPF Inválido!")
    #     return cpf

    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não inclua números neste campo.")
    #     return nome

    # def validate_rg(self, rg):
    #     if len(rg) > 9:
    #         raise serializers.ValidationError("Máximo de 9 dígitos neste campo.")
    #     return rg

    # def validate_celular(self, celular):
    #     if len(celular) > 14:
    #         raise serializers.ValidationError("Máximo de 14 dígitos neste campo.")
    #     return celular
