# Importa los módulos necesarios
import network
import time

# Configura las credenciales de tu red WiFi
SSID = 'WRITE YOUR NAME NETWORK HERE'
PASS = 'WRITE YOUR PASSWORD NETWORK HERE'

# Número de intentos de conexión antes de abandonar
CONNECTING_TRIES = 3

# Función para conectar a WiFi
def wifi_connect():
    # Crea un objeto WLAN (Wireless Local Area Network)
    wifi = network.WLAN(network.STA_IF)
    # Activa la interfaz WiFi
    wifi.active(True)

    # Muestra un mensaje indicando el intento de conexión
    print('Connecting to "{}"'.format(SSID))

    # Intenta conectarse a la red WiFi
    wifi.connect(SSID, PASS)

    # Pausa durante un breve período para permitir que se establezca la conexión
    time.sleep(5)

    # Verifica si la conexión es exitosa
    if wifi.isconnected():
        # Muestra un mensaje de éxito si se ha conectado
        print('Connection Successfully to "{}"'.format(SSID))
        # Devuelve True para indicar una conexión exitosa
        return True

    # Desconéctate si la conexión no fue exitosa
    wifi.disconnect()
    # Muestra un mensaje de error
    print('Connection Error')

    # Devuelve False para indicar una conexión no exitosa
    return False

# Cargar el script y reiniciar el dispositivo con Pymakr
print('Uploading and running the script...')
# Agrega instrucciones específicas de carga para Pymakr y reinicio del dispositivo
# Pymakr suele tener botones específicos para estas acciones
# Asegúrate de ajustar esto según las funciones proporcionadas por Pymakr

# Pymakr: Presiona el botón de carga (Upload) en tu entorno de desarrollo
# y realiza un reinicio (hard reset) del dispositivo según la documentación de Pymakr.
# Esto puede variar según la placa y configuración específica.

# Ejemplo:
# 1. Presiona el botón "Upload" en Pymakr.
# 2. Realiza un reinicio del dispositivo (hard reset) según las instrucciones de Pymakr.

print('Upload and run complete!')
