import tkinter as tk
from tkinter import messagebox

def coletar_teclas():
    def start_camera():
        exit_key = exit_key_var.get()
        left_key = left_key_var.get()
        right_key = right_key_var.get()
        jump_key = jump_key_var.get()

        if not (exit_key and left_key and right_key and jump_key):
            messagebox.showwarning("Campos obrigatórios", "Todos os campos de teclas devem ser preenchidos.")
            return None

        window.quit()

        return exit_key, left_key, right_key, jump_key

    window = tk.Tk()
    window.title("Configuração de Teclas")

    exit_key_var = tk.StringVar()
    left_key_var = tk.StringVar()
    right_key_var = tk.StringVar()
    jump_key_var = tk.StringVar()

    tk.Label(window, text="Exit Key:").grid(row=0, column=0)
    tk.Entry(window, textvariable=exit_key_var).grid(row=0, column=1)

    tk.Label(window, text="Left Key:").grid(row=1, column=0)
    tk.Entry(window, textvariable=left_key_var).grid(row=1, column=1)

    tk.Label(window, text="Right Key:").grid(row=2, column=0)
    tk.Entry(window, textvariable=right_key_var).grid(row=2, column=1)

    tk.Label(window, text="Jump Key:").grid(row=3, column=0)
    tk.Entry(window, textvariable=jump_key_var).grid(row=3, column=1)

    start_button = tk.Button(window, text="Start camera", command=lambda: start_camera())
    start_button.grid(row=4, columnspan=2)

    window.mainloop()
    window.quit()
    return start_camera()
