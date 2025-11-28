import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.simpledialog as simpledialog
import pickle
import os
import math

class Consulta:
    def __init__(self, paciente, dia, horario, medico ):
        self.__paciente = paciente
        self.__dia = dia
        self.horario = horario
        self.medico = medico
    @property
    def dia(self):
        return self.__dia


    @property
    def medico(self):
        return self.__medico
    
    @medico.setter
    def medico(self, medico):
        self.__medico = medico
        
    @property
    def paciente(self):
        return self.__paciente

    @property
    def horario(self):
        return self.__horario
    
    @horario.setter 
    def horario(self, valor):
        self.__horario = valor


class ControleConsulta():       
    def __init__(self, controle_principal):     
        if not os.path.isfile("consulta.pickle"):
            self.lista_consultas = []
        else:
            with open("consulta.pickle", "rb") as f:
                self.lista_consultas = pickle.load(f)
        self.controle_principal = controle_principal

    def cadastrar_view(self):
        self.view_cadastrar = ViewCadastraConsulta(self) 

    def salvar_consultas(self):
        if len(self.lista_consultas) != 0:
            with open("consulta.pickle","wb") as f:
                pickle.dump(self.lista_consultas, f)
    def gerar_dict_medico_consultas(self):
        dic = {}

        for consulta in self.lista_consultas:
            nome = consulta.medico.nome
            if nome not in dic:
                dic[nome] = []
            dic[nome].append( (consulta.dia, consulta.horario, consulta.paciente) )

        return dic
    
    def listar_consultas_view(self):
        self.view_listar = ViewListaConsultas(self)


    def gerar_dict_especialidades(self):
        especialidades_validas = [
            'Pediatria', 'Cardiologia', 'Neurologia', 'Oftalmologia',
            'Ortopedia', 'Gastroenterologia', 'Psiquiatria', 'Pneumologia'
        ]

        dic = {esp: [] for esp in especialidades_validas}

        lista_medicos = self.controle_principal.controle_medico.get_medicos()

        for medico in lista_medicos:
            if medico.especialidade in dic:
                dic[medico.especialidade].append(medico)

        return dic


    def limpar_input_cadastro(self, event):
        self.view_cadastrar.input_paciente.delete(0, len(self.view_cadastrar.input_paciente.get()))
        self.view_cadastrar.input_dia.delete(0, len(self.view_cadastrar.input_dia.get()))
        self.view_cadastrar.input_horario.delete(0, len(self.view_cadastrar.input_horario.get()))
    def existe_consulta(self, dia, horario, medico):
        for consulta in self.lista_consultas:
            if(consulta.dia == dia and consulta.horario == horario and consulta.medico == medico):
                return True
        return False
    def cadastrar(self, event):
        try: 
            paciente = self.view_cadastrar.input_paciente.get()
            indices = self.view_cadastrar.listbox_medico.curselection()
            pos = indices[0]  
            nome_medico = self.view_cadastrar.listbox_medico.get(pos)
            medico = self.controle_principal.controle_medico.get_medico(nome_medico)
            dia_str = self.view_cadastrar.input_dia.get()
            try:
                dia = int(dia_str)
            except ValueError:
                messagebox.showerror("Erro", "O dia deve ser um número inteiro.")
                return
        
            if dia < 1 or dia > 30:
                messagebox.showerror("Erro", "Dia inválido. Use números de 1 a 30.")
                return

            horario_str = self.view_cadastrar.input_horario.get()
            try:
                horario = int(horario_str)
            except ValueError:
                messagebox.showerror("Erro", "O horário deve ser um número inteiro.")
                return
            
            if horario < 9 or horario > 17:
                messagebox.showerror("Erro", "Horário inválido. Use números de 9 a 17.")
                return
            if(self.existe_consulta(dia, horario, medico)):
                messagebox.showinfo("Erro", f"Consulta já cadastrada")
                return

            consulta = Consulta(paciente, int(dia), int(horario), medico)
            self.lista_consultas.append(consulta)
            self.view_cadastrar.mostrar_janela('Sucesso', 'Consulta cadastrada com sucesso')
            self.salvar_consultas()
            self.limpar_input_cadastro(event)
            self.view_cadastrar.destroy()
        except ValueError as error:
            self.view_cadastrar.mostrar_janela('Erro', error) 

    def fechar_janela_cadastrar(self, event):
        self.view_cadastrar.destroy()
    def fechar_janela_avaliar(self, event):
        self.view_avaliar.destroy()

    
    def atualizar_listbox(self, event):
        especialidade_escolhida = self.view_cadastrar.especialidade_escolhida.get()
        dicionario = self.gerar_dict_especialidades()
        self.view_cadastrar.atualizar_medicos(dicionario[especialidade_escolhida])


