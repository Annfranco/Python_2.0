import os
from enum import Enum

class Setor(Enum):
    FINANCEIRO = "Financeiro" 
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Funcionario:
    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"ID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSalario: {self.salario}"
                f"\nSetor: {self.setor.value}"
                f"\nSexo: {self.sexo.value}")

os.system("cls||clear")
funcionario_1 = Funcionario(4001, "Maria", 30, 4700, Setor.MARKETING, Sexo.FEMININO)
print(funcionario_1)