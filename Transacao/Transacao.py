from abc import ABC, abstractmethod
from Conta.Conta import Conta
class Transacao(ABC):
    @abstractmethod
    def registrar(self):
        pass