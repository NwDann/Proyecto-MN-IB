# Proyecto de Métodos Numéricos: Cálculo de Intersección de Escaleras

Este proyecto forma parte de la asignatura de Métodos Numéricos y tiene como objetivo calcular la distancia o ancho de un pasillo, donde dos escaleras se apoyan en paredes opuestas y se intersectan a una cierta altura. Utiliza el método de la bisección para resolver el problema y presenta una interfaz gráfica para ingresar los datos y visualizar los resultados.

## Descripción

El programa permite al usuario ingresar las longitudes de dos escaleras y la altura de su intersección desde el suelo. A partir de estos datos, el programa calcula el ancho del pasillo utilizando el método de la bisección. Además, genera una gráfica que muestra las escaleras, el punto de intersección y el ancho del pasillo calculado.

## Instalación

Sigue estos pasos para instalar y configurar el entorno del proyecto:

1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/NwDann/Proyecto-MN-IB.git
    cd Proyecto-MN-IB
    ```

2. **Crear un entorno virtual:**
    ```bash
    python -m venv venv
    ```

3. **Activar el entorno virtual:**
    - En Windows (PowerShell):
      ```powershell
      .\venv\Scripts\activate
      ```
    - En Windows (CMD):
      ```cmd
      venv\Scripts\activate.bat
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. **Ejecutar la aplicación:**
    ```bash
    python main.py
    ```

2. **Ingresar los datos:**
    - Longitud de la escalera 1 (m).
    - Longitud de la escalera 2 (m).
    - Altura desde el suelo a la intersección (m).

3. **Calcular el ancho del pasillo:**
    - Haz clic en el botón "Calcular".

4. **Visualizar los resultados:**
    - El ancho del pasillo calculado se mostrará en un mensaje emergente.
    - Una gráfica se generará, mostrando las escaleras, el punto de intersección y el ancho del pasillo.

## Ejemplo

Para calcular el ancho de un pasillo donde dos escaleras de 5 m y 4 m se intersectan a una altura de 3 m, ingresa los siguientes valores:
- Longitud de la escalera 1: 5
- Longitud de la escalera 2: 4
- Altura: 3

Haz clic en "Calcular" para obtener el resultado y visualizar la gráfica correspondiente.

## Documentación del Código

### `calcular_raiz(x1, x2, h)`
Calcula el ancho del pasillo utilizando el método de la bisección.
- **Parámetros:**
  - `x1` (float): Longitud de la escalera 1.
  - `x2` (float): Longitud de la escalera 2.
  - `h` (float): Altura desde el suelo a la intersección.
- **Retorna:**
  - `float`: Ancho del pasillo calculado.

### `calcular()`
Maneja el evento de clic en el botón "Calcular", obtiene los valores ingresados por el usuario, calcula el ancho del pasillo y muestra los resultados.

### `graficar_funcion(x1, x2, h, raiz)`
Genera la gráfica que muestra las escaleras, el punto de intersección y el ancho del pasillo.
- **Parámetros:**
  - `x1` (float): Longitud de la escalera 1.
  - `x2` (float): Longitud de la escalera 2.
  - `h` (float): Altura desde el suelo a la intersección.
  - `raiz` (float): Ancho del pasillo calculado.

## Requisitos del Sistema

- Python 3.x
- Bibliotecas adicionales: tkinter, matplotlib, numpy, scipy
