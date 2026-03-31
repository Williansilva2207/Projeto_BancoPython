from Conta.Conta import Conta
class Cliente:
    def __init__(self, endereco, contas=None):
        self._endereco = endereco
        self._contas = contas if contas is not None else []

    @property
    def endereco(self) -> str:
        return self._endereco

    @endereco.setter
    def endereco(self, novo_endereco: str):
        if not isinstance(novo_endereco, str):
            raise ValueError("Endereço deve ser uma string")
        self._endereco = novo_endereco

    @property
    def contas(self) -> list:
        return self._contas

    @contas.setter
    def contas(self, novas_contas: list):
        self._contas = novas_contas

    def realizar_transacao(conta: Conta, transacao):
        pass

    def adicionar_conta(conta: Conta):
        pass