#Lucas Melo dos Santos Miranda

from abc import ABC, abstractmethod

class Venda():
    def __init__(self,codigo_imovel,mes, ano, valor):
        self.__codigo_imovel = codigo_imovel
        self.__mes = mes
        self.__ano = ano
        self.__valor = valor
    @property
    def codigo_imovel(self):
        return self.__codigo_imovel
    @property
    def mes(self):
        return self.__mes
    @property
    def ano(self):
        return self.__ano
    @property
    def valor(self):
        return self.__valor
    
    

class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nome(self):
        return self.__nome
    @property
    def vendas(self):
        return self.__vendas
    
    @vendas.setter
    def vendas(self, vendas):
        self.__vendas = vendas
    def getDados(self):
        pass
    def calculaRenda(self, mes, ano):
        pass
    def adicionaVenda(self, codigo_imovel, mes, ano, valor):
        self.__vendas.append(Venda(codigo_imovel, mes, ano, valor))
class Contratado(Vendedor):
    def __init__(self,codigo, nome, salario_fixo, num_carteira_trabalho):
        super().__init__(codigo, nome)
        self.__comissao = 1
        self.__salario_fixo = salario_fixo
        self.__num_carteira_trabalho = num_carteira_trabalho
    @property
    def salario(self):
        return self.__salario
    @property
    def num_carteira_trabalho(self):
        return self.__num_carteira_trabalho
    def calculaRenda(self, mes, ano):
        renda = self.__salario_fixo
        for venda in self.vendas:
            if(venda.mes == mes and venda.ano == ano):
                renda+= ((self.__comissao)/100)*venda.valor
        return renda
    def getDados(self):
        return str("Nome: " + str(self.nome) + " - Nro Carteira: " + str(self.__num_carteira_trabalho))
class Comissionado(Vendedor):
    def __init__(self,codigo, nome, cpf, comissao):
        super().__init__(codigo, nome)
        self.__comissao = 1
        self.__cpf = cpf
        self.__comissao = comissao
    @property
    def salario(self):
        return self.__salario
    @property
    def comissao(self):
        return self.__comissao
    def calculaRenda(self, mes, ano):
        renda = 0
        for venda in self.vendas:
            if(venda.mes == mes and venda.ano == ano):
                renda+= ((self.__comissao)/100)*venda.valor
        return renda
    def getDados(self):
        return str("Nome: " + str(self.nome) + " - Nro CPF: " + str(self.__cpf))
    
if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))