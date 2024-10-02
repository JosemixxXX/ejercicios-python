import sys

chars1 = "┌┐┘└│─"
chars2 = "╔╗╝╚║═"

if(len(sys.argv)<4):
    print('Error!! Debes introducir tres argumentos posicionales. El primero debe ser el ancho de caja, el segundo el alto de caja y el tercero debe ser unas de las palabras reservadas simple o doble para el tipo de linea. Si introduces un carácter en la última opción se utilizará en lugar de la línea para dibujar el contenedor.\n')
    print("Ejemplo >>> Si introduces los datos 5 6 simple debe mostrar algo así:\n")
    top = chars1[0] + chars1[5]*(5-2) + chars1[1]
    mid= chars1[4] + " "*(5-2) + chars1[4]
    bottom=chars1[3] + chars1[5]*(5-2) + chars1[2]


    print(top)

    for lineas in range(0,6):
        print(mid)
        
    print(bottom)

else:
    ancho=sys.argv[1]
    alto=sys.argv[2]
    tipo=sys.argv[3]

    try:
        ancho=int(ancho)
        alto=int(alto)
        if(tipo.lower() == 'simple'):
            top = chars1[0] + chars1[5]*(ancho-2) + chars1[1]
            mid= chars1[4] + " "*(ancho-2) + chars1[4]
            bottom=chars1[3] + chars1[5]*(ancho-2) + chars1[2]


            print(top)

            for lineas in range(0,alto):
                print(mid)
                
            print(bottom)


        elif(tipo.lower() == 'doble'):
            top = chars2[0] + chars2[5]*(ancho-2) + chars2[1]
            mid= chars2[4] + " "*(ancho-2) + chars2[4]
            bottom=chars2[3] + chars2[5]*(ancho-2) + chars2[2]


            print(top)

            for lineas in range(0,alto):
                print(mid)
                
            print(bottom)

        elif(len(tipo)==1):
            top = tipo + tipo*(ancho-2) + tipo
            mid= tipo + " "*(ancho-2) + tipo
            bottom=tipo + tipo*(ancho-2) + tipo


            print(top)

            for lineas in range(0,alto):
                print(mid)
                
            print(bottom)

        else:
            print("Error!! El dato introducido en el tercer parámetro es incorrecto.")
            
    except ValueError:
        print("Error!! Los dos primeros argumentos deben ser números enteros")

    