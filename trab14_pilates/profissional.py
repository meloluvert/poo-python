
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.simpledialog as simpledialog
import pickle
import os
import math


class Profissional:
    def __init__(self, cpf, nome, email, tipo_aula, professor):
        self.__nome = nome
        self.__cpf = cpf
        self.email = email
        self.tipo_aula = tipo_aula
        self.professor = professor
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
        self.__tipo_aula = float(valor)        
    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, valor):
        self.__professor = float(valor)        
    
    
    
class ViewCadastraProfissional(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x250')
        self.title("Cadastro de Profissionais")
        self.controle = controle


        self.frame_nome = tk.Frame(self)
        self.frame_cpf = tk.Frame(self)
        self.frame_email = tk.Frame(self)
        self.frame_valor_aula_pilates= tk.Frame(self)
        self.frame_valor_aula_funcional= tk.Frame(self)
        self.frame_preco= tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_cpf.pack()
        self.frame_nome.pack()
        self.frame_email.pack()
        self.frame_preco.pack()
        self.frame_valor_aula_pilates.pack()
        self.frame_valor_aula_funcional.pack()
        self.frame_botoes.pack()
        

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

        self.label_valor_aula_pilates = tk.Label(self.frame_valor_aula_pilates,text=" valor_aula_pilates: ")
        self.label_valor_aula_pilates.pack(side="left")
        self.input_valor_aula_pilates = tk.Entry(self.frame_valor_aula_pilates,  width=20)
        self.input_valor_aula_pilates.pack(side="left")

        self.label_valor_aula_funcional = tk.Label(self.frame_valor_aula_funcional,text=" valor_aula_funcional: ")
        self.label_valor_aula_funcional.pack(side="left")
        self.input_valor_aula_funcional = tk.Entry(self.frame_valor_aula_funcional,  width=20)
        self.input_valor_aula_funcional.pack(side="left")

        #botoes
        self.botao_enviar = tk.Button(self.frame_botoes ,text="Cadastrar")      
        self.botao_enviar.pack(side="left")
        self.botao_enviar.bind("<Button>", controle.cadastrar)
      
    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ControleProfissional():       

    def __init__(self, controle_principal):       
        self.lista_profissionais = []

    def get_profissionais(self):
        return self.lista_profissionais
    def get_profissional(self, nome_profissional):
        for profissional in self.lista_profissionais:
            if(profissional.nome == nome_profissional):
                return profissional
    def cadastrar_view(self):
        self.view_cadastrar = ViewCadastraProfissional(self) 

    def limpar_input_cadastro(self, event):
        self.view_cadastrar.input_nome.delete(0, len(self.view_cadastrar.input_nome.get()))
        self.view_cadastrar.input_crm.delete(0, len(self.view_cadastrar.input_crm.get()))
        self.view_cadastrar.input_especialidade.delete(0, len(self.view_cadastrar.input_especialidade.get()))
    def listar_profissionais_view(self):
        texto = 'Nome -- Email -- CPF -- valor funcional -- valor pilates\n'
        for profissional in self.lista_profissionais:
            texto += "Nome:" + profissional.nome + "\n" +"Email" + profissional.email + "\n" + "CPF"+ profissional.cpf + "\n" +"Funcional:"+ str(profissional.valor_aula_funcional) + "\n" + "Pilates"+ str(profissional.valor_aula_pilates)
        self.view_listar_profissionais = messagebox.showinfo("Listagem de profissionais", texto)
    def cadastrar(self, event):
        try: 
            nome = self.view_cadastrar.input_nome.get()
            cpf = self.view_cadastrar.input_cpf.get()
            email = self.view_cadastrar.input_email.get()
            valor_aula_pilates = self.view_cadastrar.input_valor_aula_pilates.get()
            valor_aula_funcional = self.view_cadastrar.input_valor_aula_funcional.get()

            profissional = Profissional(cpf, nome, email, valor_aula_pilates, valor_aula_funcional)
            self.lista_profissionais.append(profissional)
            
            self.view_cadastrar.mostrar_janela('Sucesso', 'Profissional cadastrado com sucesso')
            self.salvar_profissionais()
            self.limpar_input_cadastro(event)
            self.fechar_janela_cadastrar(event)
        except ValueError as error:
            self.view_cadastrar.mostrar_janela('Erro', error) 

    def fechar_janela_cadastrar(self, event):
        self.view_cadastrar.destroy()
    def fechar_janela_avaliar(self, event):
        self.view_avaliar.destroy()

