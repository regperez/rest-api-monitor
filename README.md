# Monitor de estado de la API

Este script de Python permite monitorear el estado de varias APIs REST. Comprueba el estado de cada API en una lista y envía una alerta por correo electrónico si alguna API devuelve un código de estado distinto de 200.

## Requisitos

- Python 3.x
- sendgrid==6.7.0
- requests==2.25.1

## Instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado. Si no lo tienes, puedes descargarlo e instalarlo desde [python.org](https://www.python.org/downloads/).
3. Instala las dependencias necesarias ejecutando el siguiente comando:

pip install sendgrid requests


## Uso

1. Asegúrate de tener un archivo de texto llamado `api_list.txt` en el mismo directorio que este script. El archivo debe contener la lista de URLs de las APIs REST que deseas monitorear, una URL por línea.
2. Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentra este script.
3. Ejecuta el script utilizando el siguiente comando:

python api_monitor.py

El script verificará la salud de cada API en la lista y enviará una alerta por correo electrónico si alguna API devuelve un código de estado distinto de 200.

## Configuración del correo electrónico

Para que el script pueda enviar alertas por correo electrónico, debes configurar tus credenciales de SendGrid y proporcionar la lista de destinatarios.

1. Regístrate en una cuenta de SendGrid en [sendgrid.com](https://sendgrid.com/).
2. Obtén tu API Key de SendGrid siguiendo las instrucciones en [este enlace](https://docs.sendgrid.com/for-developers/sending-email/quickstart-python#step-3-create-an-api-key).

3. Copia tu API Key y asignala a una variable de entorno llamada `SENDGRID_API_KEY`.

En Linux y macOS, puedes hacerlo ejecutando el siguiente comando en la terminal:

export SENDGRID_API_KEY="TU_API_KEY"


En Windows, puedes configurar la variable de entorno utilizando el panel de control del sistema.

4. Abre el archivo `api_monitor.py` con un editor de texto y encuentra la siguiente línea de código:


recipients = ['destinatario1@example.com', 'destinatario2@example.com']

Reemplaza destinatario1@example.com y destinatario2@example.com con las direcciones de correo electrónico de los destinatarios a quienes deseas enviar las alertas.

Guarda los cambios y vuelve a ejecutar el script.

Registro de errores
Si ocurre un error al enviar el correo electrónico, se registrará en el archivo error_log.txt junto con la fecha y hora del error.

Este proyecto utiliza la biblioteca SendGrid para enviar correos electrónicos. Para obtener más información sobre cómo enviar correos electrónicos con SendGrid y Python, consulta la documentación oficial[1].
