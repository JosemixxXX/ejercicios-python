import sys

input=sys.argv[1]

def esArn(texto):
    letras_permitidas = {'A','U','G','C'}

    return set(texto.upper()) <= letras_permitidas

if(esArn(input)):
    salida=input.upper().replace('A','T').replace('U','A').replace('C','X').replace('G','C').replace('X','G')
    print(salida)

else:
    print('El formato introducido no es válido')


