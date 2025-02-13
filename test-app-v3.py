import socket
import requests

def enviar_mensaje_telegram(mensaje):
    TOKEN = '7070294206:AAHnrinmuF_VxebhaiCQmq9zT3TfiKEJWlc'
    CHAT_ID = '1154774418'
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': mensaje}

    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()  # Lanza un error si la respuesta no es 200
        print('Mensaje enviado a Telegram con éxito.')
    except requests.exceptions.RequestException as e:
        print(f'Error al enviar mensaje a Telegram: {e}')

def verificar_conexion(sitio, puerto=80):
    try:
        socket.create_connection((sitio, puerto), timeout=5)
        print(f"✅ El sitio {sitio} está accesible en el puerto {puerto}.")
        enviar_mensaje_telegram(f"✅ Acceso exitoso al sitio {sitio} en el puerto {puerto}.")
    except (socket.timeout, socket.error):
        print(f"❌ No se pudo acceder al sitio {sitio}.")
        enviar_mensaje_telegram(f"⚠️❌ Alerta: No se pudo acceder al sitio {sitio}.")

"""
def hacer_ping(sitio):
    ##sistema = platform.system().lower()
    ##param = "-n 1" if "windows" in sistema else "-c 1"
    #param = '-n 1' if platform.system().lower() == 'windows' else '-c 1'
    
    #comando = f'ping {param} {sitio}'
    ##comando = f"ping {param} {sitio}"
    ##respuesta = os.system(comando) / 256 
    
    ###respuesta = os.system(f"ping -c 1 {sitio}")
    sistema = platform.system().lower()
    
    if "windows" in sistema:
        comando = f"ping -n 1 {sitio} > nul 2>&1"
        print (f'Ejecutado en Wind...{sistema}')
    else:
        comando = f"ping -c 1 {sitio} >/dev/null 2>&1"
        print (f'Ejecutado en Linux u otra......{sistema}')

    respuesta = os.system(comando)
     
    if respuesta == 0:
        print(f'El sitio {sitio} está accesible. Y el codigo es {respuesta}')
        msj_t=f'Acceso ÉXITOSO al sitio {sitio}  y el codigo es {respuesta}'
    else:
        print(f'No se pudo acceder al sitio {sitio}. Y el codigo es {respuesta}')
        msj_t=f'Alerta: No se pudo acceder al sitio {sitio} y el codigo es {respuesta}'
            
    enviar_mensaje_telegram(msj_t)
        
    #time.sleep(10)  # Espera 10 segundos antes de volver a hacer ping

"""   
if __name__ == '__main__':
    sitio = 'halzfac.net.pe'
    #hacer_ping(sitio)
    verificar_conexion(sitio)


    