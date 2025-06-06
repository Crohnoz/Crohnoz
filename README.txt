==============================
    Crohnoz® - Sistema de Mantenimiento
==============================

Versión portable para Windows 10/11
Creado por: Enrique Flores

--------------------------------------
📦 CONTENIDO DEL PAQUETE
--------------------------------------
- crohnoz_gui.py .......... Script principal
- crohnoz_gui_logo.png .... Logo para la interfaz
- crohnoz_icon.ico ........ Ícono personalizado para empaquetar .exe

--------------------------------------
🚀 CÓMO EJECUTAR LA APLICACIÓN
--------------------------------------

1. Activa tu entorno virtual (si tienes uno), o abre la terminal CMD / PowerShell.

2. Ejecuta el archivo:
   > python crohnoz_gui.py

(Recuerda tener Python instalado. Requiere: psutil, plyer, pillow)

Para instalar las dependencias:
   > pip install psutil plyer pillow

--------------------------------------
🛠️ CÓMO CREAR EL ARCHIVO .EXE PORTABLE
--------------------------------------

1. Instala PyInstaller si no lo tienes:
   > pip install pyinstaller

2. Ejecuta este comando en la carpeta:
   > pyinstaller --onefile --icon=crohnoz_icon.ico --name Crohnoz crohnoz_gui.py

3. Encontrarás el .exe en la carpeta /dist

Puedes compartir solo ese archivo .exe como versión portable.

--------------------------------------
🔐 NOTA DE SEGURIDAD
--------------------------------------

Este software no recolecta datos, ni se conecta a internet.
Todo el mantenimiento se realiza localmente desde tu PC.

--------------------------------------
💬 Soporte
--------------------------------------
Puedes mejorar esta app o distribuirla con fines educativos.

Crohnoz® 2025 - Todos los derechos reservados.
