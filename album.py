# Crear un diccionario vacío para almacenar los datos de la canción
cancion = {}

# Crear listas vacías para almacenar los nombres de canciones, autores, cantantes, álbumes y años de lanzamiento
nombres_canciones = []
autores = []
cantantes = []
albumes = []
años_lanzamiento = []

# Pedir al usuario que ingrese los datos de la canción
nombre_cancion = input("Ingrese el nombre de la canción: ")
autor = input("Ingrese el nombre del autor de la canción: ")
cantante = input("Ingrese el nombre del cantante de la canción: ")
album = input("Ingrese el nombre del álbum de la canción: ")
año_lanzamiento = input("Ingrese el año de lanzamiento del álbum: ")

# Agregar los datos de la canción a la lista correspondiente
nombres_canciones.append(nombre_cancion)
autores.append(autor)
cantantes.append(cantante)
albumes.append(album)
años_lanzamiento.append(año_lanzamiento)

# Agregar los datos de la canción al diccionario
cancion['Nombre de la canción'] = nombres_canciones
cancion['Autor'] = autores
cancion['Cantante'] = cantantes
cancion['Álbum'] = albumes
cancion['Año de lanzamiento'] = años_lanzamiento

# Imprimir los datos de la canción
print(cancion)

#buscar artista 
cantante_name = 'Nombre del cantante'
cancion_name = 'Nombre del cancion'