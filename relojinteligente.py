import tkinter as tk
import time

class RelojInteligente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reloj Inteligente")
        self.geometry("300x100")
        self.reloj_label = tk.Label(self, font=("Helvetica", 24))
        self.reloj_label.pack(pady=20)
        self.actualizar_hora()

    def actualizar_hora(self):
        hora_actual = time.strftime("%H:%M:%S")
        self.reloj_label.config(text=hora_actual)
        self.after(1000, self.actualizar_hora)

if __name__ == "__main__":
    app = RelojInteligente()
    app.mainloop()
