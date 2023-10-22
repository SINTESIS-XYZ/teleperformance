# Importa los módulos necesarios
import wifi  # Se asume que hay un módulo "wifi" que contiene la función "wifi_connect"
import usocket
import utime

# Configuración del servidor UDP
pd_host = 'Write your IP Here'  # Dirección IP del servidor UDP
pd_port = 8888  # Puerto del servidor UDP

# Conecta a la red WiFi usando la función previamente definida
wifi.wifi_connect()

# Muestra un mensaje indicando que el código se está ejecutando
print('Executing code')

# Crea un socket UDP
pd = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)

# Conecta el socket al servidor UDP
pd.connect((pd_host, pd_port))

# Muestra un mensaje indicando la conexión exitosa al servidor UDP
print('Connected to {}:{}'.format(pd_host, pd_port))
