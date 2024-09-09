from abc import ABC, abstractmethod
import os 

os.system("cls||clear")

class ValorNegativoError(Exception):
    pass

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

    def __str__(self) -> str:
        return (f"\n=== Dados do Funcionario ==="
                f"\nNome: {self.nome}"
                f"\nE-mail: {self.email}"
                f"\nSalario: {self.salario_final}"
                f"\n\nEndereco: {self.endereco}")
    
    @abstractmethod
    def salario_final(self) -> float:
        pass

    def salario_final(self, salario):
        try:
            self.__verificar_salario(salario)
        except ValorNegativoError as error:
            return f"Erro: {error}"
        return self.salario
        
    def __verificar_salario(self, salario):
        if salario < 0:
            raise ValorNegativoError("Não é possivel inserir um salario negativo.")
        
    
class Motoboy(Funcionario):
        def __init__(self, nome: str, email: str, salario: float, cnh: str, endereco: Endereco) -> None:
            super().__init__(nome, email, salario, endereco)
            self.cnh = cnh
        
        def __str__(self) -> str:
            return  (f"{super().__str__()}"
                     f"\nCNH: {self.cnh}")
        
class Gerente(Funcionario):
     def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)

motoboy = Motoboy("Jose", "jose@gmail.com", 5674, "cdcduje", Endereco("Rua b", "253", "Aracaju"))
print(motoboy)
print(motoboy.salario_final(2000))

gerente = Gerente("Marta", "ghff@gmail.com", - 5674, Endereco("Rua a", "5", "Salvador"))
print(gerente)
print(gerente.salario_final(-5000))

