from abc import ABC, abstractmethod
import os

os.system("cls||clear") # Limpa Terminal

class Funcionario(ABC):
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        # Acrescimo de 20%
        BONIFICACAO = 1.2 
        salario_final = self.salario * BONIFICACAO
        return salario_final
    

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        # Acrescimo de 10%
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final

# Instaciar classes.
gerente1 = Gerente("Marta", 22, 2000)
print(f"Nome: {gerente1.nome}")
print(f"Idade: {gerente1.idade}")
print(f"Salario: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("Marta", 22, 1000, "A")
print(f"\nNome: {motoboy1.nome}")
print(f"Salario: {motoboy1.calcular_salario()}")
print(f"CNH: {motoboy1.cnh}")