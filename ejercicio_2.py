class Libro:
    def __init__(self, titulo_libro:str, nombre_autor:str, precio_libro:float):
        self.titulo_libro=titulo_libro
        self.nombre_autor=nombre_autor
        self.precio_libro=precio_libro
        
        
    def mostrar_informacion(self):
        print(f"Titulo del libro: {self.titulo_libro}")
        print(f"Nombre del autor: {self.nombre_autor}")
        print(f"Precio del libro: {self.precio_libro}")
        
def main():
    libro_1=Libro("100 Ejercicios Python para practicar", "Laurentine K.Masson", 9.99) 
    libro_1.mostrar_informacion()

if __name__ =="__main__":
    main()
        