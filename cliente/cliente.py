from cliente.confirmador import CPF

class Cliente(CPF):
    def __init__(self, nome, cpf, email, telefone, endereco):
        super().__init__(cpf)
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._endereco = endereco

    def __str__(self):
            return f'''
                   Cliente:   {self._nome} 
                   Documento: {self._cpf}
                   Email:     {self._email}
                   Telefone:  {self._telefone}
                   Endereço:  {self._endereco}'''
         