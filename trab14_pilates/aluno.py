
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.simpledialog as simpledialog
import pickle
import os
import math


class Aluno:
    def __init__(self, cpf, nome, email, tipo_aula, professor, num_aulas_semanais):
        self.__nome = nome
        self.__cpf = cpf
        self.email = email
        self.tipo_aula = tipo_aula
        self.professor = professor
        self.num_aulas_semanais = num_aulas_semanais
    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, valor):
        self.__email = valor
    @property
    def tipo_aula(self):
        return self.__tipo_aula
    
    @tipo_aula.setter
    def tipo_aula(self, valor):
        self.__tipo_aula = valor
    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, valor):
        self.__professor = valor
    
    @property
    def num_aulas_semanais(self):
        return self.__num_aulas_semanais
    
    @num_aulas_semanais.setter
    def num_aulas_semanais(self, valor):
        self.__num_aulas_semanais = int(valor)     

class ViewCadastraAluno(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x250')
        self.title("Cadastro de Alunos")
        self.controle = controle


        self.frame_nome = tk.Frame(self)
        self.frame_cpf = tk.Frame(self)
        self.frame_email = tk.Frame(self)
        self.frame_tipo_aula= tk.Frame(self)
        self.frame_nome_professor= tk.Frame(self)
        self.frame_num_aulas_semanais= tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_cpf.pack()
        self.frame_nome.pack()
        self.frame_email.pack()
        self.frame_tipo_aula.pack()
        self.frame_nome_professor.pack()
        self.frame_num_aulas_semanais.pack()

        self.frame_botoes.pack()

        self.tipo_aula_escolhida= tk.StringVar()
        self.nome_professor_escolhido= tk.StringVar()
        self.num_aulas_semanais_escolhidas= tk.StringVar()

        self.label_nome = tk.Label(self.frame_nome,text="Nome: ")
        self.label_nome.pack(side="left")
        self.input_nome = tk.Entry(self.frame_nome,  width=20)
        self.input_nome.pack(side="left")

        self.label_cpf = tk.Label(self.frame_cpf,text=" cpf: ")
        self.label_cpf.pack(side="left")
        self.input_cpf = tk.Entry(self.frame_cpf,  width=20)
        self.input_cpf.pack(side="left")

        self.label_email = tk.Label(self.frame_email,text=" email: ")
        self.label_email.pack(side="left")
        self.input_email = tk.Entry(self.frame_email,  width=20)
        self.input_email.pack(side="left")

        self.label_tipo_aula = tk.Label(self.frame_tipo_aula,text="Tipo da aula: ")
        self.label_tipo_aula.pack(side="left")
        self.combobox = ttk.Combobox(self.frame_tipo_aula, width = 15,textvariable = self.tipo_aula_escolhida)
        self.combobox.pack(side="left")
        valores = ["pilates", "funcional"]
        self.combobox['values'] = valores

        self.label_nome_professor = tk.Label(self.frame_nome_professor,text="Nome do professor: ")
        self.label_nome_professor.pack(side="left")
        self.combobox = ttk.Combobox(self.frame_nome_professor, width = 15,textvariable = self.nome_professor_escolhido)
        self.combobox.pack(side="left")
        valores = [professor.nome for professor in controle.controle_principal.controle_profissional.get_profissionais()]
        self.combobox['values'] = valores


        self.label_num_aulas_semanais = tk.Label(self.frame_num_aulas_semanais,text="Qtd aulas semanais: ")
        self.label_num_aulas_semanais.pack(side="left")
        self.combobox = ttk.Combobox(self.frame_num_aulas_semanais, width = 15,textvariable = self.num_aulas_semanais_escolhidas)
        self.combobox.pack(side="left")
        valores = [2,3,4]
        self.combobox['values'] = valores

        #botoes
        self.botao_enviar = tk.Button(self.frame_botoes ,text="Cadastrar")      
        self.botao_enviar.pack(side="left")
        self.botao_enviar.bind("<Button>", controle.cadastrar)
      
    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ControleAluno():       

    def __init__(self, controle_principal):       
        self.lista_alunos = []
        self.controle_principal = controle_principal

    def get_alunos(self):
        return self.lista_alunos
    def get_aluno(self, nome_aluno):
        for aluno in self.lista_alunos:
            if(aluno.nome == nome_aluno):
                return aluno
    def cadastrar_view(self):
        self.view_cadastrar = ViewCadastraAluno(self) 
    def consultar_aluno_view(self):
        cpf_digitado = tk.simpledialog.askstring("Consulta de Aluno", "Digite o cpf do Aluno")
        aluno_encontrado = None
        for aluno in self.lista_alunos:
            if(aluno.cpf == cpf_digitado):
                aluno_encontrado = aluno
                break
        if(aluno_encontrado is None):
             messagebox.showinfo('Erro', 'Código não encontrado')
        texto = 'Nome -- Email -- Código\n'
        mensalidade_calculada = 0
        if(aluno.num_aulas_Semanais == 2):
            custo_prodessor = professor
        texto += "Nome:" + aluno.nome + "\n" +"Email" + aluno.email + "\n" + "CPF"+ aluno.cpf + "\n" +"Tipo de aula:"+ str(aluno.tipo_aula) + "\n" + "professor:"+ aluno.professor.nome +"\n"+ "Num aulas semanais" + str(aluno.num_aulas_semanais) + mensalidade_calculada
        self.limiteLista = messagebox.showinfo("Consulta de Aluno", texto)

    def limpar_input_cadastro(self, event):
        self.view_cadastrar.input_nome.delete(0, len(self.view_cadastrar.input_nome.get()))
        self.view_cadastrar.input_crm.delete(0, len(self.view_cadastrar.input_crm.get()))
        self.view_cadastrar.input_especialidade.delete(0, len(self.view_cadastrar.input_especialidade.get()))
    def listar_alunos_view(self):
        texto = 'Nome -- Email -- CPF -- valor funcional -- valor pilates\n'
        for aluno in self.lista_alunos:
            texto += "Nome:" + aluno.nome + "\n" +"Email" + aluno.email + "\n" + "CPF"+ aluno.cpf + "\n" +"Funcional:"+ str(aluno.valor_aula_funcional) + "\n" + "Pilates"+ str(aluno.valor_aula_pilates)
        self.view_listar_alunos = messagebox.showinfo("Listagem de alunos", texto)
    def cadastrar(self, event):
        try: 
            nome = self.view_cadastrar.input_nome.get()
            cpf = self.view_cadastrar.input_cpf.get()
            email = self.view_cadastrar.input_email.get()
            tipo_aula = self.view_cadastrar.tipo_aula_escolhida.get()
            num_aulas_semanais = self.view_cadastrar.num_aulas_semanais_escolhidas.get()
            nome_professor =  self.view_cadastrar.nome_professor_escolhido.get()

            professor = self.controle_principal.controle_profissional.get_profissional(nome_professor)
            aluno = Aluno(cpf, nome, email, tipo_aula, professor, num_aulas_semanais)
            self.lista_alunos.append(aluno)
            
            self.view_cadastrar.mostrar_janela('Sucesso', 'aluno cadastrado com sucesso')
            self.salvar_profissionais()
            self.limpar_input_cadastro(event)
            self.fechar_janela_cadastrar(event)
        except ValueError as error:
            self.view_cadastrar.mostrar_janela('Erro', error) 

    def fechar_janela_cadastrar(self, event):
        self.view_cadastrar.destroy()
    def fechar_janela_avaliar(self, event):
        self.view_avaliar.destroy()
