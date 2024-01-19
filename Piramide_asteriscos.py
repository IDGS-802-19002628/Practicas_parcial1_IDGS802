import os


class piramide:
    # Declaracion de propiedades
    num1 = 0
    i = 0
    orde = 0
    j = 0
    # Declaracion de constructor

    def __init__(self, a):
        self.num1 = int(a)
        int(self.i)

    # Declaracion de metodos de clase
    def imprimir_piramide(self):
        
        for self.i in range(self.num1+1):
            self.orde = self.num1-self.i
            print(' '*self.orde+"* "*self.i)


# Declaracion de la función main fuera de la clase


def main():
    # Lineas para limpiar la terminal
    os.system('cls')
    num = input('Ingresa la cantidad de numeros desea registrar\n')
    obj = piramide(num)
    obj.imprimir_piramide()


if __name__ == "__main__":
    main()
