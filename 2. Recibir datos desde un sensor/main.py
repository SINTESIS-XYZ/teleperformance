import wifi
import usocket
import utime
from machine import Pin, ADC

# Configurar el pin analógico para la fotorresistencia
fotoresistencia_pin = 36
fotoresistencia = ADC(Pin(fotoresistencia_pin))
fotoresistencia.atten(ADC.ATTN_11DB)  # Rango completo: 3.3v

# Configuración del servidor UDP
pd_host = '192.168.2.2'
pd_port = 8888
wifi.wifi_connect()

print('Executing code')
print('Connected to {}:{}'.format(pd_host, pd_port))

while True:
    # Leer el valor de la fotorresistencia
    fotoresistencia_value = fotoresistencia.read()

    # Imprimir el valor en la consola
    print('Valor de la fotorresistencia:', fotoresistencia_value)

    # Esperar un breve período de tiempo antes de la próxima lectura
    utime.sleep_ms(1)
