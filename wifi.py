import network

def iniciar_ap(ssid="ServoControl", pas="servocontrol"):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=pas)
    while not ap.active():
        pass
    ip = ap.ifconfig()[0]
    print("Red WiFi creada")
    print("Conéctate a:", ssid)
    print("Entra a: http://{}/".format(ip))
    return ip
