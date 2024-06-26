import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect

# Variable global del gráfico de las escaleras
canvas = None

def calcular_raiz(x1, x2, h):
    """
    Calcula la raíz de la ecuación que determina el ancho del pasillo.

    Parámetros:
    - x1: Longitud de la primera escalera (float)
    - x2: Longitud de la segunda escalera (float)
    - h: Altura desde el suelo a la intersección de las escaleras (float)

    Retorna:
    - Ancho del pasillo (float) si se encuentra una solución, de lo contrario None.
    """
    def ecuacion(w):
        return (h * w) / (x2 ** 2 - w ** 2) ** 0.5 + (h * w) / (x1 ** 2 - w ** 2) ** 0.5 - w
    
    a = 0.01
    b = min(x1, x2) - 0.01
    
    try:
        resultado = bisect(ecuacion, a, b)
        return resultado
    except Exception as e:
        print("Error al calcular la raíz:", e)
        return None

def calcular():
    """
    Maneja el evento de clic en el botón de calcular, obteniendo los valores de entrada,
    calculando el ancho del pasillo y graficando las escaleras.
    """
    try:
        x1 = float(entrada_x1.get())
        x2 = float(entrada_x2.get())
        h = float(entrada_h.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, ingrese números válidos.")
        return
    
    resultado = calcular_raiz(x1, x2, h)
    
    if resultado:
        messagebox.showinfo("Resultado", f"El valor en metros de la distancia o ancho del pasillo es: {resultado:.4f} m")
        
        # Graficar la función y las escaleras
        graficar_funcion(x1, x2, h, resultado)
    else:
        messagebox.showerror("Sin solución", "No hay solución para las longitudes dadas.")

def graficar_funcion(x1, x2, h, raiz):
    """
    Grafica la posición de las escaleras y su punto de intersección en el pasillo.

    Parámetros:
    - x1: Longitud de la primera escalera (float)
    - x2: Longitud de la segunda escalera (float)
    - h: Altura desde el suelo a la intersección de las escaleras (float)
    - raiz: Ancho del pasillo (float)
    """
    global canvas
    
    if canvas:
        canvas.get_tk_widget().pack_forget()
        canvas = None
    
    fig, ax = plt.subplots()
    
    # Coordenadas de las escaleras
    x1_altura = (x1**2 - raiz**2)**0.5 
    x_escalera1 = [0, raiz]
    y_escalera1 = [0, x1_altura]
    
    x2_altura = (x2**2 - raiz**2)**0.5 
    x_escalera2 = [raiz, 0]
    y_escalera2 = [0, x2_altura]
    
    # Graficar las escaleras
    ax.plot(x_escalera1, y_escalera1, label=f'Escalera 1 ({x1} m)', color='blue')
    ax.plot(x_escalera2, y_escalera2, label=f'Escalera 2 ({x2} m)', color='green')
    
    # Punto de intersección
    x_interseccion = h / np.tan(np.arctan(x1_altura / raiz))
    y_interseccion = h
    ax.scatter(x_interseccion, y_interseccion, color='red', zorder=5)
    ax.text(x_interseccion, y_interseccion, f'({raiz:.2f}, {h:.2f})', fontsize=10, verticalalignment='bottom')
    
    # Configurar límites del gráfico para que se ajusten a las dimensiones de las escaleras
    ax.set_xlim(0, raiz)
    y_max = max(x1_altura, x2_altura)
    ax.set_ylim(0, y_max + 1)
    
    ax.set_xlabel('Ancho del pasillo (m)')
    ax.set_ylabel('Altura (m)')
    ax.set_title('Intersección de Escaleras')
    ax.legend()
    ax.grid(True)
    
    canvas = FigureCanvasTkAgg(fig, master=ventana_principal)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Cálculo de Intersección de Escaleras")
ventana_principal.geometry("800x600")
ventana_principal.configure(bg="black")

# Frame para los campos de entrada
marco = tk.Frame(ventana_principal, bg="black")
marco.pack(pady=50)

# Configuración de estilos personalizados
estilo_label = {'bg': 'black', 'fg': 'white', 'font': ('Arial', 12)}
estilo_entry = {'bg': 'black', 'fg': 'white', 'insertbackground': 'white', 'highlightbackground': 'white', 'highlightcolor': 'white', 'highlightthickness': 1}
estilo_boton = {'bg': 'black', 'fg': 'white', 'font': ('Arial', 12), 'highlightbackground': 'white', 'highlightcolor': 'white', 'highlightthickness': 1}

# Etiquetas y campos de entrada
label_x1 = tk.Label(marco, text="Longitud de la escalera 1 (m):", **estilo_label)
label_x1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada_x1 = tk.Entry(marco, **estilo_entry)
entrada_x1.grid(row=0, column=1, padx=10, pady=10)

label_x2 = tk.Label(marco, text="Longitud de la escalera 2 (m):", **estilo_label)
label_x2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_x2 = tk.Entry(marco, **estilo_entry)
entrada_x2.grid(row=1, column=1, padx=10, pady=10)

label_h = tk.Label(marco, text="Altura desde el suelo a la intersección (m):", **estilo_label)
label_h.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entrada_h = tk.Entry(marco, **estilo_entry)
entrada_h.grid(row=2, column=1, padx=10, pady=10)

# Botón para calcular
boton_calcular = tk.Button(ventana_principal, text="Calcular", command=calcular, **estilo_boton)
boton_calcular.config(width=20, height=2)  # Ajustar el tamaño del botón
boton_calcular.pack(pady=20)

def cerrar():
    """
    Finaliza la ejecución de la ventana principal cuando el usuario cierra la ventana.
    """
    ventana_principal.quit()
    ventana_principal.destroy()

# Configura la acción de cierre de la ventana principal
ventana_principal.protocol("WM_DELETE_WINDOW", cerrar)

# Ejecutar la aplicación
ventana_principal.mainloop()
