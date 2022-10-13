from typing import Union

from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo=0, **kwargs):
        super().__init__(agencia, conta, saldo, **kwargs)
        self.extrato = list()


    def saque(self, valor:Union[str, int]):
        valor = self._normalize_value(valor)
        if valor < 0:
            raise ValueError('Valor não pode ser negativo!')
        if self._saldo < valor:
            raise ValueError('Saldo insuficiente!')
        self._saldo -= valor
        self.extrato.append(('Saque', valor))
        self.detalhes()
        return self._saldo, self.extrato
