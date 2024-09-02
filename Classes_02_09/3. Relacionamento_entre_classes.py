import os

os.system("cls||clear")

class Endereco:
    def __init__(self, logradouro: str, numero: int) -> None:
        self.logradouro = logradouro
        self.numero = numero

    # def exibir_endereco(self) -> str:
    #     return f"\nLogradouro: {self.logradouro} \nNumero: {self.numero}"
    
    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNumero: {self.numero}"

class Aluno:
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__ (self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereco: {self.endereco}"

    #def exibir_dados(self) -> str:
    #   return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereco: {self.endereco.exibir_endereco()}"
    
# Instanciar classe.
# endereco1 = Endereco("Rua A", 5)
# aluno = Aluno("Marta", 22, endereco1)

aluno1 = Aluno("Marta", 22, Endereco("Rua A", 22))

print(aluno1)