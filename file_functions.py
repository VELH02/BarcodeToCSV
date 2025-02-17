# Codigo Escrito por victor Lau 2/16/2025
import tkinter as tk
from tkinter import messagebox, filedialog
import csv

# Usamos una variable global en este módulo para almacenar la ruta del CSV
csv_file_path = None

def crear_nuevo_csv():
    """Permite seleccionar la ubicación y nombre del CSV y escribe la cabecera."""
    global csv_file_path
    filename = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("Archivos CSV", "*.csv")],
        title="Crear nuevo archivo CSV"
    )
    if filename:
        csv_file_path = filename
        try:
            with open(csv_file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Descripción", "Código", "Cantidad"])
            messagebox.showinfo("CSV creado", f"Se ha creado el archivo CSV:\n{csv_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el archivo CSV. Error: {e}")
    return csv_file_path

def guardar_en_csv(descripcion, codigo_final, cantidad):
    """Guarda la descripción, el código y la cantidad en el CSV."""
    global csv_file_path
    if not codigo_final:
        messagebox.showwarning("Advertencia", "No hay código filtrado para guardar. Procese primero un código.")
        return
    if not cantidad:
        messagebox.showwarning("Advertencia", "Por favor, ingrese la cantidad.")
        return
    try:
        cantidad_int = int(cantidad)
    except ValueError:
        messagebox.showwarning("Advertencia", "La cantidad debe ser un número entero.")
        return
    if not csv_file_path:
        messagebox.showwarning("CSV no seleccionado", "No se ha seleccionado un archivo CSV. Se abrirá el diálogo para crearlo.")
        csv_file_path = crear_nuevo_csv()
        if not csv_file_path:
            return
    try:
        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([descripcion, codigo_final, cantidad_int])
        messagebox.showinfo("Registro guardado",
                            f"Se ha guardado el registro:\nDescripción: {descripcion}\nCódigo: {codigo_final}\nCantidad: {cantidad_int}\nen:\n{csv_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar en CSV. Error: {e}")
