from cliente import Cliente
from conta import Conta

class Banco:
    def __init__(self):
        self.agencias = [1111,2222,3333]
        self.clientes = list()
        self.contas = list()


    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            print('Cliente não autenticado')
            return False
        if cliente.conta not in self.contas:
            print('Cliente não autenticado')
            return False
        if cliente.conta.agencia not in self.agencias:
            print('Cliente não autenticado')
            return False
        return True