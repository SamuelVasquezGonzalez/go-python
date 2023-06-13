#----------------------- VARIABLES EN PYTHON -------------------
#Entendamos como se declarara las variables en python y como debemos usarlas

#Las variables son espacios que usamos en la memoria de nuestro programa y que podemos utilizar en nuestro codigo
#Recordemos que las variables se declarar con un nombre y de define con un valor. Ej:

        # nombre = "Samuel"
        #  ↑           ↑
      #Declaracion   Definicion 
      
a = 1
b = 2
c = a + b

# ----- Lo IDEAL SERIA UTILIZAR Snake_Case EN NUESTRAS VARIABLES -----
variables_snake_case = "snake case variable"

nombre = "Samuel"
print(c) #print() Nos permite mostrar algo por la consola. Podemos imprimir cualquier cosa (Variables, strings, booleans, numbers, Y resultados de operaciones)
print(nombre)


# ------------- REDEFINICION DE VARIABLES ----------------

#En python podemos Redefinir el valor de las variables e imprimrlos. Pero si creamos variables con el mismo nombre de declaracion, siemore se imprimira la ultima en ser declarada. Ej:

apellido = "Vasquez" #<---- Aqui la declaramos por primera vez
apellido = "Gonzalez"  # --| 
apellido = "Fuentes"   #   ↪ Luego las siguentes. Seria estar redefiniendo la variable
print(apellido)

#Podemos usar el += igual que en javascript para tomar el valor principal y luego sumarle o concatenarle el nuevo valor, algo asi:

nombreCompleto = "Samuel"
nombreCompleto += " Vasquez"
nombreCompleto += " Gonzalez"
print(nombreCompleto)

#Tambien podemos usar el -= pero este solo funcionara en numeros
numeroFinal = 10
numeroFinal -= 5
print(numeroFinal)


# -----------  CONCATENACION EN PYTHON -------------------
#Concatenar con el "+" no es lo mas optimo ademas no nos permitiria concatenar numeros, lo ideal seria utilizar los fStrings. Solo debemos poner una f al inicio del string y colocar el nombre de la variable dentro de llaves. Lo que hace el fString es tomar todos los valores que se usaran y convertirlos en un string

# ---------- CONCATENAR CON Fstrings ----------------------
nombreMio = "Samuel"
edad = 17
bienvenida = f"Hola {nombre} ¿Como estas?, tu edad es {edad}, verdad?"
print(bienvenida)

#Hay una forma de eliminar un dato por ejemplo una variable con una palabra reservada llamada "del nombreDeLaVariable"
variablePrueba = "Samuel"
mensaje = f"Hola, {variablePrueba}"
del variablePrueba #<--- pensariamos que deberia dar algun error, pero lo que pasa es que primero declaramos mensaje con el valor de variablePrueba y luego la eliminamos y mostramos el mensaje, si eliminamos mensaje en vez de variablePrueba ahi si nos daria error porque primero la declaramos, luego la eliminamos y luego estariamos imprimiendo una variable que no existe
print(mensaje)


# ------------- OPERADOR DE PERTENENCIA (in / not in) -----------------

# Hay una forma de buscar caracteres en python, una forma es utiliza el "in" o el "not in" en el print. Lo que hace esto es devolvernos un boolean. Ejemplo:
# Para que esto funcione, el dato que queremos buscar debe ser identico en cuando a tipo de dato y mayusculas y minusculas, de lo contrario, obtendremos false

# Este operador se llama operador de pertenecina osea, quiere verificar si pertenece o no pertenecer (in / not in)
buscarPalabra = "Seek And Destroy"
print("Seek" in buscarPalabra)
print("Seek" not in buscarPalabra)