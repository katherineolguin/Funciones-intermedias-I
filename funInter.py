# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
# En el directorio_deportes, cambia "Messi" por "Andrés".
# Cambia el valor 20 en z a 30.

#EJERCICIO 1
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] =15                                  #1
print(x)

estudiantes[0]['last_name'] = 'Bryant'       #2
print(estudiantes)

directorio_deportes['fútbol'][0] = 'Andres'  #3
print(directorio_deportes)

z[0]['y'] = 30                                #4
print(z)



# # EJERCICIO 2


estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    #opcion1
def iterateDictionary(lissta):
    valor =''
    for dato in lissta:

        valor += f"first_name - {dato['first_name']}, last_name - {dato['last_name']}\n"
    return valor

print(iterateDictionary(estudiantes))

#Opcion2

def iterateDictionary(lista):

   for x in lista:
      print(f"first_name  - {x['first_name']}, last_ name -  {x['last_name']} \n ") 

iterateDictionary(estudiantes)


# # debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# # un bonus para que aparezcan exactamente como se muestra a continuación)

# # Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave,
# #  la función imprima el valor almacenado en esa clave para cada diccionario.
# #  Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterateDictionary2(key_name, some_list):
        valor=''

        for dato in some_list:
            valor += f"{dato[key_name]}\n" 

        return valor
print(iterateDictionary2('first_name', estudiantes))
print(iterateDictionary2('last_name', estudiantes))

# # Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas,
# # imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores 
# # asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


# # string ="ABCDEFG"
# # print(f"Este es un numero {str(10)}")

def printInfo(diccionario):

   for x in diccionario: 
      print("\n") 

      print(len(diccionario[x]),x)
      for y in diccionario[x]:
         print(y)

printInfo(dojo)
