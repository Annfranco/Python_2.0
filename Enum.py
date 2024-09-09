import os
from enum import Enum

class Sexo(Enum):
    """Definindo valores do Enum"""
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        """Construtor"""
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        """Equivalente ao toString() do java"""
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}")
    
# Instaciando
os.system("cls||clear")
pessoa_1 = Pessoa("Jose", 22, Sexo.MASCULINO)

print(pessoa_1)
