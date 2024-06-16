import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect

# Función que calcula la raíz
def root(x1, x2, h):
    def w(w):
        return (h * w) / (x2 ** 2 - w ** 2) ** 0.5 + (h * w) / (x1 ** 2 - w ** 2) ** 0.5 - w
    
    a = 0.01
    b = min(x1, x2) - 0.01
    
    try:
        result = bisect(w, a, b)
        return result
    except:
        return None

# Función para manejar el evento de clic en el botón
def calculate():
    try:
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())
        h = float(entry_h.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, ingrese números válidos.")
        return
    
    result = root(x1, x2, h)
    
    if result:
        messagebox.showinfo("Resultado", f"El valor en metros de la distancia o ancho del pasillo es: {result:.4f} m")
        
        # Graficar la función y las raíces
        plot_function(x1, x2, h, result)
    else:
        messagebox.showerror("Sin solución", "No hay solución para las longitudes dadas.")

# Función para graficar la función y las raíces
def plot_function(x1, x2, h, root):
    x_values = np.linspace(0.01, min(x1, x2) - 0.01, 100)
    y_values = [(h * w) / (x2 ** 2 - w ** 2) ** 0.5 + (h * w) / (x1 ** 2 - w ** 2) ** 0.5 - w for w in x_values]
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label='Función')
    ax.scatter(root, 0, color='red', label='Raíz')
    ax.set_xlabel('Ancho del pasillo (m)')
    ax.set_ylabel('Función')
    ax.set_title('Función para calcular el ancho del pasillo')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    ax.grid(True)
    
    canvas = FigureCanvasTkAgg(fig, master=root_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Configuración de la ventana principal
root_window = tk.Tk()
root_window.title("Cálculo de Intersección de Escaleras")
root_window.geometry("800x600")
root_window.configure(bg="black")

# Frame para los campos de entrada
frame = tk.Frame(root_window, bg="black")
frame.pack(pady=50)

# Configuración de estilos personalizados
label_style = {'bg': 'black', 'fg': 'white', 'font': ('Arial', 12)}
entry_style = {'bg': 'black', 'fg': 'white', 'insertbackground': 'white', 'highlightbackground': 'white', 'highlightcolor': 'white', 'highlightthickness': 1}
button_style = {'bg': 'black', 'fg': 'white', 'font': ('Arial', 12), 'highlightbackground': 'white', 'highlightcolor': 'white', 'highlightthickness': 1}

# Etiquetas y campos de entrada
label_x1 = tk.Label(frame, text="Longitud de la escalera 1 (m):", **label_style)
label_x1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_x1 = tk.Entry(frame, **entry_style)
entry_x1.grid(row=0, column=1, padx=10, pady=10)

label_x2 = tk.Label(frame, text="Longitud de la escalera 2 (m):", **label_style)
label_x2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_x2 = tk.Entry(frame, **entry_style)
entry_x2.grid(row=1, column=1, padx=10, pady=10)

label_h = tk.Label(frame, text="Altura desde el suelo a la intersección (m):", **label_style)
label_h.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_h = tk.Entry(frame, **entry_style)
entry_h.grid(row=2, column=1, padx=10, pady=10)

# Botón para calcular
button_calculate = tk.Button(root_window, text="Calcular", command=calculate, **button_style)
button_calculate.config(width=20, height=2)  # Ajustar el tamaño del botón
button_calculate.pack(pady=20)

# Ejecutar la aplicación
root_window.mainloop()
