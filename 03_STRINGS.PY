### File creado por: YugaScript ###

### STRING ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string = "Mi string"))
print(len (my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_line_string = "\tEste es un Stringcon tabulacion"
print(my_tab_line_string)

my_scape_line_string = "\tEste es un String \n escapado"
print(my_scape_line_string)

### Formateo ###

name, surname, age = "Yuga", "script" , 20

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + "y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")