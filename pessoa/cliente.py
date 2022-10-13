from pessoa import Pessoa


class Cliente(Pessoa):
    def inserir_conta(self, conta):
        self.conta = conta
