from banco import Banco
from cliente import Cliente
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca

# Instanciando banco
banco = Banco()


# Instanciando clientes
cliente1 = Cliente(nome ='Ataide', idade = 30)
cliente2 = Cliente(nome ='Carlos', idade = 20)
cliente3 = Cliente(nome ='Jose', idade = 15)


# Instanciando contas
conta1 = ContaPoupanca(agencia=1111, conta=254136, saldo=0)
conta2 = ContaCorrente(agencia=2222, conta=254137, saldo=0)
conta3 = ContaPoupanca(agencia=1212, conta=254138, saldo=0)


# Linkando conta ao cliente
cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)


# Linkando cliente ao banco
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)


# Conferindo se o cliente/conta existe no banco para sacar
if banco.autenticar(cliente1):
    cliente1.conta.deposito(100)
    cliente1.conta.saque(50)
    cliente1.conta.extrato_conta()

print(50 * '#')

if banco.autenticar(cliente2):
    cliente2.conta.deposito(100)
    cliente2.conta.saque(1000)
    cliente2.conta.extrato_conta()

print(50 * '#')

if banco.autenticar(cliente3):
    cliente3.conta.deposito(100)
    cliente3.conta.saque(20)
    cliente3.conta.extrato_conta()




