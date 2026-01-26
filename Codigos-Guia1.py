import numpy as np
import matplotlib.pyplot as plt #libreria para graficar

"""
#Ejercicio 3 de la Guia 1
1 + 3
a = 7
b = a + 1

print( "b = " , b )

# Vectores
v = np.array([ 1 , 2 , 3 , -1] )
w = np.array( [ 2 , 3 , 0 , 5 ] )

print ( "v + w = " , v + w)
print ( "2*v = " , 2*v )
print ( "v**2 = " , v **2 )

# Matrices (ejecutarlos comandos uno a uno para ver los resultados )
A = np.array( [ [ 1 , 2 , 3 , 4 , 5 ] , [ 0 , 1 , 2 , 3 , 4 ] , [ 2 , 3 , 4 , 5 , 6 ] , [ 0 , 0 , 1 , 2 , 3 ] , [ 0 , 0 , 0 , 0 , 1 ] ] )

print(A)

A[ 0 : 2 , 3 : 5 ] #Filas 0 y 1 (de la 0 a la 2, sin incluir la 2) y Columnas 3 y 4 (de la 3 a la 5, sin incluir la 5). Resultado: una submatriz 2×2
A[ : 2 , 3 : ] #Filas: desde el inicio hasta la 2 (sin incluirla), es decir filas 0 y 1. Columnas: desde la 3 hasta el final. Resultado: submatriz 2×2
A[ [ 0 , 2 , 4 ] , : ]
ind = np.array( [ 0 , 2 , 4 ] ) # Crea un array con los índices 0, 2, 4
A[ ind , ind ] # Elementos A[0,0], A[2,2], A[4,4]
A[ ind , ind[ : , None ] ]

# Numeros complejos
1j * 1j
(1+2j) * 1j
"""

#Ejercicio 4 de la Guia 1
#Encontrar los coeficientes de la parábola y = ax2 + bx + c que pasa por los puntos
#(1, 1), (2, 2) y (3, 0). Verificar el resultado obtenido usando Python. Graficar los puntos y la parábola
#aprovechando el siguiente código
# Aca, crear la matriz y resolver el sistema para calcular a , b y c.

def parabola_coefficients(x_points, y_points):
    A = np.array([x_points**2, x_points, np.ones(len(x_points))]).T #creo la matriz A de la forma x^2 , x , 1 3x3 
    coeffs = np.linalg.solve(A, y_points) #resuelvo el sistema de ecuaciones A * coeffs = y_points
    print(A)
    return coeffs

xx = np.array( [ 1 , 2 , 3 ] )
yy = np.array ( [ 1 , 2 , 0 ] )

print(parabola_coefficients(xx,yy))



a, b, c = parabola_coefficients(xx, yy)
x = np.linspace ( 0 , 4 , 100 ) #genera 100 puntos equiespaciados entre 0 y 4.
f = lambda t : a* t **2+b* t+c #esto genera una funcion f de t.
plt.plot (xx , yy , '*')
plt.plot (x , f(x))
plt.show ()

