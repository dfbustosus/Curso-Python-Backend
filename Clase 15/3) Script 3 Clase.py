import sys
# Comprobación de seguridad, ejecutar sólo si se reciben 3 argumentos reales
if len(sys.argv) == 3: # ojo aqui el primer valor es el nombre del scrip
    texto = sys.argv[1] # segundo elemento un texto
    repeticiones = int(sys.argv[2]) 
    for r in range(repeticiones):
        print(texto)
else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo: escribir_lineas.py "Texto" 5')
# python '3) Script 3 Clase.py' "Cadena" 2  [1,2,3,4]
# python '3) Script 3 Clase.py' "Cadena" 2
# python '3) Script 3 Clase.py' "Hola" 2 