import os
import subprocess
import shutil
import psutil
import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime
from plyer import notification
from PIL import ImageTk, Image
import platform
import socket

def notificar(titulo, mensaje):
    notification.notify(title=titulo, message=mensaje, app_name="Crohnoz", timeout=5)

def log(mensaje):
    salida.insert(tk.END, f"{mensaje}\n")
    salida.see(tk.END)
    root.update()

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
    except:
        log("✖ No se pudo vaciar la papelera.")
    notificar("Crohnoz", "Limpieza avanzada completada.")

def revisar_sistema():
    log("🔧 Verificando archivos del sistema...")
    try:
        subprocess.run("sfc /scannow", shell=True)
        log("✔ SFC ejecutado.")
        subprocess.run("DISM /Online /Cleanup-Image /RestoreHealth", shell=True)
        log("✔ DISM ejecutado.")
        notificar("Crohnoz", "Revisión del sistema completada.")
    except Exception as e:
        log(f"✖ Error en revisión de sistema: {e}")

def escanear_virus():
    log("🛡️ Ejecutando escaneo rápido con Windows Defender...")
    cmd = r'"%ProgramFiles%\\Windows Defender\\MpCmdRun.exe" -Scan -ScanType 1'
    try:
        subprocess.run(cmd, shell=True)
        log("✔ Escaneo completado.")
        notificar("Crohnoz", "Escaneo antivirus finalizado.")
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
    notificar("Crohnoz", f"Informe generado: {archivo}")

root = tk.Tk()
root.title("Crohnoz - Mantenimiento del Sistema")
root.geometry("900x650")
root.configure(bg="#1c1c1c")

top_frame = tk.Frame(root, bg="#1c1c1c")
top_frame.pack(pady=10)

logo_img = Image.open("crohnoz_gui_logo.png")
logo_tk = ImageTk.PhotoImage(logo_img)
tk.Label(top_frame, image=logo_tk, bg="#1c1c1c").pack(side=tk.LEFT, padx=10)

tk.Label(top_frame, text="Crohnoz® - Mantenimiento Avanzado", fg="#5ad1f5", bg="#1c1c1c", font=("Segoe UI Semibold", 18)).pack(side=tk.LEFT)

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#2e2e2e", foreground="#ffffff", padding=6, relief="flat", font=("Segoe UI", 10))
style.map("TButton", background=[("active", "#3a9bdc")], foreground=[("active", "#ffffff")])

botones_frame = tk.Frame(root, bg="#1c1c1c")
botones_frame.pack(pady=15)

ttk.Button(botones_frame, text="🧹 Limpieza Avanzada", command=limpieza_avanzada).grid(row=0, column=0, padx=10, pady=5)
ttk.Button(botones_frame, text="🔧 Revisar Sistema", command=revisar_sistema).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(botones_frame, text="🛡️ Escaneo Antivirus", command=escanear_virus).grid(row=1, column=0, padx=10, pady=5)
ttk.Button(botones_frame, text="🖥️ Info Sistema", command=info_sistema).grid(row=1, column=1, padx=10, pady=5)
ttk.Button(botones_frame, text="📄 Guardar Informe", command=guardar_informe).grid(row=2, column=0, columnspan=2, pady=10)

salida = scrolledtext.ScrolledText(root, bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff", font=("Consolas", 10))
salida.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

root.mainloop()
