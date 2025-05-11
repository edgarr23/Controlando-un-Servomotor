from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(5), freq = 50)

def Angulo(grados):
    dutie = int((grados / 180) * (115 - 35) + 35)
    return servo.duty(dutie)

r = 1
x = 1
while(True):
    r = int(input("\n            Juega con el Servo!\n\n  Que quieres hacer?:\n\n[1] Giro Automatico\n[2] Movimiento Manual\n[3]Salir\n >>"))
    if r == 1:
        q = int(input('De A cuanto quieres que se mueva? >'))
        w = float(input('Tiempo entre movimiento? >'))
        x = int(input('Cuantas veces quieres que lo haga? > '))
        while x != 0:
            for i in range(1, 230, q):
                Angulo(i)
                sleep(w)
            x = x - 1
        Angulo(0)
    if r == 2:
        x = 1
        while x > 0:
            x = int(input("Dame el Grado de rotacion. >>"))
            Angulo(x)
    if r == 3:
        print("Espero te haya gustado, bye!")
        break
    else:
        print("No has indicado cual interaccion hacer correctamente, Porfavor Vuelva a Elegir.\n{} Esta fue tu respuesta".format(r))
