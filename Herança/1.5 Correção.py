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
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"\n=== Dados do Funcionario ==="
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nE-mail: {self.email}"
                f"\nSalario: {self.salario_final()}"
                f"\n\nEndereco: {self.endereco}")
    
class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea 

    # def __str__(self) -> str:
    #     return f"\nNome: {self.nome} \nTelefone: {self.telefone} \nE-mail: {self.email} \nSalario: {self.salario} \nCREA: {self.crea} \nEndereço: {self.endereco}"
    
    def salario_final(self) -> float:
        return 3000
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}"
        )

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str,crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    # def __str__(self) -> str:
    #     return f"\nNome: {self.nome} \nTelefone: {self.telefone} \nE-mail: {self.email} \nSalario: {self.salario} \nCRM: {self.crm} \nEndereço: {self.endereco}"
    
    def salario_final(self) -> float:
        return 5000

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCRM: {self.crm}"
        )
    
# Instanciando
engenheiro = Engenheiro("Isaque", "71 98214-7598", "isaquesbd@gmail.com", "hbfhd", Endereco("Rua A", "5", "1 Andar", "41987-000", "Sao Paulo"))
print(engenheiro)

medico = Medico("Gisele", "71 98214-1388", "gizzymeneses@gmail.com", "hjuv", Endereco("Rua B", "99", "Terreo", "41987-789", "Rio de Janneiro"))
print(medico)