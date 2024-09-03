import os 

os.system("cls||clear") # Limpa terminal

#Criando excessao
class SaldoInsufienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido.
        # desse jeito não precisa perguntar ao usuario, aparece normalmente o valor atribuido assim que solicitado. Não precisando assim declarar a variavel

    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor) -> float:
        # try - except
        try:
            self.__verificar_sacar(valor)
        except SaldoInsufienteError as error:
            return f"Erro: {error}"
    
        self._saldo -= valor
        return self._saldo
    # estando dentro da classe pode utilizar o _

    def __verificar_sacar(self, valor): # metodo privado.
        if valor > self.saldo:
            raise SaldoInsufienteError("Saldo Insuficiente") # Lançando um erro. raise = excessao.
    
    
    def depositar(self, valor):
        try:
            self.__verificar_depositar(valor)
        except ValorNegativoError as erro:
            return f"Erro: {erro}"
        self._saldo += valor
        return self._saldo
    
    def __verificar_depositar(self, valor):
        if valor < 0:
            raise ValorNegativoError("Não é possivel depositar valor negativo.")
    
class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

# Instaciar classes.
conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(555, 444)

# Para limitar o acesso é usado o _. Pois só sera usado nas instancias. 
# print(conta_corrente._saldo)
# com property
print(conta_corrente.saldo) 
print(conta_corrente.sacar(200))
print(conta_corrente.depositar(-100))
print(conta_corrente.saldo) 
