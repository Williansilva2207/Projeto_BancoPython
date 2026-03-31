import random
from Cliente import Cliente
from Historico import Historico
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
    
    def nova_conta(cliente: Cliente, numero: int):
        pass

    def sacar(valor:float) -> bool:
        pass
    def depositar(valor:float) -> bool:
        pass