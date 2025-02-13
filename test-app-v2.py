import os
import platform
import requests
import sys
import time

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


def hacer_ping(sitio):
    #param = '-n 1' if platform.system().lower() == 'windows' else '-c 1'
    
    #comando = f'ping {param} {sitio}'
    ##sistema = platform.system().lower()
    ##param = "-n 1" if "windows" in sistema else "-c 1"
    ##comando = f"ping {param} {sitio} > nul 2>&1" if "windows" in sistema else f"ping {param} {sitio} >/dev/null 2>&1"

    ##respuesta = os.system(comando)
    ###respuesta = os.system(f"ping -c 1 {sitio}")
    sistema = platform.system().lower()
    
    if "windows" in sistema:
        comando = f"ping -n 1 {sitio} > nul 2>&1"
        print ('Está en Windows...')
    else:
        comando = f"ping -c 1 {sitio} >/dev/null 2>&1"
        print ('Está en Linux u otro')

    respuesta = os.system(comando)
        
    if respuesta == 0:
        print(f'El sitio {sitio} está accesible.')
        msj_t=f'Acceso ÉXITOSO al sitio {sitio}  y el codigo es {respuesta}'
    else:
        print(f'No se pudo acceder al sitio {sitio}.')
        msj_t=f'Alerta: No se pudo acceder al sitio {sitio}  y el codigo es {respuesta}'
            
    enviar_mensaje_telegram(msj_t)
        
    #time.sleep(10)  # Espera 10 segundos antes de volver a hacer ping

if __name__ == '__main__':
    sitio = 'halzfac.net.pe'
    hacer_ping(sitio)



    
