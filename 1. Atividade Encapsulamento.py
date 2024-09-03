from abc import ABC, abstractmethod
import os 

os.system("cls||clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNumero: {self.numero} \nCidade: {self.cidade}"
    
class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"\n=== Dados do Funcionario ==="
                f"\nNome: {self.nome}"
                f"\nE-mail: {self.email}"
                f"\nSalario: {self.salario_final()}"
                f"\n\nEndereco: {self.endereco}")