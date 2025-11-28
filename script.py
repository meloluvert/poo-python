import os

def generate_script(class_name, attributes):
    # Converter class_name para PascalCase se necessário
    class_name = ''.join(word.capitalize() for word in class_name.split('_'))
    
    # Atributos como lista
    attr_list = [attr.strip() for attr in attributes.split(',')]
    
    # Gerar o conteúdo do Model
    model_content = f"""
class {class_name}:
    def __init__(self, {', '.join(attr_list)}):
"""
    for attr in attr_list:
        model_content += f"        self.__{attr} = {attr}\n"
    
    for attr in attr_list:
        model_content += f"""
    @property
    def {attr}(self):
        return self.__{attr}
    
    @{attr}.setter
    def {attr}(self, valor):
        self.__{attr} = valor
"""
    
    # Gerar o conteúdo do Controller
    controller_content = f"""
class Controle{class_name}():       

    def __init__(self, controle_principal):        
        if not os.path.isfile("{class_name.lower()}.pickle"):
            self.lista_{class_name.lower()}s = []
        else:
            with open("{class_name.lower()}.pickle", "rb") as f:
                self.lista_{class_name.lower()}s = pickle.load(f)
        self.controle_principal = controle_principal

    def get_{class_name.lower()}s(self):
        return self.lista_{class_name.lower()}s
    
    def get_{class_name.lower()}(self, nome):
        for {class_name.lower()} in self.lista_{class_name.lower()}s:
            if({class_name.lower()}.nome == nome):  # Assumindo 'nome' como chave, ajuste se necessário
                return {class_name.lower()}
    
    def cadastrar_view(self):
        self.view_cadastrar = ViewCadastra{class_name}(self) 

    def salvar_{class_name.lower()}s(self):
        if len(self.lista_{class_name.lower()}s) != 0:
            with open("{class_name.lower()}.pickle","wb") as f:
                pickle.dump(self.lista_{class_name.lower()}s, f)

    def limpar_input_cadastro(self, event):
"""
    for attr in attr_list:
        controller_content += f"        self.view_cadastrar.input_{attr}.delete(0, len(self.view_cadastrar.input_{attr}.get()))\n"
    
    controller_content += f"""
    def cadastrar(self, event):
        try: 
"""
    for attr in attr_list:
        controller_content += f"            {attr} = self.view_cadastrar.input_{attr}.get()\n"
    
    controller_content += f"""
            {class_name.lower()} = {class_name}({', '.join(attr_list)})
            self.lista_{class_name.lower()}s.append({class_name.lower()})
            self.view_cadastrar.mostrar_janela('Sucesso', '{class_name} cadastrado com sucesso')
            self.salvar_{class_name.lower()}s()
            self.limpar_input_cadastro(event)
            self.fechar_janela_cadastrar(event)
        except ValueError as error:
            self.view_cadastrar.mostrar_janela('Erro', error) 

    def fechar_janela_cadastrar(self, event):
        self.view_cadastrar.destroy()
"""
    
    # Gerar o conteúdo da View
    view_content = f"""
class ViewCadastra{class_name}(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x250')
        self.title("Cadastro de {class_name}")
        self.controle = controle
"""
    for attr in attr_list:
        view_content += f"""
        self.frame_{attr} = tk.Frame(self)
"""
    
    view_content += f"""
        self.frame_botoes = tk.Frame(self)
"""
    for attr in attr_list:
        view_content += f"""
        self.frame_{attr}.pack()
"""
    
    view_content += f"""
        self.frame_botoes.pack()
"""
    
    for attr in attr_list:
        attr_cap = attr.capitalize()
        view_content += f"""
        self.label_{attr} = tk.Label(self.frame_{attr},text="{attr_cap}: ")
        self.label_{attr}.pack(side="left")
        self.input_{attr} = tk.Entry(self.frame_{attr},  width=20)
        self.input_{attr}.pack(side="left")
"""
    
    view_content += f"""
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
"""
    
    # Combinar tudo
    full_content = f"""import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.simpledialog as simpledialog
import pickle
import os
import math

{model_content}

{controller_content}

{view_content}
"""
    
    # Escrever no arquivo
    filename = f"{class_name.lower()}.py"
    with open(filename, 'w') as f:
        f.write(full_content)
    
    print(f"Arquivo gerado: {filename}")

# Inputs do usuário
class_name = input("Qual a classe? ")
attributes = input("Quais atributos? (separados por vírgula) ")

generate_script(class_name, attributes)