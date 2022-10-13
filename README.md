# banco_exercicio em construção

Exercicio com abstração, herança, encapsulamento, polformismo
criar um sistema bancario (simples) que tem cliente, contas
e um banco. A ideia é que o cliente tenha conta (poupança, corrente)
e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra
banco tem cliente e contas

Dicas:
Criar classe Cliente que herda da classe Pessoa (herança)
    Pessoa tem nome e idade (com getters)
    Cliente tem conta (Agregação da classe Conta Corrente ou Poupança)
Criar classe Conta Corrente e Poupança que herdam de Conta
    CC deve ter limite extra
    Conta tem agencia, numero da conta, saldo
    Conta deve ter metodo deposito
    Conta (super classe) deve ter metodo sacar abstrato
    (abs e poliformismo)-  as subclasses que implementam o metodo sacar)
Criar classe Banco para AGREGAR classes de cliente e de contas
Banco sera responsável por autenticar o cliente e as contas da seguinte maneira:
    Banco tem conta e cliente (agregação)
    *checar se a agencia é daquele banco
    *checar se o cliente é daquele banco
    *checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrito acima)
