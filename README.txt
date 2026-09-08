==============================
    Crohnoz Labs - Sistema de Mantenimiento
==============================

Versión portable para Windows 10/11
Brand System: Future 1.0
Claim: Tecnología que resuelve problemas reales.
Creado por: Enrique Flores

--------------------------------------
📦 CONTENIDO DEL PAQUETE
--------------------------------------
- crohnoz_gui.py ................ Interfaz con branding Future 1.0 generado en memoria
- brand/assets/crohnoz_icon.ico . Ícono oficial para empaquetar .exe
- brand/ ......................... Fuente canónica de identidad visual y tokens

--------------------------------------
🚀 CÓMO EJECUTAR LA APLICACIÓN
--------------------------------------

1. Activa tu entorno virtual (si tienes uno), o abre la terminal CMD / PowerShell.

2. Ejecuta el archivo:
   > python crohnoz_gui.py

Requiere: psutil, plyer, pillow

Para instalar las dependencias:
   > pip install psutil plyer pillow

--------------------------------------
🛠️ CÓMO CREAR EL ARCHIVO .EXE PORTABLE
--------------------------------------

1. Instala PyInstaller si no lo tienes:
   > pip install pyinstaller

2. Ejecuta:
   > pyinstaller Crohnoz.spec

Alternativamente:
   > pyinstaller --onefile --icon=brand/assets/crohnoz_icon.ico --name Crohnoz crohnoz_gui.py

3. Encontrarás el .exe en la carpeta /dist

--------------------------------------
🔐 NOTA DE SEGURIDAD
--------------------------------------

Este software no recolecta datos ni se conecta a internet.
Todo el mantenimiento se realiza localmente desde tu PC.

--------------------------------------
🎨 IDENTIDAD
--------------------------------------

La identidad visual oficial vive en /brand.
No volver a introducir logos anteriores en la raíz del repositorio.

Crohnoz Labs - Tecnología que resuelve problemas reales.
