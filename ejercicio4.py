import sys
import subprocess

def ping(ip,num):
    try:
        comando=["ping","-i","0.1","-c",str(num),ip]
        subprocess.run(comando)
    except Exception as e:
        print("Error: "+e)

if(len(sys.argv)<3):
    print('Error debes introducir dos argumentos: [direccion ip] [número de veces]')
else:
    ip=sys.argv[1]
    num=sys.argv[2]

    ping(ip,num)