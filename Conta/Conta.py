import random
from Cliente.Cliente import Cliente
from Historico.Historico import Historico
from Transacao.Deposito import Deposito
from Transacao.Saque import Saque
from ContaCorrente.ContaCorrente import ContaCorrente
class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if not isinstance(valor, (float,int)):
            raise TypeError(print("Somente números."))
        
        self._saldo = valor 

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, valor: int):
        if not isinstance(valor, (int)):
            raise TypeError(print("Somente números inteiros."))
        
        self._numero = valor 
    
    @property
    def agencia(self) -> int:
        return self._agencia

    @agencia.setter
    def agencia(self, valor: str):
        self._agencia = valor
    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @cliente.setter
    def cliente(self, valor: Cliente):
        self._cliente = valor

    def nova_conta(self,cliente: Cliente, numero: int):
        self._cliente = cliente
        self._numero = numero
        

    def sacar(self,valor:float) -> bool:
        if valor < self._saldo:
            return True
        return False

    def depositar(self,valor:float) -> bool:
        conta = ContaCorrente()
        if valor > conta.limite:
            return False
        return True
        