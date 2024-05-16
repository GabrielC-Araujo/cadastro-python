import re

class CPF():
    def __init__(self, documento):
        self._cpf = str(documento)
        #Se a função validador_cpf retornar True, armazena documento em self._cpf e retorna o número
        if self.validador_cpf(documento) == True:
            self._cpf = documento
            return self._cpf

    def validador_cpf(self, documento):
        #Limpando possíveis formatações ( . ou - que provavelmente colocam)
        entrada = re.findall('\d',documento)

        #Verifica se o tamanho está correto
        if len(documento) > 14 or len(entrada) < 11 or len(entrada) > 11:
            print('CPF inválido!')

        #Verifica se não está sendo usado somente um número
        valid = 0
        for dig in range(0,11):
            valid != int(entrada[dig])
            dig+=1
        if int(entrada[0]) == valid/11:
            raise ValueError('CPF inválido! Números repetidos')

        #Primeiro loop de contas para verificar o primeiro dígito
        soma = 0
        count = 10
        for i in range(0,len(entrada)-2):
            soma += (int(entrada[i]) * count)
            i+=1
            count-=1

        dg1 = 11-(soma%11)
        if dg1 >= 10:
            dg1 = 0

        #Segundo loop de contas para verificar o segundo dígito
        soma = 0
        count = 11
        for j in range(0,(len(entrada)-1)):
            soma += (int(entrada[j]) * count)
            j+=1
            count-=1

        dg2 = 11-(soma%11)
        if dg2 >= 10:
            dg2 = 0

        if int(entrada[9]) != dg1 or int(entrada[10]) != dg2:
            raise ValueError('CPF inválido!')
        else:
            return True
        