# Codigo Escrito por victor Lau 2/16/2025
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

import file_functions
import gui_functions

# Variable global para almacenar el código filtrado
codigo_final = ""

def filtrar_codigo():
    global codigo_final
    codigo_completo = entry_codigo.get().strip()
    if not codigo_completo:
        messagebox.showwarning("Advertencia", "Por favor, escanee o ingrese un código de barras.")
        return
    codigo_procesado = codigo_completo.replace("/", "-")
    prefijo = entry_prefijo.get().strip()
    sufijo = entry_sufijo.get().strip()
    if prefijo and codigo_procesado.startswith(prefijo):
        codigo_procesado = codigo_procesado[len(prefijo):]
    if sufijo and codigo_procesado.endswith(sufijo):
        codigo_procesado = codigo_procesado[:-len(sufijo)]
    codigo_final = codigo_procesado
    root.clipboard_clear()
    root.clipboard_append(codigo_final)
    label_resultado.config(text=f"Código filtrado y copiado:\n{codigo_final}")
    entry_codigo.delete(0, tk.END)

def on_enter(event):
    filtrar_codigo()

def save_to_csv():
    descripcion = entry_descripcion.get().strip()
    cantidad = entry_cantidad.get().strip()
    file_functions.guardar_en_csv(descripcion, codigo_final, cantidad)

# Crear ventana principal
root = tk.Tk()
root.title("Filtro de Códigos de Barras")
root.geometry("500x600")
root.resizable(False, False)

# Cambiar el icono de la aplicación a "logo.png"
try:
    icon_image = Image.open("logo.png")
    icon_image = icon_image.resize((32,32))
    app_icon = ImageTk.PhotoImage(icon_image)
    root.iconphoto(True, app_icon)
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar el icono de la aplicación. Error: {e}")

# Cargar y redimensionar logos
try:
    image = Image.open("Logo.PNG")
    image = image.resize((100,100))
    logo = ImageTk.PhotoImage(image)
    label_logo = tk.Label(root, image=logo)
    label_logo.place(x=50, y=10)
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar el logo de la empresa. Error: {e}")

try:
    siemens_image = Image.open("Siemens.png")
    original_width, original_height = siemens_image.size
    new_width = 250
    new_height = int(new_width * original_height / original_width)
    siemens_image = siemens_image.resize((new_width, new_height))
    siemens_logo = ImageTk.PhotoImage(siemens_image)
    label_siemens = tk.Label(root, image=siemens_logo)
    label_siemens.place(x=450 - new_width - 10, y=0)
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar el logo Siemens. Error: {e}")

# Menús
menubar = tk.Menu(root)

menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Nuevo CSV", command=file_functions.crear_nuevo_csv)
menu_archivo.add_command(label="Guardar en CSV", command=save_to_csv)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=menu_archivo)

menu_config = tk.Menu(menubar, tearoff=0)
# Pasamos el root y un diccionario con las referencias a los widgets que se actualizarán
widgets = {}
menubar.add_cascade(label="Configuración", menu=menu_config)
menu_config.add_command(label="Ajustar tamaño de texto", command=lambda: gui_functions.open_config(root, widgets))

menu_info = tk.Menu(menubar, tearoff=0)
menu_info.add_command(label="Ver GitHub", command=gui_functions.open_info)
menubar.add_cascade(label="Info", menu=menu_info)

root.config(menu=menubar)

# Frame principal para la interfaz
frame_main = tk.Frame(root)
frame_main.place(x=0, y=120, relwidth=1, relheight=0.75)

label_instruccion = tk.Label(frame_main, text="Escanee o ingrese el código de barras:", font=("Arial", 12))
label_instruccion.pack(pady=5)

entry_codigo = tk.Entry(frame_main, font=("Arial", 16), width=30)
entry_codigo.pack(pady=5)
entry_codigo.bind("<Return>", on_enter)
entry_codigo.focus()

frame_configuracion = tk.Frame(frame_main)
frame_configuracion.pack(pady=10)

label_prefijo = tk.Label(frame_configuracion, text="Prefijo a eliminar:", font=("Arial", 12))
label_prefijo.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_prefijo = tk.Entry(frame_configuracion, font=("Arial", 12), width=15)
entry_prefijo.grid(row=0, column=1, padx=5, pady=5)
entry_prefijo.insert(0, "1p")

label_sufijo = tk.Label(frame_configuracion, text="Sufijo a eliminar:", font=("Arial", 12))
label_sufijo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_sufijo = tk.Entry(frame_configuracion, font=("Arial", 12), width=15)
label_sufijo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_sufijo = tk.Entry(frame_configuracion, font=("Arial", 12), width=15)
entry_sufijo.grid(row=1, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame_configuracion, text="Descripción:", font=("Arial", 12))
label_descripcion.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_descripcion = tk.Entry(frame_configuracion, font=("Arial", 12), width=25)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

label_cantidad = tk.Label(frame_configuracion, text="Cantidad:", font=("Arial", 12))
label_cantidad.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_cantidad = tk.Entry(frame_configuracion, font=("Arial", 12), width=15)
entry_cantidad.grid(row=3, column=1, padx=5, pady=5)  # Aquí se posiciona entry_cantidad
entry_cantidad.insert(0, "1")

boton_filtrar = tk.Button(frame_main, text="Filtrar Código", font=("Arial", 12), command=filtrar_codigo)
boton_filtrar.pack(pady=10)

label_resultado = tk.Label(frame_main, text="Resultado", font=("Arial", 14), fg="blue")
label_resultado.pack(pady=10)

boton_guardar = tk.Button(frame_main, text="Guardar a CSV", font=("Arial", 12), command=save_to_csv)
boton_guardar.pack(pady=10)

label_footer = tk.Label(root, text="V. Lau, I+C Corp 2025", font=("Arial", 10))
label_footer.place(relx=0, rely=0.95, relwidth=1)

# Llenar el diccionario de widgets para poder actualizar las fuentes en la ventana de configuración
widgets.update({
    'label_instruccion': label_instruccion,
    'entry_codigo': entry_codigo,
    'label_resultado': label_resultado,
    'label_prefijo': label_prefijo,
    'entry_prefijo': entry_prefijo,
    'label_sufijo': label_sufijo,
    'entry_sufijo': entry_sufijo,
    'label_descripcion': label_descripcion,
    'entry_descripcion': entry_descripcion,
    'label_cantidad': label_cantidad,
    'entry_cantidad': entry_cantidad,
    'label_footer': label_footer
})

root.mainloop()
