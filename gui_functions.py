# Codigo Escrito por victor Lau 2/16/2025
import tkinter as tk
from tkinter import messagebox
import webbrowser

def update_all_fonts(new_size, widgets):
    """
    Actualiza el tamaño de fuente de los widgets.
    'widgets' debe ser un diccionario con las referencias:
       'label_instruccion', 'entry_codigo', 'label_resultado',
       'label_prefijo', 'entry_prefijo', 'label_sufijo', 'entry_sufijo',
       'label_descripcion', 'entry_descripcion', 'label_cantidad', 'entry_cantidad',
       'label_footer'
    """
    font_label = ("Arial", new_size)
    font_entry = ("Arial", new_size + 4)
    font_result = ("Arial", new_size + 2)
    font_footer = ("Arial", max(new_size - 2, 8))
    try:
        widgets['label_instruccion'].config(font=font_label)
        widgets['entry_codigo'].config(font=font_entry)
        widgets['label_resultado'].config(font=font_result)
        widgets['label_prefijo'].config(font=font_label)
        widgets['entry_prefijo'].config(font=font_label)
        widgets['label_sufijo'].config(font=font_label)
        widgets['entry_sufijo'].config(font=font_label)
        widgets['label_descripcion'].config(font=font_label)
        widgets['entry_descripcion'].config(font=font_label)
        widgets['label_cantidad'].config(font=font_label)
        widgets['entry_cantidad'].config(font=font_label)
        widgets['label_footer'].config(font=font_footer)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar las fuentes. Error: {e}")

def open_config(root, widgets):
    """
    Abre una ventana emergente para ajustar el tamaño del texto.
    'widgets' es el diccionario de widgets que se actualizarán.
    """
    config_window = tk.Toplevel(root)
    config_window.title("Configuración")
    config_window.geometry("300x150")
    label_adjust = tk.Label(config_window, text="Ajustar tamaño de texto:", font=("Arial", 12))
    label_adjust.pack(pady=10)
    scale_text_size = tk.Scale(config_window, from_=8, to=24, orient="horizontal",
                               command=lambda val: update_all_fonts(int(val), widgets))
    scale_text_size.set(12)
    scale_text_size.pack(pady=10)

def open_info():
    """Abre una ventana emergente con el enlace al repositorio de GitHub."""
    info_window = tk.Toplevel()
    info_window.title("Info")
    info_window.geometry("400x200")
    label_info = tk.Label(info_window, 
                          text="Código disponible en GitHub:\nhttps://github.com/VELH02/BarcodeToCSV",
                          font=("Arial", 12), justify="center")
    label_info.pack(pady=20)
    boton_github = tk.Button(info_window, text="Abrir GitHub", font=("Arial", 12),
                             command=lambda: webbrowser.open("https://github.com/VELH02/BarcodeToCSV"))
    boton_github.pack(pady=10)
