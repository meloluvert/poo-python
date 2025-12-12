```markdown
# Resumo Rápido Python + Tkinter para Prova de POO

Guia prático e direto com os conceitos que **mais caem** nas suas provas:  
dicionários, listas (com list comprehension), combobox, listbox e truques comuns.

---

## 1. Dicionários em Python (o que mais uso nas provas)

Dicionário = estrutura chave → valor (como um "banco de dados" simples)

```python
# Criar dicionário vazio
meu_dict = {}

# Criar com valores
pizzas = {
    101: "Portuguesa",
    102: "Calabresa",
    105: "Marguerita"
}

# Outro exemplo comum: código → objeto Pizza
pizzas_obj = {
    101: Pizza(101, "Portuguesa", 65.00),
    102: Pizza(102, "Calabresa", 55.00)
}
```

### Operações básicas

```python
# Adicionar ou alterar
pizzas[103] = "Lombinho"

# Acessar valor
print(pizzas[101])          # → Portuguesa

# Verificar se chave existe
if 999 in pizzas:
    print("existe")
else:
    print("não tem")

# Pegar valor com segurança
pizza = pizzas.get(999)     # retorna None se não existir
pizza = pizzas.get(999, "Não encontrada")  # valor padrão

# Percorrer
for codigo, descricao in pizzas.items():
    print(codigo, "-", descricao)

# Só chaves
for codigo in pizzas.keys():

# Só valores
for desc in pizzas.values():
```

**Por que uso dicionário nas provas?**  
Porque é perfeito para ligar o que aparece no Combobox (`"101 - Portuguesa"`) com o objeto real ou com outro dado.

---

## 2. Listas e List Comprehension (vetor rápido)

```python
# Lista normal
numeros = [1, 2, 3, 4, 5]

# List comprehension (muito comum nas provas)
quadrados = [x*x for x in range(1, 6)]   # → [1, 4, 9, 16, 25]

# Filtrar
pares = [x for x in range(10) if x % 2 == 0]  # → [0,2,4,6,8]

# Com dicionário → lista de strings para Combobox
opcoes = [f"{cod} - {desc}" for cod, desc in pizzas.items()]
# ou com objetos
opcoes = [f"{p.codigo} - {p.descricao}" for p in lista_pizzas]
```

**Uso clássico em Combobox**
```python
self.combobox['values'] = opcoes
```

---

## 3. Combobox + Listbox (o padrão das suas provas)

### Combobox (escolher uma opção)

```python
self.combo = ttk.Combobox(frame, width=40)
self.combo.pack()

# Preencher
opcoes = ["op1", "op2", "op3"]
self.combo['values'] = opcoes

# Pegar o que o usuário escolheu
selecionado = self.combo.get()          # retorna a string inteira
```

### Listbox (mostrar lista de coisas)

```python
self.listbox = tk.Listbox(frame, width=50, height=10)
self.listbox.pack()

# Adicionar itens
self.listbox.insert(tk.END, "Linha 1")
self.listbox.insert(tk.END, "Linha 2")

# Limpar tudo
self.listbox.delete(0, tk.END)

# Pegar item selecionado
indices = self.listbox.curselection()   # tuple com índices
if indices:
    pos = indices[0]
    texto = self.listbox.get(pos)
```

### Ligando Combobox → Listbox (exemplo clássico)

```python
def atualizar_listbox(self, event=None):
    self.listbox.delete(0, tk.END)
    
    nome_medico = self.combo_medico.get()
    
    # dicionário que liga médico → lista de consultas
    consultas_do_medico = self.controle.gerar_dict_medico_consultas().get(nome_medico, [])
    
    if not consultas_do_medico:
        self.listbox.insert(tk.END, "Nenhuma consulta")
        return
        
    for dia, hora, paciente in consultas_do_medico:
        self.listbox.insert(tk.END, f"Dia {dia} - {hora}h - {paciente}")
        
# Bind no combobox
self.combo_medico.bind("<<ComboboxSelected>>", self.atualizar_listbox)
```

---

## 4. Truques rápidos que sempre uso

```python
# Converter string para int/float com segurança
try:
    valor = int(entry.get())
    valor = float(entry.get())
except ValueError:
    messagebox.showerror("Erro", "Número inválido")

# Limpar entry
entry.delete(0, tk.END)

# Inserir valor padrão
entry.insert(0, "1")

# Formatar reais
f"R$ {valor:.2f}"

# String para código (quando uso no combobox "101 - Portuguesa")
texto = combo.get()               # "101 - Portuguesa"
codigo = int(texto.split(" - ")[0])
```

---

## 5. Estrutura típica dos meus arquivos

- `main.py` → menu dropdown + ControlePrincipal
- `xxxx.py` → 
  - Classe do modelo (Pizza, Aluno, Médico...)
  - View de cadastro (Toplevel com frames)
  - ControleXXXX (lógica, lista/dict, salvar/carregar se precisar)

**Dica de ouro na prova:**  
Sempre uso dicionário quando preciso ligar o que o usuário vê (combobox/listbox) com o objeto real ou com outro dado.

---

Boa sorte na prova!  
Você já tem o padrão na mão, é só manter a calma e ir montando pedaço por pedaço.  
Qualquer dúvida na hora, respira e lembra: "já fiz isso mil vezes no gerador".  

Você vai arrebentar! 🚀
```
```