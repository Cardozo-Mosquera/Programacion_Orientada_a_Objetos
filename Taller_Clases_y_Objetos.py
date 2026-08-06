class Libro:

    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro

        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True

    
    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            return "El libro " + self.titulo + " ha sido prestado."
        else:
            return "El libro " + self.titulo + " no está disponible."

    
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            return "El libro " + self.titulo + " ha sido devuelto."
        else:
            return "El libro " + self.titulo + " ya estaba en la biblioteca."

    
    def informacion(self):

        if self.disponible == True:
            estado = "Disponible"
        else:
            estado = "Prestado"

        texto = "Título: " + self.titulo + "\n"
        texto = texto + "Autor: " + self.autor + "\n"
        texto = texto + "Páginas: " + str(self.paginas) + "\n"
        texto = texto + "Estado: " + estado

        return texto



def main():

    
    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
    libro2 = Libro("La Metamorfosis", "Franz Kafka", 128)

    
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print()
    print(libro2.informacion())
    print()

    
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print()

    
    print("=== Intento de prestar un libro ya prestado ===")
    print(libro1.prestar())
    print()

    
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print()

    
    print("=== Devolución del libro ===")
    print(libro1.devolver())
    print()

    
    print("=== Intento de devolver un libro ya disponible ===")
    print(libro1.devolver())
    print()

    
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print()
    print(libro2.informacion())


if __name__ == "__main__":
    main()