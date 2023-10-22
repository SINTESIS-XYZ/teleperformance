import usocket
import _thread
from machine import PWM, Pin

def serverThread():
    # Configuración del motor
    pwm = PWM(Pin(12))
    pwm.duty(600)  # Configura el ciclo de trabajo del PWM para el motor
    addr = usocket.getaddrinfo('0.0.0.0', 5050)[0][-1]
    server = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
    server.bind(addr)
    print('Servidor listo para recibir')
    while True:
        # Recibe datos del cliente (Pure Data)
        data, direccion = server.recvfrom(2)
        print('De: {}: recibi:{}'.format(direccion, data))
        # Para mover el motor, convierte el valor recibido en un valor para el ciclo de trabajo
        # (Este código asume que el rango de valores es 0-1023)
        pwm.duty(data)

# Inicia el hilo del servidor para recibir datos y controlar el motor
_thread.start_new_thread(serverThread, ())
