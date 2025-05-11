import socket
from machine import Pin, PWM
from time import sleep
from wifi import iniciar_ap
from html import get_html

# --- Inicializar servo ---
servo = PWM(Pin(5), freq=50)

def mover_angulo(grados):
    duty = int((grados / 180) * (115 - 35) + 35)
    servo.duty(duty)

# --- Iniciar red Wi-Fi y obtener IP ---
ip = iniciar_ap()
html = get_html(ip)

# --- Iniciar servidor web ---
s = socket.socket()
s.bind(('', 80))
s.listen(1)
print("🌐 Servidor web listo en http://{}/".format(ip))

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    print("📩 Petición:", request)

    if "/servo?g=" in request:
        try:
            grado = int(request.split("/servo?g=")[1].split()[0])
            mover_angulo(grado)
        except:
            pass

    conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
    for linea in html.split('\n'):
        conn.send(linea + '\n')

    conn.close()
