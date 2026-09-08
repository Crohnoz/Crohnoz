import os
import subprocess
import shutil
import psutil
import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime
from plyer import notification
from PIL import ImageTk, Image, ImageDraw
import platform
import socket

BRAND_BG = "#0A0B14"
BRAND_PURPLE = "#8B5CF6"
BRAND_MAGENTA = "#EC4899"
BRAND_CYAN = "#06B6D4"
BRAND_BLUE = "#3B82F6"
BRAND_TEXT = "#F8FAFC"


def notificar(titulo, mensaje):
    notification.notify(title=titulo, message=mensaje, app_name="Crohnoz Labs", timeout=5)


def log(mensaje):
    salida.insert(tk.END, f"{mensaje}\n")
    salida.see(tk.END)
    root.update()


def _mix(a, b, t):
    return tuple(round(a[i] * (1 - t) + b[i] * t) for i in range(3))


def build_brand_mark(size=170):
    """Render the canonical Crohnoz Future 1.0 signal mark in memory."""
    canvas = Image.new("RGBA", (254, 280), (0, 0, 0, 0))
    mask = Image.new("L", canvas.size, 0)
    draw_mask = ImageDraw.Draw(mask)

    bars = [
        (0, 72, 150),
        (38, 38, 66), (38, 116, 132),
        (76, 20, 230),
        (114, 0, 280),
        (152, 44, 70), (152, 128, 142),
        (190, 28, 230),
        (228, 66, 64), (228, 148, 94),
    ]

    for x, y, h in bars:
        draw_mask.rounded_rectangle((x, y, x + 26, y + h), radius=13, fill=255)

    gradient = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    pixels = gradient.load()
    top = (236, 72, 153)
    mid = (139, 92, 246)
    bottom = (6, 182, 212)
    for y in range(280):
        t = y / 279
        color = _mix(top, mid, t * 2) if t <= 0.5 else _mix(mid, bottom, (t - 0.5) * 2)
        for x in range(254):
            pixels[x, y] = (*color, 255)

    canvas = Image.composite(gradient, canvas, mask)
    canvas.thumbnail((size, size), Image.Resampling.LANCZOS)
    return canvas


def limpieza_avanzada():
    log("🧹 Ejecutando limpieza avanzada...")
    carpetas = [os.environ.get('TEMP'), r"C:\Windows\Prefetch", r"C:\Windows\SoftwareDistribution\Download", os.path.expanduser("~\\AppData\\Local\\Temp")]
    for carpeta in carpetas:
        try:
            shutil.rmtree(carpeta, ignore_errors=True)
            os.makedirs(carpeta, exist_ok=True)
            log(f"✔ Limpieza de: {carpeta}")
        except Exception as e:
            log(f"✖ Error limpiando {carpeta}: {e}")
    try:
        subprocess.run("powershell.exe -Command Clear-RecycleBin -Force", shell=True)
        log("✔ Papelera vaciada.")
    except Exception:
        log("✖ No se pudo vaciar la papelera.")
    notificar("Crohnoz Labs", "Limpieza avanzada completada.")


def revisar_sistema():
    log("🔧 Verificando archivos del sistema...")
    try:
        subprocess.run("sfc /scannow", shell=True)
        log("✔ SFC ejecutado.")
        subprocess.run("DISM /Online /Cleanup-Image /RestoreHealth", shell=True)
        log("✔ DISM ejecutado.")
        notificar("Crohnoz Labs", "Revisión del sistema completada.")
    except Exception as e:
        log(f"✖ Error en revisión de sistema: {e}")


def escanear_virus():
    log("🛡️ Ejecutando escaneo rápido con Windows Defender...")
    cmd = r'"%ProgramFiles%\\Windows Defender\\MpCmdRun.exe" -Scan -ScanType 1'
    try:
        subprocess.run(cmd, shell=True)
        log("✔ Escaneo completado.")
        notificar("Crohnoz Labs", "Escaneo antivirus finalizado.")
    except Exception as e:
        log(f"✖ Error al escanear: {e}")


def info_sistema():
    log("🖥️ Información del sistema:")
    try:
        log(f"Equipo: {platform.node()}")
        log(f"SO: {platform.system()} {platform.release()}")
        log(f"Procesador: {platform.processor()}")
        log(f"RAM total: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")
        log(f"Disco usado: {psutil.disk_usage('/').percent}%")
        ip = socket.gethostbyname(socket.gethostname())
        log(f"IP local: {ip}")
    except Exception as e:
        log(f"✖ Error: {e}")


def guardar_informe():
    archivo = f"Crohnoz_informe_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(salida.get(1.0, tk.END))
    log(f"📁 Informe guardado como {archivo}")
    notificar("Crohnoz Labs", f"Informe generado: {archivo}")


root = tk.Tk()
root.title("Crohnoz Labs - Mantenimiento del Sistema")
root.geometry("900x650")
root.configure(bg=BRAND_BG)

top_frame = tk.Frame(root, bg=BRAND_BG)
top_frame.pack(pady=10)

logo_img = build_brand_mark()
logo_tk = ImageTk.PhotoImage(logo_img)
tk.Label(top_frame, image=logo_tk, bg=BRAND_BG).pack(side=tk.LEFT, padx=10)

heading = tk.Frame(top_frame, bg=BRAND_BG)
heading.pack(side=tk.LEFT, padx=8)
tk.Label(heading, text="CROHNOZ LABS", fg=BRAND_TEXT, bg=BRAND_BG, font=("Segoe UI Semibold", 20)).pack(anchor="w")
tk.Label(heading, text="Tecnología que resuelve problemas reales.", fg=BRAND_CYAN, bg=BRAND_BG, font=("Segoe UI", 10)).pack(anchor="w")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#171826", foreground=BRAND_TEXT, padding=8, relief="flat", font=("Segoe UI", 10))
style.map("TButton", background=[("active", BRAND_PURPLE)], foreground=[("active", BRAND_TEXT)])

botones_frame = tk.Frame(root, bg=BRAND_BG)
botones_frame.pack(pady=15)

ttk.Button(botones_frame, text="🧹 Limpieza Avanzada", command=limpieza_avanzada).grid(row=0, column=0, padx=10, pady=5)
ttk.Button(botones_frame, text="🔧 Revisar Sistema", command=revisar_sistema).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(botones_frame, text="🛡️ Escaneo Antivirus", command=escanear_virus).grid(row=1, column=0, padx=10, pady=5)
ttk.Button(botones_frame, text="🖥️ Info Sistema", command=info_sistema).grid(row=1, column=1, padx=10, pady=5)
ttk.Button(botones_frame, text="📄 Guardar Informe", command=guardar_informe).grid(row=2, column=0, columnspan=2, pady=10)

salida = scrolledtext.ScrolledText(root, bg="#171826", fg=BRAND_TEXT, insertbackground=BRAND_TEXT, font=("Consolas", 10))
salida.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

root.mainloop()
