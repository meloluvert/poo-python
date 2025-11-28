import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.simpledialog as simpledialog
import pickle
import os
import math

class Medico:
    def __init__(self, nome, crm, especialidade):
        self.__nome = nome
        self.__crm = crm
        self.especialidade = especialidade
        self.__consultas = []
    @property
    def crm(self):
        return self.__crm

    @property
    def consultas(self):
        return self.__avaliacoes
    
    @consultas.setter
    def consultas(self, avaliacao):
        self.__avaliacoes = avaliacao
        
    @property
    def nome(self):
        return self.__nome

    @property
    def especialidade(self):
        return self.__especialidade
    
    @especialidade.setter 
    def especialidade(self, valor):
        self.especialidades = ['Pediatria', 'Cardiologia', 'Neurologia', 'Oftalmologia', 'Ortopedia', 'Gastroenterologia','Psiquiatria', 'Pneumologia']
        if not valor in self.especialidades:
            raise ValueError("Especilidade inválida: {}".format(valor))
        else:
            self.__especialidade = valor
    
    
class ControleMedico():       

    def __init__(self, controle_principal):        
        if not os.path.isfile("medico.pickle"):
            self.lista_medicos = []
        else:
            with open("medico.pickle", "rb") as f:
                self.lista_medicos = pickle.load(f)
        self.controle_principal = controle_principal

    def get_medicos(self):
        return self.lista_medicos
    def get_medico(self, nome_medico):
        for medico in self.lista_medicos:
            if(medico.nome == nome_medico):
                return medico
    def cadastrar_view(self):
        self.view_cadastrar = ViewCadastraMedico(self) 

    def salvar_medicos(self):
        if len(self.lista_medicos) != 0:
            with open("medico.pickle","wb") as f:
                pickle.dump(self.lista_medicos, f)

    def limpar_input_cadastro(self, event):
        self.view_cadastrar.input_nome.delete(0, len(self.view_cadastrar.input_nome.get()))
        self.view_cadastrar.input_crm.delete(0, len(self.view_cadastrar.input_crm.get()))
        self.view_cadastrar.input_especialidade.delete(0, len(self.view_cadastrar.input_especialidade.get()))

    def cadastrar(self, event):
        try: 
            nome = self.view_cadastrar.input_nome.get()
            crm = self.view_cadastrar.input_crm.get()
            especialidade = self.view_cadastrar.input_especialidade.get()

            medico = Medico(nome, crm, especialidade)
            self.lista_medicos.append(medico)
            
            self.view_cadastrar.mostrar_janela('Sucesso', 'Médico cadastrado com sucesso')
            self.salvar_medicos()
            self.limpar_input_cadastro(event)
            self.fechar_janela_cadastrar(event)
        except ValueError as error:
            self.view_cadastrar.mostrar_janela('Erro', error) 

    def fechar_janela_cadastrar(self, event):
        self.view_cadastrar.destroy()
    def fechar_janela_avaliar(self, event):
        self.view_avaliar.destroy()



class ViewCadastraMedico(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x250')
        self.title("Cadastro de Consultas")
        self.controle = controle


        self.frame_nome = tk.Frame(self)
        self.frame_crm = tk.Frame(self)
        self.frame_especialidade = tk.Frame(self)
        self.frame_genero= tk.Frame(self)
        self.frame_preco= tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_nome.pack()
        self.frame_crm.pack()
        self.frame_especialidade.pack()
        self.frame_genero.pack()
        self.frame_preco.pack()
        self.frame_botoes.pack()
        

        self.label_nome = tk.Label(self.frame_nome,text="Nome: ")
        self.label_nome.pack(side="left")
        self.input_nome = tk.Entry(self.frame_nome,  width=20)
        self.input_nome.pack(side="left")

        self.label_crm = tk.Label(self.frame_crm,text=" CRM: ")
        self.label_crm.pack(side="left")
        self.input_crm = tk.Entry(self.frame_crm,  width=20)
        self.input_crm.pack(side="left")

        self.label_especialidade = tk.Label(self.frame_especialidade,text=" Especialidade: ")
        self.label_especialidade.pack(side="left")
        self.input_especialidade = tk.Entry(self.frame_especialidade,  width=20)
        self.input_especialidade.pack(side="left")

        #botoes
        self.botao_enviar = tk.Button(self.frame_botoes ,text="Cadastrar")      
        self.botao_enviar.pack(side="left")
        self.botao_enviar.bind("<Button>", controle.cadastrar)
      
        self.botao_limpar = tk.Button(self.frame_botoes ,text="Limpar")      
        self.botao_limpar.pack(side="left")
        self.botao_limpar.bind("<Button>", controle.limpar_input_cadastro)  

        self.botao_fechar = tk.Button(self.frame_botoes ,text="Sair")      
        self.botao_fechar.pack(side="left")
        self.botao_fechar.bind("<Button>", controle.fechar_janela_cadastrar)
    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

