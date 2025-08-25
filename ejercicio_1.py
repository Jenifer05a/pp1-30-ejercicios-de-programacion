class Galleta:
    def __init__(self, nombre:str, forma:str):
        self.nombre=nombre
        self.forma=forma
        

    def metodo_hornear(self):
        print(f"{self.nombre} tiene forma de {self.forma}")
        print("¡Buen provecho!")
        
    
def main():
    galleta_1= Galleta("Galleta de chocolate", "Estrella")
    galleta_1.metodo_hornear()
    
if __name__ =="__main__":
    main() 