import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.simpledialog as simpledialog

class ItemPedido:
    def __init__(self, pizza1, pizza2=None, quantidade=1):
        self.pizza1 = pizza1
        self.pizza2 = pizza2
        self.quantidade = quantidade

    def get_valor_unitario(self):
        if self.pizza2:
            return max(self.pizza1.preco, self.pizza2.preco)
        return self.pizza1.preco

    def get_valor_total(self):
        return self.get_valor_unitario() * self.quantidade

    def get_descricao(self):
        if self.pizza2:
            return f"{self.pizza1.descricao}/{self.pizza2.descricao}"
        return self.pizza1.descricao

class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def get_total(self):
        return sum(item.get_valor_total() for item in self.itens)

class ViewCadastraPedido(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('500x400')
        self.title("Cadastrar Pedido")
        self.controle = controle

        # Frames
        self.frame_num = tk.Frame(self)
        self.frame_sabor1 = tk.Frame(self)
        self.frame_sabor2 = tk.Frame(self)
        self.frame_qtd = tk.Frame(self)
        self.frame_lista = tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_num.pack()
        self.frame_sabor1.pack()
        self.frame_sabor2.pack()
        self.frame_qtd.pack()
        self.frame_lista.pack()
        self.frame_botoes.pack()

        # Número do pedido
        tk.Label(self.frame_num, text="Número do pedido: ").pack(side="left")
        self.input_num = tk.Entry(self.frame_num, width=10)
        self.input_num.pack(side="left")
        self.btn_iniciar = tk.Button(self.frame_num, text="Iniciar Pedido")
        self.btn_iniciar.pack(side="left")
        self.btn_iniciar.bind("<Button>", controle.iniciar_pedido)

        # Sabor 1
        tk.Label(self.frame_sabor1, text="Sabor 1: ").pack(side="left")
        self.combo_sabor1 = ttk.Combobox(self.frame_sabor1, width=40)
        self.combo_sabor1.pack(side="left")

        # Sabor 2
        tk.Label(self.frame_sabor2, text="Sabor 2 (opcional): ").pack(side="left")
        self.combo_sabor2 = ttk.Combobox(self.frame_sabor2, width=40)
        self.combo_sabor2.pack(side="left")

        # Quantidade
        tk.Label(self.frame_qtd, text="Quantidade: ").pack(side="left")
        self.input_qtd = tk.Entry(self.frame_qtd, width=5)
        self.input_qtd.pack(side="left")
        self.input_qtd.insert(0, "1")

        self.btn_incluir = tk.Button(self.frame_qtd, text="Incluir Pizza")
        self.btn_incluir.pack(side="left")
        self.btn_incluir.bind("<Button>", controle.incluir_item)

        # Lista de itens
        self.listbox = tk.Listbox(self.frame_lista, width=60, height=10)
        self.listbox.pack()

        # Botões finais
        self.btn_fechar = tk.Button(self.frame_botoes, text="Fechar Pedido")
        self.btn_fechar.pack(side="left")
        self.btn_fechar.bind("<Button>", controle.fechar_pedido)

        self.btn_sair = tk.Button(self.frame_botoes, text="Sair")
        self.btn_sair.pack(side="left")
        self.btn_sair.bind("<Button>", lambda e: self.destroy())

        self.atualizar_combos()

    def atualizar_combos(self):
        pizzas = self.controle.controle_principal.controle_pizza.pizzas
        opcoes = [f"{p.codigo} - {p.descricao}" for p in pizzas.values()]
        vazio = [""] + opcoes
        self.combo_sabor1['values'] = opcoes
        self.combo_sabor2['values'] = vazio

    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ControlePedido():
    def __init__(self, controle_principal):
        self.controle_principal = controle_principal
        self.pedidos = {}
        self.pedido_atual = None

    def cadastrar_view(self):
        self.view = ViewCadastraPedido(self)

    def iniciar_pedido(self, event):
        try:
            num = int(self.view.input_num.get())
            if num in self.pedidos:
                messagebox.showerror("Erro", "Pedido já existe!")
                return
            self.pedido_atual = Pedido(num)
            self.view.listbox.delete(0, tk.END)
            messagebox.showinfo("Sucesso", f"Pedido {num} iniciado!")
        except ValueError:
            messagebox.showerror("Erro", "Número inválido!")

    def _get_pizza(self, texto):
        if not texto:
            return None
        cod = int(texto.split(" - ")[0])
        return self.controle_principal.controle_pizza.get_pizza(cod)

    def incluir_item(self, event):
        if not self.pedido_atual:
            messagebox.showwarning("Atenção", "Inicie o pedido primeiro!")
            return

        s1 = self.view.combo_sabor1.get()
        s2 = self.view.combo_sabor2.get()

        if not s1:
            messagebox.showwarning("Atenção", "Escolha pelo menos um sabor!")
            return

        pizza1 = self._get_pizza(s1)
        pizza2 = self._get_pizza(s2)

        try:
            qtd = int(self.view.input_qtd.get())
            if qtd <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida!")
            return

        item = ItemPedido(pizza1, pizza2, qtd)
        self.pedido_atual.adicionar_item(item)

        desc = f"{qtd}x {item.get_descricao()} - R$ {item.get_valor_total():.2f}"
        self.view.listbox.insert(tk.END, desc)

    def fechar_pedido(self, event):
        if not self.pedido_atual:
            return
        if not self.pedido_atual.itens:
            messagebox.showwarning("Atenção", "Adicione pelo menos uma pizza!")
            return

        self.pedidos[self.pedido_atual.numero] = self.pedido_atual
        messagebox.showinfo("Sucesso", f"Pedido {self.pedido_atual.numero} fechado! Total: R$ {self.pedido_atual.get_total():.2f}")

        self.pedido_atual = None
        self.view.listbox.delete(0, tk.END)
        self.view.input_num.delete(0, tk.END)
        self.view.combo_sabor1.set("")
        self.view.combo_sabor2.set("")
        self.view.input_qtd.delete(0, tk.END)
        self.view.input_qtd.insert(0, "1")

    def consultar_view(self):
        num_str = simpledialog.askstring("Consultar Pedido", "Digite o número do pedido:")
        if num_str is None:
            return
        try:
            num = int(num_str)
            pedido = self.pedidos.get(num)
            if not pedido:
                messagebox.showinfo("Erro", "Pedido não encontrado!")
                return

            texto = f"Número do pedido: {pedido.numero}\n\n"
            for item in pedido.itens:
                texto += f"{item.quantidade}x {item.get_descricao()} - R$ {item.get_valor_total():.2f}\n"
            texto += f"\nTotal do pedido: R$ {pedido.get_total():.2f}"

            messagebox.showinfo("Pedido", texto)
        except ValueError:
            messagebox.showerror("Erro", "Número inválido!")