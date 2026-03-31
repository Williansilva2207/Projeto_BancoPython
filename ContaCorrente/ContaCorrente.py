from Conta.Conta import Conta
class ContaCorrente(Conta):
    def __init__(self,saldo,limite = 5000.00, limite_saques = 3):
        super().__init__(saldo)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if valor < 0:
            raise ValueError("O limite não pode ser negativo")
        self._limite = valor

    @property
    def limite_saques(self):
        return self._limite_saques

    @limite_saques.setter
    def limite_saques(self, valor):
        if valor < 0:
            raise ValueError("O limite de saques não pode ser negativo")
        self._limite_saques = valor