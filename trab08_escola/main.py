class TitulacaoErrada(Exception):
    pass
class IdadeMenorQuePermitida(Exception):
    pass
class CursoNaoPermitido(Exception):
    pass
class CPFJaCadastrado(Exception):
    pass
class Pessoa:
    def __init__(self, nome,cpf, endereco, idade):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__idade = idade
    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def endereco(self):
        return self.__endereco
    @property
    def idade(self):
        return self.__idade
    def printDescricao(self):
        pass
class Professor(Pessoa):
    def __init__(self, nome,cpf, endereco, idade, titulacao):
        super().__init__(nome, cpf, endereco, idade)
        self.__titulacao = titulacao
    @property
    def titulacao(self):
        return self.__titulacao
    def printDescricao(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Endereço:", self.endereco)
        print("Idade:", self.idade)
        print("Titulação:", self.titulacao)
    
class Aluno(Pessoa):
    def __init__(self, nome,cpf, endereco, idade, curso):
        super().__init__(nome, cpf, endereco, idade)
        self.__curso = curso
    @property
    def curso(self):
        return self.__curso
    def printDescricao(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Endereço:", self.endereco)
        print("Idade:", self.idade)
        print("Curso:", self.curso)
    
if __name__ == "__main__":
    listaExemplo = [
        Professor("Carlos", "11111111111", "Rua A", 45, "doutor"),     
        Professor("Ana", "22222222222", "Rua B", 28, "doutor"),        
        Professor("Rafael", "33333333333", "Rua C", 40, "mestre"),     
        Aluno("Beatriz", "44444444444", "Rua D", 20, "SIN"),           
        Aluno("João", "55555555555", "Rua E", 16, "CCO"),              
        Aluno("Lucas", "66666666666", "Rua F", 21, "ADM"),             
        Aluno("Beatriz", "44444444444", "Rua D", 20, "SIN"),          
    ]
    cadastro = []
    for pessoa in listaExemplo:
        try:
            for pessoaCadastrada in cadastro:
                if(pessoaCadastrada.cpf  ==  pessoa.cpf):
                    raise CPFJaCadastrado()
            if(isinstance(pessoa, Professor)):
                if(pessoa.idade<30):
                    raise IdadeMenorQuePermitida()
                if(pessoa.titulacao != "doutor"):
                    raise TitulacaoErrada()
                cadastro.append(pessoa)
            elif(isinstance(pessoa, Aluno)):
                if(pessoa.idade<18):
                    raise IdadeMenorQuePermitida()
                if(pessoa.curso != "SIN" and pessoa.curso != "CCO"):
                    raise CursoNaoPermitido()
                cadastro.append(pessoa)

        except IdadeMenorQuePermitida:
            print("A idade é menor que a permitida!")
        except TitulacaoErrada:
            print("A titulação deve ser 'doutor' para ser cadastrada!")
        except CursoNaoPermitido:
            print("Os cursos permitidos são somente SIN e CCO")
        except CPFJaCadastrado:
            print("CPF já cadastrado!")
    print()
    for pessoaCadastrada in cadastro:
        pessoaCadastrada.printDescricao()
        print()
