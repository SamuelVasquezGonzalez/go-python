# ------- TIPOS DE DATOS COMPUESTOS ------------
# los datos compuestos son tipos de datos que estan compuestos por otros datos

# ----- LISTAS ----------
# Las listas o arrays es una variable que puede guardar multiples datos separados por comas, que estan compuestos por tipos de datos y un indice
# Las listas podemos redifinarlas cuanto queramos

# En este caso, tenemos 4 elementos, pero tenemos una longitud de 3 en su indice porque recordermos que en el mundo de la programacion. Se cuenta desde el numero 0

#  ELEMENTOS=   E = 1           E = 2   E = 3  E = 4
lista_uno = ['Samuel Vasquez', 'Lenwas', True, 1.65]
# INDICE=       i=0              i=1     i=2    i=3

print("---------- TODOS ESTOS DATOS LOS ESTOY LLAMANDO DESDE VARIABLES USANDO F-STRINGS -------------")
print(f" estos son mi datos desde una lista {lista_uno}")

# ------ Mostrar los datos de la lista -------
# Llamamos a la lista y dentro de corchetes, ponemos el indice que queremos observar, en este caso, el indice 0
print(f"este es mi nombre desde una lista: {lista_uno[0]}")
# para redifinir el valor de uno de los elementos del array simplemente llamamos a la posicion y la igualamos al nuevo valor
lista_uno[1] = "Lenwitas_bb" #<------ El indice 1 paso se ser "Lenwas" a "Lenwitas_bb"


# ------------- LAS TUPLAS -------------
# Las tuplas a diferencia de las lista, NO SE PUEDEN MODIFICAR O REDIFINIR, es como una constante, sus datos no cambian
# Si intentamos modificar una tupla, obtendremos un error
# Las tuplas de defines entre ()
tupla = ('Samuel Vasquez', 'Lenwas',True, 1.65)
print(f" este es mi nombre desde una tupla {tupla[0]}")

# ---------- CONJUNTO (SET) ----------
# Los conjuntos son otro tipo de array pero en este caso, los datos estan desordenados, pueden cambiar de indice, para usarlos debemos crearlos con una funcion que veremos mas adelante, este es solo un ejemplo de como se define

conjunto = {'Samuel Vasquez', 'Lenwas',True, 1.65}
# La diferencia con las tuplas y los array es que no se pueden modificar los elementos, si queremos cambiar algo, debemos redefinir todo el conjunto completo
# es importante aclarar que NO podemos acceder A LOS INDICES como lo hariamos con las tuplas o los array, si queremos mostrar el conjunto, debemos mostrarlo completo
# Tambien es importante aclarar que NO podemos REPETIR VALORES, no nos devolvera un error, simplemente, no aparecera el dato duplicado al igual que su indice
# conjunto[1] = "Samu" #<----- Esto nos dara error
conjunto = {'Samu', 'Lenwas',True, 1.65} #<------- Esto es lo que debemos hacer
print(f"Estos son mis datos desde un conjunto {conjunto}")
# Mas adelante veremos como usarlos y para que nos sirven
# se puede recorrer con un bucle


# ----------- DICCIONRIARO (DICT) -----------------
# Son basicamente un json. Obligatoriamente el nombre de la propiedad debe ir entre comillas
# la estrucuta es (key : value)
diccionario = {
    'nombre': 'Samuel Vasquez Gonzalez',
    'estatuta': 1.65,
    'Estado': "Feliz"
}
# Para mostrar alguna propiedad el objeto, ponemos llaves y dentro ponemos el nombre la propiedad
print(f"Este es mi nombre desde un diccionario: {diccionario['nombre']}")