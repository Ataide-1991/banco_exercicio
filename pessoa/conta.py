from abc import ABC, abstractmethod
from typing import Union
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

class Conta(ABC):
    def __init__(self, agencia, conta, saldo = 0, **kwargs):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self.extrato = list()



    def deposito(self, valor:Union[int, int]):
        valor = self._normalize_value(valor)
        if valor < 0:
            raise ValueError('Valor não pode ser negativo!')
        self._saldo += valor
        self.extrato.append(('Deposito', valor))
        self.detalhes()


    def detalhes(self):
        logger.info(f'Agẽncia: {self.agencia} '
        f'Conta: {self.conta} '
        f'Saldo: {self._saldo}')


    def extrato_conta(self):
        logger.info(self.extrato)


    @property
    def agencia(self):
        return int(self._agencia)

    @agencia.setter
    def agencia(self, valor):
        if isinstance(valor, float):
            raise TypeError('Agência deve conter somente números')
        if isinstance(valor, str):
            try:
                valor = int(valor)
            except:
                raise TypeError('Agência deve conter somente números')
        self._agencia = valor
        return self._agencia


    @property
    def conta(self):
        return int(self._conta)

    @conta.setter
    def conta(self, valor):
        if isinstance(valor, float):
            raise TypeError('Número da conta deve conter somente números')
        elif isinstance(valor, str):
            try:
                valor = int(valor)
            except:
                raise TypeError('Número da conta deve conter somente números')
        self._conta = valor


    @property
    def saldo(self):
        return float(f'{self._saldo:.2f}')

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError('Saldo negativo!')
        self._saldo = valor

        
    @abstractmethod
    def saque(self, valor):
        pass


    @staticmethod
    def _normalize_value(valor) -> float:
        if isinstance(valor, str):
            if 'R$' in valor:
                valor = str(valor).strip().split('R$')[1]
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError('Valor deve ser numérico!')
        return valor
