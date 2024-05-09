### Operadores ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(3 ** 4)
print(2 ** 3 + 3 -7 / 1 // 4) # Como se puede comprobar, aqui si se puede mezclar cada signo ya que cada uno realiza una operacion, para que esto se pueda entender veamos las siguientes lineas.

# Ahora vamos a operar con cadenas de caracteres

print("Hola " - "python") # De esta manera se puede comprobar que no se puede operar, pero si se puede con un signo '+' vamos a comprobarlo.
print("Hola " + "python") # Como puedes comprobar ahora si se puede, porque estas sumando dos cadenas de caracteres, de esta forma se vera asi: 'Hola python'

# Ahora vamos a operar mezclando con cadenas de caracteres y numeros enteros

print("Hola " + 5) # UYYY!! Que ha pasado aqui?, pues como puedes comprobar no se puede trabajar con tipos diferente ya que no se puede trabajar con enteros y string. Veamos la forma correcta.
print("Hola " + str(5)) # Para poder sumar una string con un numero entero debemos de pasar un numero a tipo string con str(), de esta forma no te dara ningun error como en la linea anterior...

print("Hola " * 5) # Como se puede comprobar al multiplicar esta string con el numero entero nos duplica x 5 veces la string "Hola". Tambien se puede de esta forma
print("Hola " * (2 ** 3)) # Aqui hace primero la multiplicacion que esta entre parentesis osea (2 ** 3) y luego su resultado lo multiplica con la string "Hola"

