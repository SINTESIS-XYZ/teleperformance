# Proyecto IoTMusic - Integración de Sensores, Actuadores, IoT y Música

Este proyecto utiliza MicroPython para integrar una fotoresistencia con la tecnología IoT (Internet de las cosas) y música. Los valores de la fotoresistencia se envían a través de UDP desde un ESP32 a un servidor, luego se utilizan para controlar parámetros sonoros en Pure Data y un motor en tiempo real.

## Descripción del Proyecto

En este proyecto, hemos desarrollado una solución que combina hardware y software para explorar la intersección entre la música y la tecnología. Utilizando un ESP32 con MicroPython, hemos conectado una fotoresistencia para medir la luz ambiente. Los valores obtenidos se transmiten de manera inalámbrica a un servidor a través de UDP.

El servidor, configurado en Pure Data, recibe estos datos y los utiliza para influir en parámetros sonoros. Además, Pure Data envía datos al ESP32 para controlar un motor en tiempo real. La fotoresistencia actúa como un sensor que interactúa con el entorno, permitiendo la creación de experiencias musicales y cinéticas únicas basadas en la intensidad de la luz.

## Componentes del Proyecto

- **ESP32 con MicroPython:** El ESP32 funciona como un dispositivo IoT que captura datos del entorno utilizando una fotoresistencia y los envía a un servidor.

- **Fotoresistencia:** Mide la luz ambiente y proporciona datos analógicos que reflejan las condiciones lumínicas.

- **UDP y Pure Data:** Se utiliza la comunicación UDP para transmitir datos desde el ESP32 a un servidor Pure Data y viceversa. Pure Data interpreta estos datos para modular parámetros sonoros y controlar un motor en tiempo real.

- **Motor Controlado por ESP32:** Se utiliza un motor controlado por el ESP32 para agregar una dimensión cinética al proyecto.

## Configuración del Proyecto

1. **Configuración del Hardware:**
   - Conecta la fotoresistencia y el motor al ESP32 según el esquema de conexión proporcionado.
   - Configura Pure Data para recibir y enviar datos según las especificaciones.

2. **Configuración del Software:**
   - Utiliza Visual Studio Code para abrir la carpeta del proyecto.
   - Configura el ESP32 con MicroPython y carga los scripts proporcionados.
   - Configura Pure Data en el servidor según las instrucciones proporcionadas.

3. **Visualización y Control:**
   - Utiliza Pure Data para visualizar y controlar la respuesta sonora en tiempo real basada en los datos de la fotoresistencia.
   - Configura Pure Data para enviar datos al ESP32 y controlar el motor en tiempo real.

## Estructura de la Carpeta

- **1. Configurar RED Wifi:** Contiene scripts para configurar la conexión Wi-Fi del ESP32.
- **2. Configurar Servidor UDP:** Scripts para configurar el servidor UDP en el ESP32.
- **3. Recivir Datos desde ESP32:** Contiene scripts y configuraciones para recibir datos desde ESP32 del sensor (forotresistencia) y enviarlos a Pure Data.
- **4. Enviar datos a ESP32:** Incluye el código de MicroPython para el ESP32 y las configuraciones en Pure Data para enviar datos al ESP32.

## Instrucciones de Uso

1. **Descarga del Proyecto:**
   - Descarga este repositorio en tu máquina local.

2. **Configuración del Hardware:**
   - Conecta la fotoresistencia y el motor al ESP32 según las instrucciones proporcionadas.

3. **Configuración del Software:**
   - Utiliza Visual Studio Code para abrir la carpeta del proyecto.
   - Configura el ESP32 con MicroPython y carga los scripts proporcionados.
   - Configura Pure Data en el servidor según las instrucciones proporcionadas.

4. **Ejecución del Proyecto:**
   - Ejecuta los scripts en MicroPython y Pure Data para iniciar la captura y procesamiento de datos.

5. **Exploración Musical, Cinética y Control del Motor:**
   - Mueve la fotoresistencia para experimentar con diferentes condiciones lumínicas y observa cómo afecta a la música y al motor.

## Requisitos del Proyecto

### Hardware

- **ESP32 con MicroPython:**
  - Descargar e instalar controladores USB para la placa ESP32.
  - Configurar Visual Studio Code con la extensión Pymakr para cargar scripts en el ESP32.

- **Sensores y Actuadores:**
  - Fotoresistencia: Conectar al pin analógico del ESP32 (por ejemplo, pin 32).
  - Motor: Conectar al pin PWM del ESP32 (por ejemplo, pin 12).

### Software

- **Visual Studio Code:**
  - Instalar Visual Studio Code como entorno de desarrollo.
  - Instalar la extensión Pymakr para la programación del ESP32.

- **MicroPython:**
  - Configurar MicroPython en el ESP32.
  - Cargar scripts en el ESP32 utilizando Visual Studio Code y Pymakr.

- **Pure Data:**
  - Descargar e instalar Pure Data en el servidor.
  - Configurar Pure Data para recibir y enviar datos a través de UDP.

### Conexión a Internet


