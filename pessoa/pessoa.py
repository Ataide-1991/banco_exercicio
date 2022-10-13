from typing import Union


class Pessoa:
    def __init__(self, nome:str= None, idade:Union[str,int]= None, **kwargs):
        self._nome = self._check_nome(nome)
        self._idade = self._check_idade(idade)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def nome(self, valor):
        self._idade = valor


    # método statico para levantar erros de nome fora do padrão
    @staticmethod
    def _check_nome(nome):
        if nome is None:
            raise TypeError('Nome é obrigatório!')
        elif not isinstance(nome, str):
            raise TypeError('Nome deve ser String!')
        return nome
    
    # método statico para levantar erros de idade fora do padrão
    @staticmethod
    def _check_idade(idade):
        if idade is None:
            raise TypeError('Idade é obrigatória!')
        if isinstance(idade, float):
            raise TypeError('idade deve ser um numero inteiro!')
        if not isinstance(idade, int):
            try:
                idade = int(idade)
            except ValueError:
                raise ValueError('Idade deve ser um numero')
        return idade

    def __str__(self) -> str:
        return str(self.nome)

    def __repr__(self) -> str:
        return str(f'nome: {self.nome}, idade: {self.idade}')
