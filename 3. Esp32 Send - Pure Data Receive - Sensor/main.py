# Importar módulos necesarios
import wifi  # Suponiendo que este es un módulo personalizado para Wi-Fi (no estándar en MicroPython)
import usocket
import utime
from machine import Pin, ADC

# Configurar el Resistor Dependiente de la Luz (LDR)
ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)  # Configurar atenuación para rango completo (3.3v)

# Configurar el host y puerto de Pure Data
pd_host = "127.0.0.1"
pd_port = 3333

# Conectar a Wi-Fi
wifi.wifi_connect()  # Suponiendo que esta es una función personalizada para la conexión Wi-Fi
print('Ejecutando código')

# Crear un socket UDP y conectar a Pure Data
pd = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
pd.connect((pd_host, pd_port))
print('Conectado a {}:{}'.format(pd_host, pd_port))

# Leer continuamente los valores de LDR, enviar a Pure Data e imprimir
while True:
    # Leer el valor de LDR
    valor_ldr = ldr.read()

    # Convertir el valor de LDR a bytes y enviar a Pure Data
    pd.send(valor_ldr.to_bytes(2, "big"))

    # Imprimir el valor de LDR
    print(valor_ldr)

    # Dormir durante 20 milisegundos
    utime.sleep_ms(20)
