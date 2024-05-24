import sys
import threading
from pythonosc import dispatcher, osc_server
import logging

# Configuración del logging
logging.basicConfig(level=logging.DEBUG)

# Importar obswebsocket
sys.path.append('../')
from obswebsocket import obsws, requests  # noqa: E402

# Configuración de la conexión con OBS
host = "127.0.0.1"
port = 4455
password = "mafufi"

ws = obsws(host, port, password)
ws.connect()

# Función para manejar los mensajes OSC
def manejar_mensaje(address, *args):
    print(f"Mensaje recibido en {address}: {args}")
    if address == "/streaming":
        if args[0] == 1:
            print('Inicia transmisión')
            ws.call(requests.StartStream())
        elif args[0] == 0:
            print('Detén la transmisión')
            ws.call(requests.StopStream())

# Crea un despachador de mensajes OSC
dispatcher = dispatcher.Dispatcher()

# Mapea las direcciones OSC a la función de manejo
direcciones_osc = ["/streaming", "/ch1", "/ch2", "/ch3"]
for direccion in direcciones_osc:
    dispatcher.map(direccion, manejar_mensaje)

# Configura y corre el servidor OSC en un hilo separado
ip_escucha = "0.0.0.0"  # Escucha en todas las interfaces de red
puerto_escucha = 9500   # Puerto en el que escucha el servidor

servidor = osc_server.ThreadingOSCUDPServer((ip_escucha, puerto_escucha), dispatcher)
print(f"Escuchando en {ip_escucha}:{puerto_escucha}")

# Inicia el servidor en un hilo separado
servidor_thread = threading.Thread(target=servidor.serve_forever)
servidor_thread.start()




'''

try:

        #print("Switching to {}".format(name))
        #print(ws.call(requests.GetStreamStatus()))
    print("Obtiene status antes de iniciar la transmisión")
        #print(ws.call(requests.GetStreamStatus()))
    time.sleep(5)
    print("se comienza la transmisión")
        #ws.call(requests.StartStream())
        #print(ws.call(requests.StartStream()))
        #print(ws.call(requests.GetStreamStatus()))

        #print(ws.call(requests.StopStream()))
        #ws.call(requests.SetCurrentProgramScene(sceneName=name))
    time.sleep(2)
    ws.call(requests.GetStreamStatus())
        #print(ws.call(requests.GetStreamStatus()))
    #print("End of list")

except KeyboardInterrupt:
    pass

ws.disconnect()
'''