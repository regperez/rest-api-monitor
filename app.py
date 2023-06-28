import os
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime

# Leer el archivo de texto que contiene la lista de API REST
with open("api_list.txt", "r") as file:
    api_list = file.read().splitlines()

# Verificar la salud de cada API
for api in api_list:
    response = requests.get(api)
    status_code = response.status_code

    # Comprobar si la respuesta no es 200 (OK)
    if status_code != 200:
        # Configurar destinatarios y contenido del correo electrónico
        recipients = ['destinatario1@example.com', 'destinatario2@example.com']
        subject = 'Alerta de API'
        body = f'La API {api} ha devuelto un código de estado: {status_code}'

        # Crear objeto Mail de SendGrid
        message = Mail(
            from_email='tu_email@example.com',
            to_emails=recipients,
            subject=subject,
            plain_text_content=body
        )

        try:
            # Enviar el correo electrónico utilizando la API de SendGrid
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print('Correo electrónico enviado correctamente')
        except Exception as e:
            # Registrar el error al enviar el correo en el archivo de log
            error_message = f'Error al enviar el correo electrónico: {str(e)}'
            print(error_message)
            # Obtener la fecha y hora actual
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Guardar el mensaje de error en el archivo de log
            with open("error_log.txt", "a") as log_file:
                log_file.write(f'{current_time}: {error_message}\n')
                log_file.write(f'{current_time}: Respuesta de la API {api}: {response.status_code}\n')
    else:
        print(f'La API {api} está saludable (código de estado 200)')
