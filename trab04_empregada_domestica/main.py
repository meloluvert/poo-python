
#Lucas Melo dos Santos Miranda
from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def getSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora
    
    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas

    @horasTrabalhadas.setter
    def horasTrabalhadas(self, horasTrabalhadas):
        self.__horasTrabalhadas = horasTrabalhadas

    @property
    def valorPorHora(self):
        return self.__valorPorHora

    @valorPorHora.setter
    def valorPorHora(self, valorPorHora):
        self.__valorPorHora = valorPorHora

    def getSalario(self):
        return self.horasTrabalhadas * self.valorPorHora

class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia
    
    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados

    @diasTrabalhados.setter
    def diasTrabalhados(self, diasTrabalhados):
        self.__diasTrabalhados = diasTrabalhados

    @property
    def valorPorDia(self):
        return self.__valorPorDia

    @valorPorDia.setter
    def valorPorDia(self, valorPorDia):
        self.__valorPorDia = valorPorDia

    def getSalario(self):
        return self.diasTrabalhados * self.valorPorDia

class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal
    
    @property
    def valorMensal(self):
        return self.__valorMensal

    @valorMensal.setter
    def valorMensal(self, valorMensal):
        self.__valorMensal = valorMensal

    def getSalario(self):
        return self.valorMensal



lista_candidatas = [Horista('Joana', '21916645856',160,12), Diarista('Valéria', '35916678346',20,65), Mensalista('Ivone', '321936354782',1200)]
candidataMenorSalario = lista_candidatas[0]
for i in lista_candidatas:
    print("Nome:", i.nome)
    print("Telefone:", i.telefone)
    print("Salário:", i.getSalario())
    print("-------------------------------")
    if(i.getSalario() < candidataMenorSalario.getSalario()):
        candidataMenorSalario = i
print("Candidata com menor sálario:", candidataMenorSalario.nome , "\nTelefone:", candidataMenorSalario.telefone)