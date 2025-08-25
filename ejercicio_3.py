class Notas:
    def __init__(self, nombre_estudiante:str, nota:int):
        self.nombre_estudiante=nombre_estudiante
        self.nota=nota
        
    def ha_pasado(self):
        print(f"Nombre: {self.nombre_estudiante}")
        print(f"Nota: {self.nota}")
        
        if self.nota >= 75:
            print("Aprobado")
        else:
            print("Reprobado")
            
def main():
    nota_1=Notas("Julien", 80)
    nota_1.ha_pasado()
    
if __name__ == "__main__":
    main()