class ViewListaConsultas(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("350x350")
        self.title("Consultas por Médico")

        self.controle = controle

        # Frames
        self.frame_combo = tk.Frame(self)
        self.frame_lista = tk.Frame(self)
        self.frame_botao = tk.Frame(self)

        self.frame_combo.pack(pady=10)
        self.frame_lista.pack(pady=10)
        self.frame_botao.pack(pady=10)

        # Label + Combobox
        tk.Label(self.frame_combo, text="Selecione o médico:").pack(side="left")

        self.medico_escolhido = tk.StringVar()
        self.combo = ttk.Combobox(self.frame_combo, width=25, textvariable=self.medico_escolhido)
        self.combo.pack(side="left")

        # Preencher combobox
        medicos = self.controle.controle_principal.controle_medico.get_medicos()
        nomes = [m.nome for m in medicos]
        self.combo["values"] = nomes

        self.combo.bind("<<ComboboxSelected>>", self.atualizar_listbox)

        # Listbox
        self.listbox = tk.Listbox(self.frame_lista, width=45, height=15)
        self.listbox.pack()

        # Botão fechar
        btn = tk.Button(self.frame_botao, text="Fechar", command=self.destroy)
        btn.pack()

    def atualizar_listbox(self, event):
        self.listbox.delete(0, tk.END)

        nome = self.medico_escolhido.get()

        dic = self.controle.gerar_dict_medico_consultas()

        if nome not in dic or len(dic[nome]) == 0:
            self.listbox.insert(tk.END, "Nenhuma consulta para este médico.")
            return

        consultas = dic[nome]

        for dia, hora, paciente in consultas:
            self.listbox.insert(tk.END, f"Dia {dia:02d} | {hora}h | {paciente}")


class ViewCadastraConsulta(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("Cadastro de consultas")
        self.controle = controle


        self.frame_paciente = tk.Frame(self)
        self.frame_dia = tk.Frame(self)
        self.frame_horario = tk.Frame(self)
        self.frame_especialidade= tk.Frame(self)
        self.frame_medico= tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_paciente.pack()
        self.frame_dia.pack()
        self.frame_horario.pack()
        self.frame_especialidade.pack()
        self.frame_medico.pack()
        self.frame_botoes.pack()
        

        self.label_paciente = tk.Label(self.frame_paciente,text="paciente: ")
        self.label_paciente.pack(side="left")
        self.input_paciente = tk.Entry(self.frame_paciente,  width=20)
        self.input_paciente.pack(side="left")

        self.label_dia = tk.Label(self.frame_dia,text=" dia: ")
        self.label_dia.pack(side="left")
        self.input_dia = tk.Entry(self.frame_dia,  width=20)
        self.input_dia.pack(side="left")

        self.label_horario = tk.Label(self.frame_horario,text=" horario: ")
        self.label_horario.pack(side="left")
        self.input_horario = tk.Entry(self.frame_horario,  width=20)
        self.input_horario.pack(side="left")



        self.label_especialidade = tk.Label(self.frame_especialidade, text="Escolha a especialidade: ")
        self.label_especialidade.pack(side="left")
        self.especialidade_escolhida = tk.StringVar()
        self.combobox_especialidades = ttk.Combobox(self.frame_especialidade, width=20, textvariable=self.especialidade_escolhida)
        self.combobox_especialidades.pack(side="left")
        self.combobox_especialidades.bind("<<ComboboxSelected>>", controle.atualizar_listbox)

        especialidades_validas = ['Pediatria', 'Cardiologia', 'Neurologia', 'Oftalmologia', 'Ortopedia', 'Gastroenterologia','Psiquiatria', 'Pneumologia']
        self.combobox_especialidades["values"] = especialidades_validas
        


        self.label_medico = tk.Label(self.frame_medico, text="Escolha o médico:")
        self.label_medico.pack(side="left")
        self.listbox_medico = tk.Listbox(self.frame_medico, width=30, height=10)
        self.listbox_medico.pack(side="left")


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
    def atualizar_medicos(self, lista_medicos):
        self.listbox_medico.delete(0, tk.END)
        for medico in lista_medicos:
            self.listbox_medico.insert(tk.END, medico.nome)
    def adicionar_medico(self, medico_obj):
            self.lista_medicos.append(medico_obj)
            messagebox.showinfo("Sucesso", f"Consulta MARCADA")
    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
