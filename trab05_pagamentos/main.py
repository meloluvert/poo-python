
#Lucas Melo dos Santos Miranda

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self,codigo , nome):
        self.__nome = nome
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__telefone = telefone

    def imprimeFolha(self):
        pass


class PontoFunc():
    def __init__(self, mes, ano, faltas, atrasos):
        self.__mes = mes
        self.__ano = ano
        self.__faltas = faltas
        self.__atrasos = atrasos

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def faltas(self):
        return self.__faltas

    @faltas.setter
    def faltas(self, faltas):
        self.__faltas = faltas

    @property
    def atrasos(self):
        return self.__atrasos

    @atrasos.setter
    def atrasos(self, atrasos):
        self.__atrasos = atrasos


class Professor(Funcionario):
    def __init__(self, codigo ,nome,profissao, salarioHora, nroAulas):
        super().__init__(codigo, nome)
        self.__profissao = profissao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas
        self.__fichasMensais = []
    
    @property
    def nroAulas(self):
        return self.__nroAulas

    @property
    def fichasMensais(self):
        return self.__fichasMensais
        
    @fichasMensais.setter
    def fichasMensais(self, fichasMensais):
        self.__fichasMensais = fichasMensais

    @nroAulas.setter
    def nroAulas(self, nroAulas):
        self.__nroAulas = nroAulas

    @property
    def salarioHora(self):
        return self.__salarioHora

    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao
    def adicionaPonto(self, mes, ano, faltas, atrasos):
        self.fichasMensais.append(PontoFunc(mes, ano, faltas, atrasos))
    def lancaFaltas(self, mes, ano, faltas):
        for mes_ficha in self.fichasMensais:
            if mes_ficha.mes == mes and mes_ficha.ano ==  ano:
                mes_ficha.faltas = faltas
     

    def lancaAtrasos(self, mes, ano, atrasos):
        for mes_ficha in self.fichasMensais:
            if mes_ficha.mes == mes and mes_ficha.ano ==  ano:
                mes_ficha.atrasos = atrasos

    def getSalario(self, nroFaltas):
        return self.salarioHora * self.nroAulas - self.salarioHora * nroFaltas

    def getBonus(self, salario , nroAtrasos):
        return 0.1*salario - nroAtrasos*0.01*salario


    def imprimeFolha(self, mes,ano):
        for mes_ficha in self.fichasMensais:
            if mes_ficha.mes == mes and mes_ficha.ano ==  ano:
                print('Código: ', self.codigo)
                print('Nome:', self.nome)
                print(f"Salário líquido: {self.getSalario(mes_ficha.faltas):.2f}")
                print(f"Bônus: {self.getBonus(self.getSalario(mes_ficha.faltas), mes_ficha.atrasos):.2f}")


class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, profissao, salarioMensal):
        super().__init__(codigo,nome)
        self.__salarioMensal = salarioMensal
        self.__profissao = profissao
        self.__fichasMensais = []
    
    @property
    def salarioMensal(self):
        return self.__salarioMensal

    @salarioMensal.setter
    def salarioMensal(self, salarioMensal):
        self.__salarioMensal = salarioMensal

    @property
    def fichasMensais(self):
        return self.__fichasMensais
        
    @fichasMensais.setter
    def fichasMensais(self, fichasMensais):
        self.__fichasMensais = fichasMensais

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao

    def adicionaPonto(self, mes, ano, faltas, atrasos):
        self.fichasMensais.append(PontoFunc(mes, ano, faltas, atrasos))
    def lancaFaltas(self, mes, ano, faltas):
        for mes_ficha in self.fichasMensais:
            if mes_ficha.mes == mes and mes_ficha.ano ==  ano:
                mes_ficha.faltas = faltas
     

    def lancaAtrasos(self, mes, ano, atrasos):
        for mes_ficha in self.fichasMensais:
            if mes_ficha.mes == mes and mes_ficha.ano ==  ano:
                mes_ficha.atrasos = atrasos

    def getSalario(self, nroFaltas):
        return self.salarioMensal - ((self.salarioMensal/30) * nroFaltas)

    def getBonus(self, salario , nroAtrasos):
        return 0.08*salario - nroAtrasos*0.01*salario


    def imprimeFolha(self, mes,ano):
        for mes_ficha in self.fichasMensais:
            if mes_ficha.mes == mes and mes_ficha.ano ==  ano:
                print('Código: ', self.codigo)
                print('Nome:', self.nome)
                print(f"Salário líquido: {self.getSalario(mes_ficha.faltas):.2f}")
                print(f"Bônus: {self.getBonus(self.getSalario(mes_ficha.faltas), mes_ficha.atrasos):.2f}")


if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()