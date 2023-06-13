# ------------ suma y resta ( + y -) -----------


suma = 12 + 5
resta = 12 - 5



# ----------- Multiplicacion y division (* - /) -----------



multiplicacion = 12 * 5
division = 12 / 5 #<---------- estos siempre nos va a devolver un numero flotante (decimal) nunca devolvera un entero



# ------- Potenciacion -------- (**)
exponente = 12**5 #<------ pontenciacion 12 de exponente 5 (12*12*12*12*12)


# ------ Division Baja (//)
division_baja = 12//5 #<------ Lo que hace la division baja es devolvernos un entero redondeado hacia abajo, es lo mismo que la division normal solo que este nos devurlve un entero


# -------- Resto o Modulo (%) -------
modulo = 12 % 5 #<--- esto nos devuelve el residuo. osea, lo que sobro para llegar al numero. en este caso 5 solo cabe 2 veces en al divison, lo que falto para llegar a 12 fue 2, ese dos es el residuo

# type(dato) nos devuelve que tipo de dato es
tipo_de_dato = type("dato")
print(tipo_de_dato)
print(f"esta es una suma: {suma}")
print(f"esta es una resta: {resta}")
print(f"esta es una multi: {multiplicacion}")
print(f"esta es una division: {division}")
print(f"este es un exponente reuelto: {exponente}")
print(f"esta es una division baja: {division_baja}")
print(f"este es un modulu: {modulo}")