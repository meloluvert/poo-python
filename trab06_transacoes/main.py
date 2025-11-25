#Lucas Melo dos Santos Miranda


from abc import ABC, abstractmethod
from datetime import date

class Transacao(ABC):
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data
    @property
    def valor(self):
        return self.__valor
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha  = senha
    @property
    def senha(self):
        return self.__senha
class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante  = nomeDepositante
    @property
    def nomeDepositante(self):
        return self.__nomeDepositante   
class Transferencia(Transacao):
    def __init__(self, valor, data, tipoTransf):
        super().__init__(valor, data)
        self.__tipoTransf  = tipoTransf
    @property
    def tipoTransf(self):
        return self.__tipoTransf
class Conta():
    def __init__(self, nroConta, nome, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self.__transacoes = []
    @property
    def nroConta(self):
        return self.__nroConta
    @property
    def nome(self):
        return self.__nome
    @property
    def limite(self):
        return self.__limite
    @property
    def senha(self):
        return self.__senha
    @property
    def transacoes(self):
        return self.__transacoes
    @transacoes.setter
    def transacoes(self, transacoes):
        self.__transacoes = transacoes
    def adicionaDeposito(self, valor, data, nomeDepositante):
        self.__transacoes.append(Deposito(valor, data, nomeDepositante))

    def adicionaSaque(self, valor, data, senha):
        if(senha == self.senha and valor <= self.calculaSaldo() + self.limite) :
            self.__transacoes.append(Saque(valor, data, senha))
            return True
        return False
    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if(senha == self.senha and valor <= self.calculaSaldo() + self.limite):
            self.__transacoes.append(Transferencia(valor, data, "D"))
            contaFavorecido.transacoes.append(Transferencia(valor, data, "C"))
            return True
        return False
    #obs: não sooube como varrer o vetor, uma vez que o método pai tinha o valor, mas o tipo do filho precisaria acessar de outra maneira, (como saberia se é Deposito, Saque ou Transferência para não dar erro no atributos?) tive que pesquisar por fora
    def calculaSaldo(self):
        saldo = self.limite
        
        for transacao in self.__transacoes:
            if isinstance(transacao, Deposito):
                saldo += transacao.valor

            elif isinstance(transacao, Saque):
                saldo -= transacao.valor

            elif isinstance(transacao, Transferencia):
                if transacao.tipoTransf == "D":  
                    saldo -= transacao.valor
                elif transacao.tipoTransf == "C":  
                    saldo += transacao.valor

        return saldo

if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')

    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')

    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 1700