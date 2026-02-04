import tkinter as tk
from tkinter import messagebox
import time
import subprocess

class ContadorRegresivo:
    def __init__(self, root):
        self.root = root
        self.root.title("Cuenta Regresiva")

        self.label_horas = tk.Label(root, text="Horas:")
        self.label_horas.grid(row=0, column=0, padx=5, pady=5)
        self.entry_horas = tk.Entry(root, width=5)
        self.entry_horas.grid(row=0, column=1, padx=5, pady=5)

        self.label_minutos = tk.Label(root, text="Minutos:")
        self.label_minutos.grid(row=1, column=0, padx=5, pady=5)
        self.entry_minutos = tk.Entry(root, width=5)
        self.entry_minutos.grid(row=1, column=1, padx=5, pady=5)

        self.label_segundos = tk.Label(root, text="Segundos:")
        self.label_segundos.grid(row=2, column=0, padx=5, pady=5)
        self.entry_segundos = tk.Entry(root, width=5)
        self.entry_segundos.grid(row=2, column=1, padx=5, pady=5)

        self.boton_iniciar = tk.Button(root, text="Iniciar cuenta regresiva", command=self.iniciar_cuenta)
        self.boton_iniciar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.boton_pausa = tk.Button(root, text="Pausar", command=self.pausar_cuenta)
        self.boton_pausa.grid(row=4, column=0, padx=5, pady=5)

        self.boton_detener = tk.Button(root, text="Detener", command=self.detener_cuenta)
        self.boton_detener.grid(row=4, column=1, padx=5, pady=5)

        self.label_tiempo = tk.Label(root, text="", font=("Arial", 24))
        self.label_tiempo.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.total_segundos = 0
        self.tiempo_restante = 0
        self.contando = False

    def iniciar_cuenta(self):
        horas = int(self.entry_horas.get()) if self.entry_horas.get() else 0
        minutos = int(self.entry_minutos.get()) if self.entry_minutos.get() else 0
        segundos = int(self.entry_segundos.get()) if self.entry_segundos.get() else 0
        self.total_segundos = segundos + minutos * 60 + horas * 3600
        self.tiempo_restante = self.total_segundos
        self.contando = True
        self.actualizar_tiempo()

    def actualizar_tiempo(self):
        while self.tiempo_restante > 0 and self.contando:
            horas = self.tiempo_restante // 3600
            minutos = (self.tiempo_restante % 3600) // 60
            segundos = self.tiempo_restante % 60

            tiempo_str = "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)
            self.label_tiempo.config(text=tiempo_str)
            self.root.update()

            time.sleep(1)
            self.tiempo_restante -= 1

        if self.tiempo_restante == 0:
            comando = "shutdown /s /t 0"
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            if resultado.returncode == 0:
                print("Comando ejecutado correctamente.")
            else:
                print("Ocurrió un error al ejecutar el comando:", resultado.stderr)


    def pausar_cuenta(self):
        self.contando = False
        self.boton_pausa.config(text="Reanudar", command=self.reanudar_cuenta)

    def reanudar_cuenta(self):
        self.contando = True
        self.boton_pausa.config(text="Pausar", command=self.pausar_cuenta)
        self.actualizar_tiempo()

    def detener_cuenta(self):
        self.contando = False
        self.tiempo_restante = self.total_segundos
        self.label_tiempo.config(text="00:00:00")

root = tk.Tk()
contador = ContadorRegresivo(root)
root.mainloop()