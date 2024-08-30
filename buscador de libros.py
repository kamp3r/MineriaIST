class Libro:
    libros_lista = []

    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion
    def agregar_libro(libro):
        titulo = input("Ingresa el titulo del libro: ")
        autor = input("Ingresa el autor del libro: ")
        genero = input("Ingresa el genero del libro: ")
        puntuacion = float(input("Ingresar la puntuacion: "))
        final = libro(titulo,autor,genero,puntuacion)
        libro.libros_lista.append(final)
        print(f"El Libro '{titulo}' fue agregado a la lista")
    def buscar_genero(lista):
        genero = input ("Ingresa el genero que te interesa: ")
        libros_coincidencia = [bk.titulo for bk in lista if bk.genero.lower() == genero.lower()]
        if libros_coincidencia:
            print(f"Libros encontrados en el genero '{genero}':")
            for titulo in libros_coincidencia:
                print(f"{titulo}\n")
        else:
            print((f"No se encontraron libros con dicho genero"))
    def recomendar_libro(lista):
        genero = input ("Ingresa el genero que te interesa: ")
        libros_coincidencia = [bk for bk in lista if bk.genero.lower() == genero.lower()]
        if libros_coincidencia:
            elegido = max(libros_coincidencia, key=lambda libro: libro.puntuacion)
            print(f"Te recomendamos leer '{elegido.titulo}' del autor '{elegido.autor}'")
        else:
            print((f"No se encontraron libros con dicho genero"))

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficcion", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficcion", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasia", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clasico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clasico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasia", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasia", 4.0)

# Agregar libros a la lista
Libro.libros_lista.extend([libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10])

# Función principal para ejecutar el bucle de la aplicación
def ejecutar_aplicacion():
    while True:
        print("Menú:")
        print("1. Agregar Libro")
        print("2. Buscar Libros por Género")
        print("3. Recomendar Libro")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            Libro.agregar_libro(Libro.libros_lista)
        elif opcion == "2":
            Libro.buscar_genero(Libro.libros_lista)
        elif opcion == "3":
            Libro.recomendar_libro(Libro.libros_lista)
        elif opcion == "4":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.\n")

ejecutar_aplicacion()