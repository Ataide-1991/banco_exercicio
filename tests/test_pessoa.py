import pytest
from pessoa import Pessoa

class TestPessoa:
    def test_tipo_instance(self):
        pessoa1 = Pessoa(nome = 'teste1', idade=1)
        assert isinstance(pessoa1._nome, str)
        assert isinstance(pessoa1._idade, int)
        pessoa2 = Pessoa(nome = 'teste1', idade='1')
        assert isinstance(pessoa2._nome, str)
        assert isinstance(pessoa2._idade, int)

    def test_tipo_instancia_fail(self):
        msg = 'Nome deve ser String!'
        with pytest.raises(TypeError) as error:
            Pessoa(nome = 1, idade='1')
        assert str(error.value) == msg

        msg2 = 'idade deve ser um numero inteiro!'
        with pytest.raises(TypeError) as error:
            Pessoa(nome = 'teste', idade=1.1)
        assert str(error.value) == msg2

        msg3 ='Idade deve ser um numero'
        with pytest.raises(Exception) as error:
            Pessoa(nome = 'teste1', idade='teste')
        assert str(error.value) == msg3

        msg4 = 'Nome é obrigatório!'
        with pytest.raises(TypeError) as error:
            Pessoa(idade=1)
        assert str(error.value) == msg4

        msg5 = 'Idade é obrigatória!'
        with pytest.raises(TypeError) as error:
            Pessoa(nome = 'teste')
        assert str(error.value) == msg5