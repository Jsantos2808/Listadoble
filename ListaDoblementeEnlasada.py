import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

# Nodo para la lista doblemente enlazada
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Lista doblemente enlazada
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None

    def append(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = self.tail = self.current_node = new_node
        else:
            # Si estamos en el medio del historial, cortar el futuro
            if self.current_node and self.current_node.next:
                self.current_node.next = None
                self.tail = self.current_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.current_node = new_node

    def move_backward(self):
        if self.current_node and self.current_node.prev:
            self.current_node = self.current_node.prev

    def move_forward(self):
        if self.current_node and self.current_node.next:
            self.current_node = self.current_node.next

    def current(self):
        return self.current_node.value if self.current_node else ""

# Interfaz gráfica para el editor
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor con Historial")
        self.root.geometry("700x500")
        self.style = tb.Style("superhero")

        self.history = DoublyLinkedList()

        self.create_widgets()

    def create_widgets(self):
        # Área de texto
        self.text_area = tk.Text(self.root, height=20, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Botones
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.X, pady=5)

        ttk.Button(button_frame, text="Guardar Estado", command=self.save_state).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Deshacer", command=self.undo).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Rehacer", command=self.redo).pack(side=tk.LEFT, padx=5)

    def save_state(self):
        content = self.text_area.get("1.0", tk.END).strip()
        self.history.append(content)

    def undo(self):
        self.history.move_backward()
        self.update_text()

    def redo(self):
        self.history.move_forward()
        self.update_text()

    def update_text(self):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, self.history.current())

if __name__ == "__main__":
    root = tb.Window(themename="superhero")
    app = TextEditor(root)
    root.mainloop()