Este proyecto proporciona una plataforma para la exploración creativa de la intersección entre la tecnología IoT y la música. ¡Disfruta experimentando y creando tus propias experiencias musicales, cinéticas y sensoriales!


---

## 1. Configuración de Placa ESP32

Para comenzar a trabajar con la placa ESP32 y este proyecto, sigue estos pasos para configurar los controladores:

1. **Descargar el Controlador:**
   - Visita el sitio web del fabricante de tu placa ESP32 y busca la sección de descargas o soporte. Puedes encontrar controladores USB en el [sitio oficial de Espressif](https://www.espressif.com/en/support/download/all) si estás utilizando un módulo de Espressif.

2. **Instalar el Controlador:**
   - Descarga el controlador adecuado para tu sistema operativo (Windows, macOS, o Linux).
   - Sigue las instrucciones de instalación proporcionadas por el fabricante.

3. **Conectar la Placa ESP32:**
   - Conecta la placa ESP32 a tu computadora mediante un cable USB.

4. **Verificar la Conexión:**
   - Abre el Administrador de Dispositivos en Windows o utiliza comandos como `ls /dev` en Linux/macOS para verificar si la placa ESP32 aparece correctamente.

5. **Configuración en Visual Studio Code con Pymakr:**
   - Asegúrate de tener la extensión Pymakr instalada en Visual Studio Code.
   - Abre tu proyecto y selecciona el puerto COM correcto para tu ESP32 en la configuración de Pymakr.

6. **Reiniciar Visual Studio Code:**
   - Reinicia Visual Studio Code después de configurar los controladores y el puerto COM.

Para una guía visual detallada sobre cómo configurar tu placa ESP32 y Visual Studio Code con la extensión Pymakr, puedes consultar el siguiente video tutorial:

[![Configuración de Placa ESP32 con Pymakr](https://img.youtube.com/vi/YOeV14SESls/0.jpg)](https://www.youtube.com/watch?v=YOeV14SESls&t=186s)

Asegúrate de seguir los pasos y ajustar la configuración según las necesidades de tu proyecto. Si tienes alguna pregunta específica después de ver el video o necesitas más ayuda, no dudes en preguntar en nuestro [foro de soporte](#enlace-al-foro) o [comunidad en línea](#enlace-a-comunidad).

## 2.Configuración de la Red WiFi

Antes de ejecutar el script en tu dispositivo ESP32, asegúrate de configurar correctamente la conexión WiFi. Sigue estos pasos:

1. Descarga la carpeta 1. Configurar RED Wifi, carga los scripts en un proyecto de Visual Studio.

2. Busca la sección de **Configuración de WiFi** en el código. Debería verse algo así:

    ```python
    # Configuración de WiFi
      SSID = 'WRITE YOUR NAME NETWORK HERE'
      PASS = 'WRITE YOUR PASSWORD NETWORK HERE'
      CONNECTING_TRIES = 3
    ```

    Reemplaza `'SSID'` y `'PASS'` con los detalles de tu red WiFi.

3. Guarda los cambios en el archivo.

4. Presiona el botón de carga (Upload) en Pymakr para cargar el script en tu dispositivo.

5. Realiza un reinicio del dispositivo (hard reset) para ejecutar el script. Puedes hacer esto a través de los botones proporcionados por Pymakr o según las instrucciones específicas de tu placa.
   
Si encuentras problemas de conexión, asegúrate de que los detalles de la red WiFi sean correctos y de que la placa ESP32 está en un rango de señal adecuado.

En consola te parecer un mensaje como el siguiente

```python
Uploading and running the script...
Upload and run complete!
Connecting to "YOUR NETWORK"
Connection Successfully to "YOUR NETWORK"
Executing code
Connected to 192.168.2.2:8888
MicroPython v1.21.0 on 2023-10-05; Generic ESP32 module with ESP32
```

### Sugerencia:
Si no conoces tu IP, realiza el siguiente procedimiento:

## 3. Configuración del Servidor UDP

Antes de ejecutar el script, puedes obtener dinámicamente la dirección IP del servidor UDP utilizando el comando `ipconfig` en la terminal de Windows. Sigue estos pasos:

1. **Abre la terminal de Windows:**
   - Busca "cmd" o "Símbolo del sistema" en el menú de inicio y ábrelo.

2. **Ejecuta el comando `ipconfig` para obtener información sobre las interfaces de red:**
   - Utiliza el siguiente comando:

   ```plaintext
   > ipconfig

Busca la sección correspondiente a tu interfaz de red activa, generalmente "Adaptador de Ethernet" o "Adaptador de Wi-Fi". Allí encontrarás tu "Dirección IPv4". Anota esta dirección IP.

Adaptador de Ethernet:
...
   ```plaintext
   Dirección IPv4. . . . . . . . . . . . . . : xxx.xxx.xxx.xxx
   ```
Configura el servidor UDP con la dirección IP anotada:

En tu script, utiliza la dirección IP que has anotado para la conexión al servidor UDP.
```plaintext
pd_host = 'xxx.xxx.xxx.xxx'  # Utiliza la dirección IP anotada
pd_port = 8888
pd.connect((pd_host, pd_port))
```
### 4. Recibir Datos de un Sensor desde ESP32 y enviarlos a Pure Data.

En este paso, configuraremos la placa ESP32 para leer datos de un sensor de fotorresistencia. Sigue estos pasos:

1. **Configura el Sensor:**
   - Conecta el sensor de fotorresistencia al pin analógico 36 de la placa ESP32.

**ESP32 Pinout:**
![Logo de Mi Proyecto](https://github.com/EddieBorbon/IoTMusic/blob/main/Images/ESP32-Pinout.jpg)

**Ejemplo del circuito**

![Logo de Mi Proyecto](https://github.com/EddieBorbon/IoTMusic/blob/main/Images/esp32-ldr-wiring.jpg)

Ahora tu placa ESP32 estará configurada para recibir datos de un sensor y enviarlos al servidor.
2. **Actualizar el Código en ESP32:**
   - Descarga la carpeta `3. Enviar Datos a Pure Data` y carga los scripts en tu proyecto de Visual Studio Code.

3. **Configuración de Pure Data:**
   - Abre tu patch de Pure Data y configura los objetos necesarios para recibir datos UDP. Por ejemplo:

   ```pd
   [udpreceive 8888]
   |
   [unpack s]
   |
   [print]

4. **Configuración del Código en ESP32:**

Abre el script en tu proyecto relacionado con el envío de datos (sendData.py, por ejemplo).

Busca la sección que configura el servidor UDP:
   ```python
   pd_host = 'xxx.xxx.xxx.xxx'  # Utiliza la dirección IP anotada
   pd_port = 8888
   pd.connect((pd_host, pd_port))
   ```
Asegúrate de que pd_host sea la dirección IP correcta de tu computadora con Pure Data y el puerto sea el mismo que configuraste en Pure Data.

5. **Enviar Datos desde ESP32:**
Añade el siguiente código al bucle principal para leer datos del sensor y enviarlos a Pure Data:
   ```python
   while True:
       ldr_value = ldr.read()
       pd.send(ldr_value.to_bytes(2, 'big'))
       utime.sleep_ms(20)
   ```
Este código lee el valor del sensor (fotorresistencia) y lo envía a Pure Data como bytes a través de UDP. Puedes adaptar este código según tus necesidades y el tipo de datos que estás enviando.

**Verificar Resultados:**

   - Ejecuta el script en tu ESP32 y observa la consola para asegurarte de que no haya errores.
   - Observa la consola de Pure Data para verificar que está recibiendo los datos correctamente.

**Sugerencia:**

   - Si encuentras problemas de conexión, verifica que las direcciones IP y los puertos coincidan entre la ESP32 y Pure Data. Puedes utilizar las herramientas de depuración en ambas plataformas para identificar cualquier problema potencial.

Con estos pasos, tu ESP32 debería estar enviando datos a Pure Data. Puedes ajustar el código según tus necesidades y experimentar con diferentes tipos de datos y configuraciones en Pure Data.

Este proyecto proporciona una base para explorar la integración de sensores y actuadores con tecnologías IoT y música utilizando MicroPython y Pure Data. ¡Diviértete explorando y creando!

## 5. Pure Data to ESP32

En esta sección, te guiaremos a través de la configuración de Pure Data para enviar datos a tu ESP32 y controlar un motor.

1. **Descarga de la Carpeta:**
   - Descarga la carpeta "4. Pure data to ESP32".
   - Abre la carpeta "4. Pure data to ESP32" desde Visual Studio Code.

2. **Configuración en Pure Data**
Abre Pure Data y sigue estos pasos:
   - Crea un objeto `[udpsend 192.168.1.115 5050]` para enviar datos a la dirección IP de tu ESP32 y al puerto configurado en tu script (`5050` en este caso).
   - Puedes utilizar diferentes objetos para generar datos. Por ejemplo, un objeto `[hslider]` puede generar valores que enviarás a tu ESP32. Conecta el `[hslider]` al `[udpsend]` para enviar los valores.
   - Si deseas visualizar los datos que estás enviando, puedes crear un objeto `[print]` y conectarlo al `[udpsend]`.

3. **Ejecución y Verificación**
Ejecuta tu script en Pure Data.
Mueve el slider (o genera datos de la manera que hayas configurado) para enviar valores a tu ESP32.
Observa la consola de Pure Data para verificar que los datos se estén enviando correctamente.

Con estos pasos, habrás configurado Pure Data para enviar datos a tu ESP32 y controlar el motor.

Sugerencia:
Si encuentras problemas de conexión, verifica que las direcciones IP y los puertos coincidan entre Pure Data y la ESP32. Puedes utilizar las herramientas de depuración en ambas plataformas para identificar cualquier problema potencial.

## Contribución

Si deseas contribuir a este proyecto en IoTMusic:
- Realiza un fork del repositorio.
- Crea una rama para tu nueva característica o corrección de errores.
- Envía una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia [nombre de la licencia].

## Contacto

Para preguntas o comentarios, contáctame en [tu dirección de correo electrónico] o [tus redes sociales].
