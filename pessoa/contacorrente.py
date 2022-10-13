from typing import Union

from conta import Conta



class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 1000,**kwargs):
        super().__init__(agencia, conta, saldo, **kwargs)
        self.limite = limite
        self.extrato = list()
        

    def saque(self, valor:Union[int, int]):
        valor = self._normalize_value(valor)
        if valor < 0:
            raise ValueError('Valor não pode ser negativo!')
        if (self._saldo + self.limite) < valor:
            raise ValueError('Valor do saque supera seu saldo e seu limite!')
        self._saldo -= valor
        self.extrato.append(('Saque', valor))
        self.detalhes()
        return self._saldo, self.extrato
