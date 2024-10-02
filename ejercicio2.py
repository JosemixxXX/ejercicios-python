import sys

def convertir(input):
    conversion={
        'o':'0',
        'O':'0',
        'i':'1',
        'I':'1',
        'e':'3',
        'E':'3',
        'a':'4',
        'A':'4',
        's':'5',
        'S':'5',
        'g':'6',
        'G':'6',
        't':'7',
        'T':'7',
        'b':'8',
        'B':'8',
        'g':'9',
        'G':'9',
        'c':'[',
        'C':'[',
        'v':'^',
        'V':'^'
    }

    salida=[]
    for c in input:
        salida.append(conversion.get(c,c))

    return ''.join(salida)

input=' '.join(sys.argv[1:])
print(convertir(input))
