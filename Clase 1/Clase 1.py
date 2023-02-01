#1. Numeros
# 1.1 Enteros
print(type(2))
# 1.2 Decimales
print(type(1.322))
# 1.3 Complejos
print(type(2 +4j))
c= 3-7j
print(type(c))
print(c.real)
print(c.imag)
#print(982145888888L) ya no existen los long a partir de python 3.0
# 2. Operaciones numericas
# 2.1 Suma
print(2.5+2.1)
# 2.2 Resta
print(4-3.5)
# 2.3 Multiplicacion
print(5*4)
# 2.4 Potencia
print(2**3)
# 2.5 Division
print(5/6)
# 2.6 division (resto)
print(4%3) 
# 2.7 Floor division (division parte entera)
print(5//2) 
# 3. Precedencia de operaciones
'''
1. Parentesis
2. Exponenciacion
3. * y /, //, %
4. + y -
'''
print((4**2 +3*4 +2)*(2*1+3))
# 4. Cadenas de texto
print("Hola")
print("Po aqui!")
print("742 San Juan")
print("1234")
print("'Que tan largo es este string?'")
print("'Ohh!' ")
print(type("'Ohh!' "))
print("Otro \"texto\" entre comilas")
print("Otro \'texto\' entre comilas")
print('''Hola mundo este soy soy
este es un texto largo''')
# 5. Print
print('Una cadena \t con tabulacion')
print('Una cadena \n con nueva linea')
print('C:Users/Windows/David')
print(r'C:David/Users/Windows')
print("""Esta es una cadena 
en formato long""")
a = "1"
print(type(a))
print(1+2)
print("David_"," _Juan") # Concatenation de Strings
a = "pic123"
b = "21344"
print (a.isnumeric()) # Fijense que el print no esta pegado al parentesis 
print (b.isnumeric()) # Con la funcion is.numeric puedo verificar si es numero 
print("Hola %s, has obtenido un score de %i del total de %f" % ("David", 3, 100))
print("Hola %s, has obtenido un score de %f del total de %f" % ("Juan", 2.15, 2.5))
# 6. Variables
a=2
print(a)
print(type(a))
b= True
print(type(b))
c_123= "David F BU"
print(type(c_123))
d_Juan_Perez= 'Este es un escenario X'
print(type(d_Juan_Perez))
nombre='David'
Nombre='Juan'
nomBre='Andrea'
print(nombre, Nombre, nomBre) # Distincion de mayusculas
# 7. Input
nombre_x= input('Hola como te llamas?: ')
edad= int(input('Que edad tienes?: '))
print(type(edad))
# 8. Operaciones aritmeticas
a=2;b=3.1
print(a+b)
print(a*b)
print(a/b)
print(a**b)
cadena='David'
print(cadena*2)
print(cadena+cadena)
# 9. Indexacion de strings
planet = "Jupiter"
print(planet[-1])   # Indice reverso
print(planet[2])
print(planet[0])
# 10. Longitud de strings
a= 'Hola este es el mundo'
print(len(a))
b='David !'
print(len(b))
# 11. Slicing
planet = "Jupiter"
print(planet[2:5])   # va desde 0: n-1 indice comienza en 0
print(planet[:-1])
print(planet[-1:])
print(planet[1:3])
#12. Inmutabilidad y reasignacion de strings
cad='Pithon'
cad[0:1]+'y'+cad[2:]

############################################################3
# Desafio nota final
nota_1= float(input('Ingresa nota 1: '))
nota_2= float(input('Ingresa nota 2: '))
promedio= nota_1*0.4 + nota_2*0.6
print('Tu nota final es:', promedio)
# Desafio String
cadena_1='moderno'
cadena_2='Python'
cadena_3='es un lenguaje'
cadena_4='de programación'
print(cadena_2+' '+ cadena_3 +' '+cadena_4 +' '+ cadena_1)
# Desafio Slicing
cadena='divaD 6.4 sacitametaM'
print(cadena[::-1])
nombre= cadena[::-1][-5:]
nota= cadena[::-1][-9:-6]
materia=cadena[::-1][0:11]
print('El nombre es: ',nombre, ' ha sacado una nota ', nota, 'en ', materia)