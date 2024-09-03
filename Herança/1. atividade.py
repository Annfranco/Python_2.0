from abc import ABC, abstractmethod
import os 

os.system("cls||clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNumero: {self.numero} \nComplemento {self.cep} \nCidade: {self.cidade}"

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.salario = salario
        self.endereco = endereco
    
    @abstractmethod
    def salario_final(self) -> float:
        pass

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crea = crea 

    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nTelefone: {self.telefone} \nE-mail: {self.email} \nSalario: {self.salario} \nCREA: {self.crea} \nEndereço: {self.endereco}"
    
    def salario_final(self) -> float:
        pass

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crm = crm

    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nTelefone: {self.telefone} \nE-mail: {self.email} \nSalario: {self.salario} \nCRM: {self.crm} \nEndereço: {self.endereco}"
    
    def salario_final(self) -> float:
        pass

engenheiro = Engenheiro("Isaque", "71 98214-7598", "isaquesbd@gmail.com", 3000, "hbfhd", Endereco("Rua A", "5", "1 Andar", "41987-000", "Sao Paulo"))
print(engenheiro)

medico = Medico("Gisele", "71 98214-1388", "gizzymeneses@gmail.com", 5000, "hjuv", Endereco("Rua B", "99", "Terreo", "41987-789", "Rio de Janneiro"))
print(medico)