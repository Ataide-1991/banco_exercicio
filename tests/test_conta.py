import pytest
from pessoa.conta import Conta

class instanced(Conta):
    def saque(self, valor):
        print('Saque instanciado')

    def deposito(self, valor):
        print('Deposito instanciado')


class TestConta:
    def test_instance_obj(self):
        msg = "Can't instantiate abstract class Conta with abstract methods deposito, saque"
        with pytest.raises(TypeError) as error:
            self.conta = Conta()
        assert msg == str(error.value)

        self.conta2 = instanced()
        self.conta2.limite = 10.5
        assert isinstance(self.conta2, object)
        assert self.conta2.limite == 10.5

        msg2 = 'Saldo negativo!'
        with pytest.raises(ValueError) as error:
            self.conta2.saldo = -5
        assert msg2 == str(error.value)
        


