from Cliente import Cliente
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento):
        super().__init__()
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str):
        self._nome = valor 
    
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor 
    
    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor: str):
        self._data_nascimento = valor 
    
    

